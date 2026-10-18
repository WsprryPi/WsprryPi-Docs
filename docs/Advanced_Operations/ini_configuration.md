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
