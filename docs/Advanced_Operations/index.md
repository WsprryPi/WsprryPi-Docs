# Advanced Operations

Use this section when normal web UI operation is not enough and you need timing, calibration, direct configuration, service interfaces, or RF hardware details.

Start with [Transmission Timing and Calibration](timing_calibration.md) when a transmission starts at the wrong time or RF frequency accuracy needs attention. For normal configuration and operation, use the [User Interface](../User_Interface/index.md).

## Critical PHP2Shell security maintenance

**I strongly recommend that every operator upgrade all of their WsprryPi devices promptly. Stable installations should move to v3.2.1, and every device must receive its distribution's PHP security updates. — Lee C. Bussy, maintainer**

PHP2Shell includes two critical PHP vulnerabilities, [CVE-2026-109618](https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w) and [CVE-2026-109619](https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp), each rated CVSS v4.0 9.2/10. In susceptible configurations, an attacker who can reach the PHP web service can execute code without logging in, with the web worker's privileges.

Use the [PHP2Shell audit and upgrade instructions](https://github.com/WsprryPi/WsprryPi/blob/v3.2.1/scripts/README.md#php2shell-configuration-audit-and-partial-mitigations) to review every device's PHP packages and web configuration. **Upgrading WsprryPi or applying partial configuration mitigations alone does not fix PHP2Shell.** Install the vendor PHP security updates, fully restart the serving PHP workers, and verify the actual serving PHP version and settings. Include private-LAN devices; development and Beta installations also need PHP updates without downgrading their WsprryPi application. See the [3.2.1 security release notes](https://github.com/WsprryPi/WsprryPi/releases/tag/v3.2.1).

```{toctree}
:maxdepth: 1
:hidden:

Transmission Timing and Calibration <timing_calibration>
INI Configuration Reference <ini_configuration>
Configuration Troubleshooting <configuration_troubleshooting>
REST API <rest_api>
WebSocket Interface <websocket>
RF and Electrical Reference <rf_electrical>
```

## Topics

(transmission-timing)=
(frequency-calibration)=
(gpio-based-transmissions)=
(si5351-based-transmissions)=
(am-calibration)=
- [Transmission Timing and Calibration](timing_calibration.md) explains WSPR timing, GPIO and Si5351 frequency calibration, and manual AM zero-beat calibration.

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

(pwm-peripheral)=
(rf-and-electrical-considerations)=
- [RF and Electrical Reference](rf_electrical.md) covers the GPIO PWM restriction, filtering, power-supply noise, isolation, and electrical protection.
