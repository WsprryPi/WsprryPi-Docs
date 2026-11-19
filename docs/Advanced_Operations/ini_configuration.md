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

## Existing WTP configuration

WTP transmission and inbound listener settings are retired. Review
[legacy configuration and recovery](ini_configuration/runtime.md#retired-wtp-configuration)
before replacing software on a deployment that used them. Current transmitter
settings select a native Pi backend; Pico connections are management profiles.



## Device-owned scheduling configuration

The local Pi management API stores scheduling separately from the INI. Its
`pi-scheduling` capability reports `next_occurrence`. Complete legacy retirement
or **Set up this transmitter** before explicitly enabling native recurrence.
Saving solar settings does not enable scheduling, Transmit, or Enable on Boot.
The web interface does not yet provide a solar scheduling editor; advanced
clients use the [protected target API](rest_api.md#local-pi-device-owned-scheduling).

Scheduling settings are stored in `<active-INI-path>.managed-settings.json`.
The daemon publishes settings and operation receipts in a recoverable transaction;
ordinary INI saves and reloads retain the policy. Bounded recurrence progress is
stored in `<active-INI-path>.recurrence-progress.json`. Keep established settings,
authority, progress, and recovery files together. Do not hand-edit or delete them
to repair an error. Solar fields are not INI keys.

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
locator. Native Pi GPS is unavailable. Saving a draft does not require time
synchronization; actual solar admission requires healthy target-local UTC in
2025–2099. Geometry uses UTC without timezone or daylight-saving rules. See
[native recurrence and time readiness](ini_configuration/runtime.md#native-recurrence-and-time-readiness)
for the supported provider, uncertainty, holdover, and recovery behavior.
