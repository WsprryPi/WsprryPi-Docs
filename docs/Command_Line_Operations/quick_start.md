# Command-Line Quick Start

Use this page to stop the managed service safely, understand the command-line forms, and run common one-off WSPR commands.

## `systemd` Service

The `wsprrypi` executable is managed by Linux `systemd`. It runs in the
background after boot, and only one instance is allowed at a time. Stop the
daemon before running manual CLI commands.

Useful commands:

- `sudo systemctl status wsprrypi`  
  Show current status and recent logs.

- `sudo systemctl restart wsprrypi`  
  Restart the daemon and reload configuration.

- `sudo systemctl stop wsprrypi`  
  Stop the daemon. It starts again on reboot unless disabled.

- `sudo systemctl start wsprrypi`  
  Start the daemon manually.

- `sudo systemctl disable wsprrypi`  
  Prevent daemon startup on boot.

- `sudo systemctl enable wsprrypi`  
  Enable daemon startup on boot.

---

## Command Line Overview

The CLI supports two primary modes:

- **Direct CLI mode**  
  Run WSPR or CW-based transmissions directly.

- **INI (daemon-style) mode**  
  Use `-i` to load and monitor a configuration file.

### Usage

```text
(sudo) wsprrypi [options] CALLSIGN GRID POWER FREQ [FREQ...]
(sudo) wsprrypi -i /path/to/wsprrypi.ini
(sudo) wsprrypi --test-tone RF_FREQ [backend/options]
(sudo) wsprrypi --mode QRSS --cw-message TEXT --cw-base-frequency FREQ
```

---

## Common Examples

- `wsprrypi --help`  
  Display help text.

- `sudo wsprrypi --test-tone 780kHz`
  Transmit a constant RF tone at 780 kHz. Frequency inputs use whole-number
  hertz, or a value with an `Hz`, `kHz`, `MHz`, or `GHz` suffix that resolves
  to whole-number hertz. Scientific notation and fractional-hertz results are
  rejected. Band aliases resolve to their WSPR dial frequencies; use an
  explicit frequency when the test carrier should differ from the dial. See
  [Canonical Bands and WSPR Frequency Presets](../Advanced_Operations/canonical_bands.md)
  for qualified 60 m presets and country/locality selection.

- `sudo wsprrypi N9NNN EM10 33 20m`  
  Transmit a single WSPR message.

- `sudo wsprrypi --use-ntp N9NNN EM10 33 20m`  
  Use NTP calibration before transmission.

- `sudo wsprrypi --repeat --offset --use-ntp N9NNN EM10 33 40m`  
  Continuous transmissions with offset randomization.

---

## Positional Arguments

These are required for direct WSPR transmission unless provided via INI:

- **CALLSIGN**  
  Your callsign or supported WSPR identity form. Standard Type 1 WSPR
  messages use a normal callsign that fits the classic WSPR field. When the
  supplied identity cannot be represented as a single Type 1 message, the
  planner can use paired WSPR message planning where supported. This allows
  Type 2 and Type 3 message forms for extended callsign/grid combinations.

- **GRID**  
  Maidenhead grid square or locator value used by the WSPR planner. Standard
  Type 1 messages use the normal four-character Maidenhead grid square. For
  identities that require paired planning, the grid and callsign are evaluated
  together so the planner can select the appropriate Type 2/Type 3-capable
  message strategy when available.

- **POWER**  
  Transmit power in dBm. The value is rounded to valid WSPR steps and included
  in the transmitted WSPR message where the selected message type supports it.

- **FREQ**  
  One or more frequencies or band aliases.  
  Examples: `20m`, `14097100`, `0` (skip slot)
