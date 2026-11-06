# Advanced Operations

Use this section when normal web UI operation is not enough and you need timing, calibration, direct configuration, service interfaces, or RF hardware details.

Start with [Transmission Timing and Calibration](timing_calibration.md) when a transmission starts at the wrong time or RF frequency accuracy needs attention. For normal configuration and operation, use the [User Interface](../User_Interface/index.md).

```{toctree}
:maxdepth: 1
:hidden:

Transmission Timing and Calibration <timing_calibration>
Canonical Bands and WSPR Frequency Presets <canonical_bands>
INI Configuration Reference <ini_configuration>
Configuration Troubleshooting <configuration_troubleshooting>
REST API <rest_api>
WebSocket Interface <websocket>
Raspberry Pi 5 RP1 GPCLK <rp1_gpclk>
RF and Electrical Reference <rf_electrical>
```

## Topics

(transmission-timing)=
(frequency-calibration)=
(gpio-based-transmissions)=
(si5351-based-transmissions)=
(am-calibration)=
- [Transmission Timing and Calibration](timing_calibration.md) explains WSPR timing, frequency calibration for GPIO and Si5351, and manual AM zero-beat calibration.

(canonical-band-correlation)=
- [Canonical Bands and WSPR Frequency Presets](canonical_bands.md) explains frequency-to-band correlation, built-in WSPR dial presets, profiles, per-band preferences, and country/locality selection.

(ini-file)=
- [INI Configuration Reference](ini_configuration.md) documents the complete daemon configuration file, including WSPR, CW, hardware, and scheduling values.

(troubleshooting-cw-configuration-saves)=
- [Configuration Troubleshooting](configuration_troubleshooting.md) explains recoverable CW timing validation and configuration reload failures.

(rest-and-websocket-interfaces)=
(rest-api)=
(configuration-endpoint)=
(version-endpoint)=
- [REST API](rest_api.md) documents the proxied HTTP interface, configuration operations, and version metadata.

(websocket-interface)=
(available-commands)=
(broadcast-events)=
(configuration-reload)=
(transmission-start)=
(transmission-complete)=
(transmission-cancelled)=
(test-tone-state)=
- [WebSocket Interface](websocket.md) documents commands, runtime broadcasts, transmission lifecycle events, and browser synchronization.

- [Raspberry Pi 5 RP1 GPCLK](rp1_gpclk.md) explains installer-managed provider
  lifecycle, route identities, reboot transactions, recovery, and diagnostic
  evidence.

(pwm-peripheral)=
(rf-and-electrical-considerations)=
- [RF and Electrical Reference](rf_electrical.md) covers the GPIO PWM restriction, filtering, power-supply noise, isolation, and electrical protection.
