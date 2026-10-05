# Transmitter Backend Options

## Backend Selection

<!-- if-wsprrypico -->
- `--backend <gpio\|si5351\|wtp>`
<!-- else-wsprrypico -->
- `--backend <gpio\|si5351>`
<!-- endif-wsprrypico -->
  Select RF output method.  
  - `gpio`: Direct RF from Raspberry Pi GPIO (limited models).  
  - `si5351`: External clock generator via I2C.
<!-- if-wsprrypico -->
  - `wtp`: WsprryPico over its dedicated USB WTP interface, Plain LAN, or
    authenticated TLS network connection on Linux. The binding comes from
    `[WTP] Transport` in the selected INI file.
<!-- endif-wsprrypico -->

- `--power-level <level>`  
  Set transmit power for the active backend:  
  - GPIO: 0–7  
  - Si5351: 1–4

- `--gpio-power-level <0-7>`  
  Explicitly set GPIO drive strength.

- `--si5351-power-level <1-4>`  
  Set Si5351 output drive strength.

## Experimental Frequency Policy

These advanced options are available from the command line and INI file. They
are intentionally not exposed in the Web UI, and both default to disabled.

- `--allow-unqualified-frequency`, `--no-allow-unqualified-frequency`
  Allow or deny a backend, hardware profile, band, and mode combination whose
  recorded state is **Untested** or **Unqualified**. This option cannot enable
  an **Unavailable** output that the selected backend cannot safely construct.

- `--allow-non-amateur-frequency`, `--no-allow-non-amateur-frequency`
  Allow or deny a frequency outside WsprryPi's recognized US and international
  amateur-band ranges. Outside-band transmission requires both allow options.

These options do not grant permission to transmit. The operator remains
responsible for authorization, RF-path safety, filtering, and compliance with
applicable rules.

### Precedence

When `--ini-file` is present, WsprryPi loads the INI file first and then
applies these CLI switches to the current process. A CLI switch therefore
overrides the corresponding `[Experimental]` INI value at startup without
rewriting the INI file. Switches are processed from left to right; if a switch
is repeated, its last occurrence wins. If the monitored INI file is later
changed and its reload is accepted, the reloaded INI values become the live
settings for subsequent transmission decisions.

With an authorized frequency and a suitable attenuated, filtered RF path or
dummy load, this command permits an Untested or Unqualified combination on a
recognized amateur band for the current process:

```bash
sudo wsprrypi --allow-unqualified-frequency --test-tone 137500Hz --backend gpio
```

A frequency outside WsprryPi's recognized amateur-band ranges requires both
positive switches:

```bash
sudo wsprrypi --allow-unqualified-frequency --allow-non-amateur-frequency \
  --test-tone 30000000Hz --backend si5351
```

The second command still fails if the selected backend cannot construct the
requested output safely. To load an INI file that enables both settings but
deny outside-band operation for this process, use the explicit negative form:

```bash
sudo wsprrypi --ini-file /usr/local/etc/wsprrypi.ini \
  --no-allow-non-amateur-frequency
```

The last occurrence controls the effective value. This example leaves the
unqualified-frequency override enabled and the non-amateur-frequency override
disabled:

```bash
sudo wsprrypi --allow-unqualified-frequency \
  --allow-non-amateur-frequency --no-allow-non-amateur-frequency \
  --test-tone 137500Hz --backend gpio
```

### Confirm the active settings

The Web UI and runtime status do not display these advanced settings. For a
direct CLI run, inspect the command that started the process and apply the
left-to-right, last-occurrence rule above. For the managed service, first show
the running command and identify the file passed to `--ini-file`:

```bash
main_pid="$(systemctl show --property MainPID --value wsprrypi)"
ps -ww -p "$main_pid" -o args=
```

Then inspect the `[Experimental]` section in that exact INI file. CLI switches
shown in the running command take precedence at startup. After editing a
monitored INI file, confirm that the journal reports `INI file changed,
reloading.` and does not report that the reload was rejected. An accepted
reload makes the file values effective for subsequent transmission decisions:

```bash
journalctl -u wsprrypi --since "10 minutes ago"
```

A support bundle includes the installed INI file, service definition, process
details, and recent logs for the same review. It does not turn these controls
into Web UI settings or establish operating authority.

---

## GPIO Backend

GPIO qualification depends on the Raspberry Pi clock profile, band, and
transmission mode. A band can be qualified for TONE, QRSS, FSKCW, or DFCW while
WSPR remains unqualified. Requests for unqualified combinations are rejected
before GPIO activation unless the experimental override is enabled; unavailable
combinations remain blocked. Check the current [Band qualification](../About_Wsprry_Pi/index.md#band-qualification)
table and its numbered notes before transmitting.

A steady test tone is not sufficient evidence that WSPR modulation will
decode. See [GPIO Band Capabilities and Signal Quality](../FAQ/why_12m_looks_noisy.md)
for the underlying signal-quality findings.

- `--transmit-gpio <4\|20>`  
  Select GPIO pin used for RF output.

- `--transmit-pin <4\|20>`  
  Legacy alias for transmit GPIO.

- `-n`, `--use-ntp`  
  Enable NTP-based frequency calibration.

- `--no-use-ntp`  
  Disable NTP calibration and use manual PPM.

- `-p`, `--ppm <value>`  
  Apply manual frequency correction (-200 to 200 ppm).

---

## Si5351 Backend

- `--si5351-i2c-bus <bus>`  
  Select I2C bus (default: 1).

- `--si5351-i2c-address <addr>`  
  Set the device address in decimal or `0x`-prefixed hexadecimal. Valid
  addresses are `0x60` through `0x6F` inclusive.

- `--si5351-reference-frequency <hz>`  
  Define reference oscillator frequency.

- `--si5351-reference-source <external_tcxo|crystal>`
  Select an active external clock/TCXO or a passive crystal. Missing settings default to `external_tcxo`.

- `--si5351-crystal-load-capacitance <6|8|10>`
  Set the internal load capacitance used only with `--si5351-reference-source crystal`. The default is 10 pF.

- `--si5351-tx-output <CLK0\|CLK1\|CLK2>`  
  Select output clock. This option is not exposed in the Web UI.


<!-- if-wsprrypico -->
## Pico WTP Backend

Select `--backend wtp` and supply the endpoint through `--ini-file` (`-i`).
`[WTP] Transport` chooses USB (`usb`, the legacy default), Plain LAN
(`network_plain`), or authenticated TLS (`network`). For USB, use the dedicated
WTP function, not the Pico Console. For a network binding, set `Hostname`
and `TCP Port`; TLS also requires provisioned host-side CA, client
certificate, and client-key files. Configure the
[WTP INI section](../Advanced_Operations/ini_configuration/transmitter_backends.md#pico-wtp)
first, with transmission and automatic startup disabled.

There is no command-line option to browse DNS-SD services, edit the known-device
catalog, or choose a saved Fleet profile. The Fleet development pane is hidden
at every page load. When enabled for a session, **Use this device** explicitly
copies a selected profile into the active `[WTP]` configuration. Running
`--backend wtp` by itself does not choose a catalog profile and does not
override `Transmit = true` in an INI file. Direct and manual endpoints remain
usable when discovery is unavailable.

The host and Pico each need independently valid UTC. The default Pico start
uncertainty budget is 1 ms; choose a larger value only with device clock
evidence. Finite WSPR, QRSS, FSKCW, and DFCW jobs use the Pico's local timing.
Continuous `--test-tone` is unavailable for WTP. Host PPM must be zero, and
ancillary GPIO controls and CW fades must be disabled before selecting WTP.

WTP band/mode combinations remain untested in the host frequency policy and
require the explicit unqualified-frequency option described above. A successful
USB or network connection, discovery advertisement, or completed job does not
qualify RF output.

Review [Pico status and recovery](../User_Interface/Setup/Transmitter/index.md#pico-status-and-recovery)
before operation. Closing a connection or exiting WsprryPi does not prove the
Pico has stopped. An unresolved job blocks further work; recovery must
establish the current device state without resuming or taking another owner's
job.
<!-- endif-wsprrypico -->

<!-- if-wsprrypico -->
## Pi WTP server capability

A managed Pi can expose its local transmitter to a central Pi through Plain
LAN WTP. This is independent of choosing `--backend wtp` for an outbound
endpoint. Configure the server in
[`[WTP Server]`](../Advanced_Operations/ini_configuration/runtime.md#wtp-server)
and use [Fleet output assignments](../User_Interface/Setup/index.md#assign-an-output-schedule)
on the controller.

The selected native **GPIO, RP1 GPCLK or Si5351** backend exposes **WSPR,
TONE, QRSS, FSKCW and DFCW** through the same WTP server. GPIO uses the selected
transmit pin, drive and clock correction; RP1 uses its kernel provider, selected
GPIO4/GPIO20 route and drive; Si5351 uses its bus, address, reference, CLK output,
drive and PPM settings.

CAPS reports the selected backend's numerical clock or planner envelope.
Si5351's envelope is 7,812.5 Hz through 200 MHz; its existing qualified bands
from 2200m through 2m retain their qualification, and 8m/5m retain their separate
experimental policy. GPIO retains its processor-specific frequency policy.
Each job must satisfy the selected backend's native tone plan and frequency
policy. Backend selection remains explicit.

RP1 retains its existing development authorization. A WTP job requires the
host's existing development confirmation for that exact job ID and selected
route. Fleet does not create that confirmation.

Finite jobs may contain up to 512 contiguous events and have a total duration
up to 24 hours. These are protocol resource limits. Frequency changes and
RF-off intervals, including an initial silent interval, use the backend's
precomputed execution plan. Per-event realized frequencies come from that same configured
clock or tone plan and require adjustment consent when they differ from the request.

The server requires synchronized UTC, at least two seconds of ARM lead, and
reported UTC uncertainty no greater than 500 ms. The controller profile must
also allow the target's reported uncertainty. Reported frequency realization
requires explicit permission for adjustment; it is not a measured RF frequency.
Output-disable timeout is five seconds; unconfirmed output-off inhibits further
work. The WTP integration preserves the existing backend qualification; it does not
establish a new claim about measured frequency accuracy or long-term timing.

For legacy GPIO, forcibly terminating the controlling process can leave the
clock output active until startup quiescence runs on restart. The five-second
output-disable timeout applies while the process is responsive. A killed
process or closed connection does not confirm output-off; review the restored
endpoint and [reconcile local output](../User_Interface/index.md#local-control-and-remote-ownership).

Protocol details are maintained in the
[WsprryPico protocol documentation](https://github.com/WsprryPi/WsprryPico/tree/devel/docs/protocol).
<!-- endif-wsprrypico -->
