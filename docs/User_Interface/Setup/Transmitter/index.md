# Transmitter Configuration Tab

The Transmitter tab on the Signal Setup page contains settings related to the active output hardware path and transmission behavior.

Use the **RF Output Path** switch to choose between GPIO and Si5351. The switch
shows GPIO on the left and Si5351 on the right; switch it off for GPIO or on for
Si5351. The same RF Output panel then shows only the settings for that hardware.
On wide screens those controls share one row. On smaller screens they wrap or
stack without changing their order.

- **GPIO** - Available on earlier Raspberry Pi models and on Pi 5 when the
  installer-managed RP1 GPCLK provider and selected route are eligible.
- **Si5351** - If detected, the Si5351 may be used on any supported Raspberry Pi.
<!-- if-wsprrypico -->
- **Pico via WTP** - Development controls support USB, Plain LAN, and
  authenticated network connections on Linux. Fleet remains hidden on every
  page load.
<!-- endif-wsprrypico -->

## GPIO

GPIO-based transmissions are the typical method most people think of when they think of WsprryPi.  It uses a GPIO Pin attached to a clock generator on the Pi to transmit WSPR tones.

On Pi 5-family systems, the normal installer supplies and validates the RP1
GPCLK provider but leaves both routes unselected and output disabled.
Installation alone does not qualify either route or authorize transmission.

For the legacy GPIO backend, conducted testing qualifies 80 m, 20 m, 15 m, and 10 m with
the production pacing value. WsprryPi rejects legacy GPIO requests in the 12 m, 6 m,
and 2 m band ranges before transmitter activation. The restriction applies to
scheduled operation and Test Tone and does not limit the Si5351 backend. See
[GPIO Band Capabilities and Signal Quality](../../../FAQ/why_12m_looks_noisy.md).

There are only two choices when setting up the GPIO-based transmitter:

### Transmit Pin

GPIO4 and GPIO20 are the supported direct RF output choices. The selected pin is reserved by the GPIO backend even when transmission is disabled, because WsprryPi must retain ownership of the configured RF path for startup and safe-state handling.

On Pi 5, the route panel distinguishes **Requested** from **Active**. Selecting
the other pin or None creates a draft; it does not autosave or redirect
committed work. When the transmitter is completely idle, choose **Switch
route** for GPIO4 or GPIO20. Choose **Remove route** for None. Choose **Cancel**
to restore the persisted selection without changing the Pi.

Switching and removal happen in the current boot and do not require a reboot.
The status dialog remains visible through the brief controller disconnect and
checks the result without repeating the operation. If WsprryPi was running,
successful removal brings it back online and idle. A service that was already
stopped or administrator-masked remains stopped or masked.

The panel distinguishes checking, plan ready, switching, restoring, route
selected, removing, route removed, service stopped, restoration failed, and
recovery-required states. Transmission remains disabled during an unresolved
transaction. **Recover to no route** is an exceptional fail-closed action: it
leaves WsprryPi stopped and the controller inhibited for investigation. Use
**Remove route** for normal removal. See [Raspberry Pi 5 RP1 GPCLK](../../../Advanced_Operations/rp1_gpclk.md)
for recovery guidance.

WsprryPi permits RP1 transmission only when the route and eligibility
evidence agrees exactly.

The other pin remains available on the **Pi I/O** tab. Selecting the Si5351 backend releases both GPIO4 and GPIO20 for ordinary GPIO roles; the retained GPIO transmit-pin value is ignored while Si5351 is selected.

If an existing configuration assigns the selected RF pin to an enabled ordinary GPIO role, both controls remain visible and are marked invalid until one assignment is changed or disabled. Invalid edits are not saved.

### GPIO Power Level

These are output driver strength levels mapped within the Pi's GPIO registers.  You may adjust the output from 0-7 with the slider.  The values roughly align to power levels at the pin before any amplification or filtering:

1. 2 mA: ~-7.0 dBm
2. 4 mA - ~-1.0 dBm
3. 6 mA - ~2.6 dBm
4. 8 mA - ~5.1 dBm
5. 10 mA - ~7.0 dBm
6. 12 mA - ~8.6 dBm
7. 14 mA - ~9.9 dBm
8. 16 mA - ~11.1 dBm

Actual output should be measured with the entire circuit and antenna.

## Si5351

The Si5351 is selectable as an output device on all supported Pi versions. If
the application cannot validate communication with the Si5351, the RF Output
panel reports that the device was not detected.

### I2C Bus

Choose one of the I2C buses detected on the Raspberry Pi. WsprryPi lists only
buses currently exposed by Linux with a corresponding I2C device. If the saved
bus is no longer available, it remains identified as unavailable but cannot be
selected; choose another listed bus explicitly. Enable or attach an I2C bus,
then reload the page to refresh the list.

A listed bus confirms only that the Linux adapter is present. It does not
confirm access permissions, external-header routing, wiring, power, or an
attached Si5351.

### I2C Address

After a bus is selected, WsprryPi checks addresses `0x60` through `0x6F` and
lists only addresses that respond to the Si5351 register-read check. The saved
address remains selected only while it is detected on that bus. If it is
missing, the menu has no selection; choose a detected address explicitly.

The menu distinguishes discovery in progress, no compatible response, and a
discovery error. Select the bus again or reload the page to retry after fixing
wiring, power, permissions, or I2C configuration.

The standard Si5351 address is `0x60`; some boards support `0x61`, and
compatible devices or clones may use another address in the supported range.
The Si5351 does not provide a definitive silicon-identification register, so a
listed address means that a register-compatible device responded. Verify the
attached hardware before transmitting.

### Reference Frequency

You must configure the reference frequency installed on the clock-generator board. QRP Labs synthesizer kits are supplied with a 27 MHz crystal and support optional TCXO configurations; Adafruit breakout boards use a 25 MHz crystal. Either reference can generate many supported frequencies.

For qualified 2 m WSPR operation, use a 27 MHz reference. [QRP Labs selected 27 MHz](https://qrp-labs.com/images/synth/synth_assembly6.pdf) because its synthesis calculations preserve WSPR tone spacing through 145 MHz, while its 25 MHz configuration does not. WsprryPi's current planner can calculate the four 2 m tones from a 25 MHz reference, but WsprryPi has physically qualified only its 27 MHz reference configuration on 2 m. A 25 MHz reference therefore remains unqualified for 2 m rather than proven incompatible.

Enter the frequency that corresponds to the installed reference hardware.

### Reference Source

Choose **External clock / TCXO** for a module driven by an active reference. This is the default and preserves existing behavior. Choose **Passive crystal** only when a crystal is connected across the Si5351 XA/XB pins.

When **Passive crystal** is selected, the **Crystal Load Capacitance** menu appears with 6, 8, and 10 pF choices. Select the value specified for the installed crystal; 10 pF is the default. The menu is hidden and its value is not programmed when **External clock / TCXO** is selected.

### Si 5351 Power Level

The Si5351 has four configurable power levels:

1. 2mA - ~0 to +3 dBm
2. 4mA - ~+3 to +6 dBm
3. 6mA - ~+6 to +8 dBm
4. 8mA - ~+8 to +10 dBm

While these are technically feasible levels, the device is not intended to drive a load.  It should be followed by an amplifier of some sort.


<!-- if-wsprrypico -->
## Pico development controls

The **Fleet** tab is hidden and disabled on every page load. It is available
only when enabled for the current development session; that choice is not saved
as a browser preference. The instructions below apply only while Fleet is
visible. Showing or hiding it does not change the active endpoint or start a
transmission.

**Use Pico** selects the WTP backend in the saved host configuration. The
**Connection** choice supports USB, Plain LAN, and Network (TLS). Keep
transmission disabled while configuring a device. Disable TX LED, amplifier,
shutdown-button, and band GPIO controls first; host GPIO calibration and CW
fades do not apply. Set host PPM to zero. For USB, use the Pico's dedicated WTP
interface, not its Console port. For network connections, enter the hostname
and actual TCP port. TLS also needs host paths to the CA, client certificate,
and client key. See the [WTP INI reference](../../../Advanced_Operations/ini_configuration/transmitter_backends.md#pico-wtp)
for the individual settings.

**Maximum start uncertainty (ns)** defaults to 1000000 (1 ms). The Pico's own
clock evidence must meet this limit, and the host needs synchronized UTC.
**Allow device frequency rounding** accepts reported realizable frequencies;
it does not qualify RF accuracy. Continuous **Test Tone** is unavailable with
Pico; complete finite jobs use its local timing.

### Known and nearby devices

The selector separates **Saved devices** from **Nearby advertisements**. A
saved device stays listed when its advertisement disappears. An advertisement
is a connection hint, not proof of device identity, an active listener, or RF
readiness. If Avahi discovery is unavailable or no service appears, use
**Add device** for a manual USB or network profile. Merely opening the selector
or highlighting an entry does not connect, identify, save, or switch devices.

To add a nearby Pi or Pico, select its advertisement and choose **Add device**.
Review its connection type and the advertised SRV target and port. Give the
profile a name and enter the expected full 32-character WTP device ID. For
Network (TLS), provision the device-specific trust files on the host and enter
the expected certificate identity before identifying or saving it. For Plain
LAN, explicitly choose that binding and use **Identify selected nearby
device** to read HELLO, STATUS, and CAPS. Confirm the observed full device ID
before saving it. Plain LAN's reported ID is an unauthenticated observation;
the connection is neither encrypted nor client-authenticated. Identification
does not claim, arm, or recover a job.

**Save device** asks for confirmation and saves a profile only. It does not
change the active `[WTP]` endpoint. To apply a saved profile, select it and
choose **Use this device**. This separate action asks for confirmation and is
refused while transmission is enabled or the current Pico has pending, owned,
active, or unresolved work. Resolve that work and review Pico status before
trying again. Selection never enables transmission or resumes an old job.
Renaming, editing, or removing a saved profile also leaves the active endpoint
unchanged.

A DNS-SD profile keeps its saved endpoint. If the advertisement's target,
port, or binding changes, Fleet shows the difference and blocks a new use of
that profile until you edit it and a fresh identity check succeeds. Plain LAN
requires explicit review and consent again; neither binding silently follows
a changed advertisement or falls back to another binding. Manual profiles
keep their configured connection behavior.

For independent remote schedules alongside this Pi's local schedule, use
[Output schedules](../index.md#assign-an-output-schedule). The Pi server uses
Plain LAN and derives its supported modes and frequency limits from the
selected backend. Native GPIO, RP1 and Si5351 support finite WSPR, TONE, QRSS,
FSKCW and DFCW jobs under their existing backend policies. See
[Pi WTP server capability](../../../Command_Line_Operations/transmitter_backends.md#pi-wtp-server-capability)
for RP1's exact-operation development confirmation. The single-endpoint selection
and Pico status controls below
remain separate from those assignments.

### Pico status and recovery

**Pico status** shows **Output observed**, **Host UTC**, **Device / boot**, and
**Last job**. These are recorded observations, not electrical measurements.
Check their age and any reported failure. An unavailable status response means
unknown; it does not establish that the Pico is stopped. A previous job failure
remains in the history after cleanup.

If a job or connection becomes unresolved, disable transmission and review
the reported state. **Reconcile Pico** checks an idle device or reconnects the
current session to resolve its owned job. Recovery may stop that job. It never
resumes transmission, reloads an uncertain job, or takes another owner's job.
After successful reconciliation, review the current observation and
configuration before explicitly enabling transmission again.

Status polling does not perform recovery. A changed device or boot identity,
foreign ownership, or unresolved output blocks further work. Restarting the
host creates a new session and does not adopt the old session's job. Closing
USB or a network connection, or exiting the host application, is not proof of
RF shutdown.

### Pico standalone settings and Wi-Fi

Open **Pico standalone settings and Wi-Fi** in Fleet when the selected Pico
uses **Network (TLS)**. These controls manage settings saved on Pico for its
own standalone scheduler. They are separate from this Pi's schedule, output
assignments, and saved connection profile. USB and Plain LAN do not provide
this settings panel.

Keep WsprryPi transmission disabled while editing. Management requires an idle
host and confirmed Pico state, with no pending, owned, active, or unresolved
work. Use [Pico status and recovery](#pico-status-and-recovery) to resolve that
work first. Disabling transmission on the Pi does not disable Pico's standalone
scheduler: leave **Enable Pico standalone schedule** cleared until you intend
Pico to transmit autonomously and its clock and RF path are ready.

#### Load and save settings

1. Confirm the selected Pico and its **Device / boot** observation, then choose
   **Load saved Pico settings**. A normal load replaces the form's draft and
   clears any entered password. Status polling preserves the draft.
2. Edit the required fields. **WSPR power metadata (dBm)** is the reported WSPR
   power, not an RF output-drive control. **Time server** accepts an IPv4 address
   or a hostname supported by the Pico firmware.
3. Choose **Save Pico settings** and read the result below the controls. Saving
   applies the changed settings together. An unchanged form reports that no
   settings changed and performs no save.

Ordinary saves preserve settings outside this form, including Pico pin
assignments and advanced frequency-policy settings. On supported older firmware,
WsprryPi preserves the settings it understands when saving. If the firmware or
saved settings cannot be handled safely, it refuses the operation and keeps the
draft. Use compatible firmware or Pico's supported configuration workflow;
repeated saves do not bypass the refusal. If feedback says Pico setup owns the
station or Wi-Fi values, change them through Pico setup.

Reset individual values explicitly. For example, set **Schedule expiry (UTC
epoch seconds)** to `0` to remove expiry, or clear **Enable Pico standalone
schedule** and choose **Save Pico settings** to disable standalone scheduling.
The form has no whole-configuration reset or replacement control, and does not
edit pins or advanced frequency-policy settings.

#### Schedules and passwords

In **Standalone schedule periods and phases (seconds)**, enter one period and
phase per line, separated by a space, such as `120 0`. Use up to eight
nonoverlapping schedules. The period must divide 86400 seconds (one day), and
both values must be multiples of 120 seconds; the phase must be smaller than the
period. An enabled standalone schedule requires at least one entry.

**Save schedules only** changes the saved schedule entries while preserving
other saved settings and all unrelated form drafts, including an entered
password. It does not apply a draft enable/disable checkbox or expiry change;
use **Save Pico settings** for those changes.

For an already configured Pico, leave **New Wi-Fi password** blank to preserve
the saved credential. A blank entry does not erase it, and Pico never returns
the saved password to the form. Enter a new password only when changing it;
complete the credentials explicitly when configuring Pico for the first time.
A confirmed **Save Pico settings** clears the password entry. A failed or
unconfirmed save, or **Save schedules only**, keeps it. Keep this draft page
open during recovery; browser reload or navigation does not preserve the draft.

#### Saved changes and restart feedback

A confirmed save means Pico accepted the settings. Station and schedule changes
can apply to later transmissions without a restart. Saved network or pin changes
may still await a Pico restart, with the previous settings active in the current
boot. Read the reported restart requirement; saving does not request a restart.
If restart requirements are unconfirmed, check Pico status before operating.

**Read Pico Wi-Fi status** observes the current network state. **Disable Pico
Wi-Fi** disconnects network control and is a temporary switch, separate from
saved standalone settings. Re-enable it using the physical USB Console or a
restart; changing the saved Wi-Fi fields is not a reconnect control.

#### Conflicting or unconfirmed saves

A conflict means the saved settings changed since they were loaded. A timeout,
lost reply, or interrupted connection can leave a save's outcome unconfirmed:
the change may already have been saved. WsprryPi keeps the draft and password
entry, disables further saves, and does not automatically repeat the operation.

Confirm the intended Pico, resolve any busy or unresolved job state, then choose
**Load saved Pico settings**. After a conflicting or unconfirmed save, this load
keeps the draft and entered password and displays saved values beside the fields.
Compare them, adjust the draft as needed, and choose another Save only after
review. The redacted saved password cannot be compared with the retained entry;
review that entry separately before deciding to submit it again.
<!-- endif-wsprrypico -->
