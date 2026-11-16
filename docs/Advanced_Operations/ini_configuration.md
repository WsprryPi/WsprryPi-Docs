# INI Configuration Reference

The daemon reads `wsprrypi.ini` for its execution parameters. In normal use, configure WsprryPi through the [web interface](../User_Interface/Setup/index.md); edit the INI file directly only when a setting is not exposed there or a development workflow requires it.

The installer stores the configuration in the user data directory:

```bash
$ ls -al /usr/local/etc/wsprrypi.ini
total 12
drwxr-xr-x  2 root root 4096 Feb 18 14:51 .
drwxr-xr-x 10 root root 4096 Sep 21 19:02 ..
-rw-rw-rw-  1 root root  171 Mar  6 19:47 wsprrypi.ini
```

The file uses standard INI syntax with ten sections: `Meta`, `Security`, `Operation`, `Experimental`, `Calibration`, `GPIO`, `Si5351`, `WSPR`, `CW`, and `Band GPIO`. Blank lines and extra whitespace are ignored. Each setting is a key/value pair separated by an equals sign, and comments begin with a semicolon (`;`).

After editing, confirm the syntax and values before restarting WsprryPi or relying on the configuration for transmission.

```{toctree}
:maxdepth: 1
:hidden:

Runtime and Service Settings <ini_configuration/runtime>
Calibration and Transmitter Backends <ini_configuration/transmitter_backends>
WSPR Settings <ini_configuration/wspr>
CW and Band GPIO Settings <ini_configuration/cw_and_band_gpio>
Complete Default INI File <ini_configuration/complete_example>
```

## Configuration Areas

- [Runtime and Service Settings](ini_configuration/runtime.md) covers `[Meta]`, `[Security]`, `[Operation]`, and `[Experimental]`, including network safety, mode, service ports, transmission gating, control GPIOs, and experimental frequency policy.
- [Calibration and Transmitter Backends](ini_configuration/transmitter_backends.md) covers `[Calibration]`, `[GPIO]`, and `[Si5351]`.
- [WSPR Settings](ini_configuration/wspr.md) covers station identity, frequency, reported power, planning, and random offset.
- [CW and Band GPIO Settings](ini_configuration/cw_and_band_gpio.md) covers QRSS, FSKCW, DFCW, scheduling, fades, and band switching.
- [Complete Default INI File](ini_configuration/complete_example.md) provides the full copyable example and downloadable source.

## Development WTP configuration

Development builds also support `[WTP]` for the selected outbound endpoint and
`[WTP Server]` for this Pi's inbound listener. See the
[endpoint settings](ini_configuration/transmitter_backends.md#pico-wtp) and
[listener settings](ini_configuration/runtime.md#wtp-server). Independent Fleet
assignments are saved separately from the INI and from the device catalog.
Local Enable, listener admission, and remote assignment Enable are independent.

## Stored solar configuration

Development builds can save a disabled solar-policy draft through the local Pi
management API. The `pi-scheduling` capability reports `stored_only`: saving a
draft does not apply solar restrictions, start a schedule, or permit transmission.
The existing recurrence settings continue to apply. There is no solar scheduling
editor or activation control in the web interface.

The draft is stored in `<active-INI-path>.managed-settings.json`, beside the INI.
The daemon publishes the INI, managed settings, and operation receipt in one
recoverable transaction. Ordinary configuration saves and reloads retain the draft.
Keep these files and their private management journal together; do not hand-edit
or delete the sidecar to repair an error. Solar fields are not INI keys.

A draft has independent day and night permissions and optional morning and evening
windows. Windows use integer millidegrees from −90000 to 90000, with a lower bound
strictly below the upper bound. Defaults are −6000 and +6000. The lower bound is
included and the upper bound excluded. The evaluator treats day as solar-center
elevation at least −0.833°; a qualifying morning or evening window takes
precedence over day/night policy. Null frequency overrides inherit the saved
mode settings. WSPR overrides retain their list, skip entries, frequency profile,
band preferences, and per-entry selector metadata. CW bases are positive decimal
hertz with at most nine fractional digits; trailing fractional zeroes are omitted.
FSKCW and DFCW use the saved positive CW shift, with both derived tones validated.
Changed overrides are validated even when their period is disabled. Unchanged,
well-formed values that a backend no longer supports can be retained for repair;
retention does not qualify them for transmission.

The site is the center of the saved uppercase 4-, 6-, or 8-character Maidenhead
locator. Native Pi GPS is unavailable. Stored drafts do not sample the clock or
require time synchronization. The policy evaluator uses injected UTC between
2025-01-01 inclusive and 2100-01-01 exclusive, without timezone or daylight-saving
rules. Its readiness policy permits at most 250 ms uncertainty and at most one
hour of holdover following a healthy sample in the same boot, with 50000 ppb
uncertainty growth. Runtime solar admission is not available in this build.
