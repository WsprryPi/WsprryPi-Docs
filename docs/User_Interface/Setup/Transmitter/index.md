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
- **Pico via WTP** - Fleet supports USB, Plain LAN, and
  authenticated network connections on Linux. Open **Setup → Fleet** to add
  and manage a Pico output.

## GPIO

GPIO-based transmissions are the typical method most people think of when they think of WsprryPi.  It uses a GPIO Pin attached to a clock generator on the Pi to transmit WSPR tones.

On Pi 5-family systems, a fresh installation supplies and validates the RP1
GPCLK provider and establishes neutral administration with no route selected.
An update can restore an explicitly saved `rp1-gpclk` GPIO4 or GPIO20 route
after neutral activation, with transmission disabled. A retained GPIO pin for
another backend is not route consent. Installation alone does not qualify
either route or authorize transmission.

GPIO qualification depends on the processor clock profile, band and mode. Use
the accepted [band qualification table and numbered notes](../../../About_Wsprry_Pi/index.md#band-qualification).
Unqualified combinations are blocked by default in scheduled operation and
Test Tone; an experimental override cannot enable an Unavailable plan.
Si5351 has its own qualification. See
[GPIO Band Capabilities and Signal Quality](../../../FAQ/why_12m_looks_noisy.md)
for the retained signal-quality evidence.

The output controls select the transmit pin and drive; frequency calibration
is described [below](#gpio-frequency-correction-feedback).

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

The Si5351 is selectable on all supported Pi versions. Discovery establishes
register communication only. Unchecked or failed discovery leaves presence
unconfirmed; a completed scan with no compatible response is a different result.
Neither a responding address nor successful initialization proves RF readiness
under every operating condition.

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

Selecting Si5351 or loading it as the active backend requests fresh inventory
after the saved bus/address is populated. WsprryPi checks only `0x60` through
`0x6F`. Ordinary configuration and status reads use cached observations; they
do not scan an inactive Si5351 merely to fill the form.

The scan has a two-second deadline plus at most 25 ms of cleanup attempts.
Unchecked, checking, busy, timeout/error, and confirmed no compatible response
are distinct states. Busy or failed discovery keeps the saved address visible
as **unconfirmed**; timeout does not mean missing hardware. A completed scan
that does not find the saved address requires an explicit detected selection.

Wait for an outstanding worker to exit before retrying a busy scan. After a
communication failure, correct the reported bus, wiring, power or permissions
problem, then select the bus again or reload to request another bounded scan.
Saving a newly selected bus/address independently validates it on the server;
the browser's cached list is not authority to use it.

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

Levels **1, 2, 3, 4** retain **2, 4, 6, 8 mA** output drive respectively.
These are drive settings, not calibrated RF power. Measure the complete filtered
and loaded RF path independently; WSPR reported dBm does not set this drive.

### Readiness and recovery

Initialization waits for the device's initialization status before ordinary
programming. A later PLL/reference readiness fault or transport error during
execution ends that work and attempts output inhibition. Read the reported phase
and cleanup result: an I2C failure is different from a valid non-ready status.
Failed disable/readback leaves output uncertain and further output inhibited.

Keep transmission disabled, resolve the reported hardware or configuration
problem and establish exclusive ownership before recovery. Use the existing
stop/quiescence workflow; startup-inhibited processes require a service restart
after repair. Verify the resulting status before deliberately starting new work.
Recovery does not automatically resume the interrupted transmission. Startup
attempts to inhibit all Si5351 outputs; accepted writes or register readback
are not a measured RF-off guarantee.

CW fades switch the selected output on and off at its retained full drive.
They approximate an envelope by duty cycle; they do not vary analog amplitude.
See [CW envelope control](../../../Command_Line_Operations/cw_modes.md#envelope-control)
for slice/deadline limits and measurement boundaries.

## GPIO frequency correction feedback

**Frequency calibration** separates **System clock estimate**, **Residual PPM**
and **Fixed/manual PPM**. Candidate correction describes what a future request
would use. Committed correction belongs to the already prepared work and stays
fixed even when a newer estimate arrives or settings are saved. Displayed
effective/correction PPM is the additional term; chipset intrinsic compensation
is applied separately once.

Read the selected correction mode as well as estimate qualification. A currently
unavailable or converging report can still use a bounded prior-qualified value.
**age unknown** means freshness could not be established; it is different from
**age 0 s**. Source provenance describes selected/combined Chrony records, not
verified GNSS lock or measured RF accuracy. See
[Transmission Timing and Calibration](../../../Advanced_Operations/timing_calibration.md)
for intrinsic, residual, manual and zero-additional accounting.


## Add a Pico and manage outputs

Open **Setup → Fleet** to add a Pico to WsprryPi, select it for jobs from this
Pi, or assign independent schedules to several outputs. Fleet is available on
every page load. Opening the tab and browsing devices do not select an output,
save settings or start transmission.

Use a Pico 2 W running WsprryPico firmware. Connect its USB cable to the Pi
that runs WsprryPi, or connect both devices to a reachable network. Start with
the [device list](#known-and-nearby-devices), then choose either **Use this
device** for the Pi's single selected output or
[Assign a schedule](../index.md#assign-an-output-schedule) for an independent
fleet output. These are separate choices.

**Use Pico** selects the WTP backend in the saved host configuration. The
**Connection** choice supports USB, Plain LAN, and Network (TLS). Keep
transmission disabled while configuring a device. Disable TX LED, amplifier,
shutdown-button, and band GPIO controls first; host GPIO calibration and CW
fades do not apply. Set host PPM to zero. For USB, select the attached Pico from
the device list; WsprryPi fills its dedicated WTP connection and identifiers.
For network connections, enter the hostname
and actual TCP port. TLS also needs host paths to the CA, client certificate,
and client key. See the [WTP INI reference](../../../Advanced_Operations/ini_configuration/transmitter_backends.md#pico-wtp)
for the individual settings.

**Maximum UTC uncertainty (ns)** defaults to 100000000 (100 ms). Existing saved
limits are retained. The Pico's own
clock evidence must meet this limit, and the host needs synchronized UTC.
**Allow device frequency rounding** accepts reported realizable frequencies;
it does not qualify RF accuracy. Continuous **Test Tone** is unavailable with
Pico; complete finite jobs use its local timing.

### Known and nearby devices

The selector includes saved devices, attached USB Picos and nearby network
advertisements. A saved device stays listed when its advertisement disappears.
An advertisement
is a connection hint, not proof of device identity, an active listener, or RF
readiness. If Avahi discovery is unavailable or no service appears, use
**Add device** for a manual network profile. USB discovery is independent of
Avahi: a connected Pico running supported firmware appears automatically and
does not require entering a USB path, serial or vendor/product IDs. Its Console
and Management ports are not listed as separate transmitters. A board in BOOTSEL
mode does not expose the normal application connection. Merely opening the selector
or highlighting an entry does not connect, identify, save, or switch devices.

To add an attached USB Pico, select its entry and choose **Add device**, give it
a name, then review and save the supplied connection. Confirm the intended
board before choosing **Use this device**. For a nearby network Pi or Pico,
select its advertisement and choose **Add device**.
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

### Install or update Pico firmware over USB

Use this workflow for a selected USB Pico already running WsprryPico. Updates
retain its saved settings. Keep the Pico connected to the Pi throughout
programming and verification.

1. Disable transmission on the Pi, resolve any pending or owned Pico job, and
   select the intended Pico. Open **Pico firmware over USB** in Fleet.
2. Choose **main** or **devel** under **Firmware branch**. The default is
   **main**, independently of the Pi's branch. **Latest verified CI image**
   selects an available verified image from that branch; an unavailable image
   is refused without substituting another branch. A specific CI version or
   stable release can also be selected explicitly.
3. Choose **Read firmware status**, then **Download and check image**. Review
   the reported version, branch and source before choosing **Install checked
   image** and confirming the selected USB Pico.
4. Follow any BOOTSEL instructions shown by the tool. Older firmware needs a
   one-time migration and its standalone schedule must be disabled or
   unconfigured. When prompted, unplug that Pico, hold BOOTSEL while reconnecting
   it to the same Pi USB port, release BOOTSEL, then choose **Continue after
   BOOTSEL**. Preparation writes no firmware; continuation backs up and checks
   the saved state before completing the update.
5. Wait for **Verified** with confirmation that settings were preserved and
   the Pi reconnected. Check the current Pico status before enabling a Pi job
   or resuming its fleet schedule.

During firmware work or unresolved maintenance, settings, device selection,
transmission, reboot and shutdown controls are unavailable. **Read firmware
status** remains available and shows when its read completes; an unchanged
status can still be a successful read. Reading status never repeats the update.

If firmware is verified but the Pi connection remains unconfirmed, keep the
Pico connected and choose **Recover this update**. That state retries only the
Pi connection without reflashing. Other failed or interrupted updates retain
their recovery record and backup. Read the result before another attempt;
follow a requested BOOTSEL reconnect or seek administrator help rather than
clearing maintenance or choosing a different device.

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

Open **Pico standalone settings and Wi-Fi** in Fleet when you need to manage
the selected member's saved settings or network connection from WsprryPi.
These controls manage settings saved on the selected Pico for its own
standalone application. They are separate from this Pi's settings, prepared
jobs, output assignments and saved connection profiles. A USB connection uses
the Pico's paired USB management channel automatically. For network management,
Engineering HTTPS uses the configured
Network (TLS) credentials; supported consumer Wi-Fi or setup Wi-Fi uses an
explicit login. A network WTP connection alone does not provide that login.

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

To change the Pico's own network name, use
[Change the Pico hostname](#change-the-pico-hostname) below. This Pi's settings
form preserves that name during ordinary saves; it has no hostname editor.

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

### Management connection and login

Choose **Management connection** explicitly. Engineering HTTPS retains the
provisioned certificate policy. Consumer Wi-Fi and setup Wi-Fi require the
configured Pico's full device ID, reachable IPv4/local hostname and its saved
Wi-Fi passphrase. Setup Wi-Fi uses `192.168.4.1`; the Pi must already have
network reachability. Selection does not move the Pi between networks.

Login input clears after an attempt. Consumer traffic keys remain only in RAM,
with five-minute idle and fifteen-minute absolute expiry. Reauthenticate after
expiry and explicitly load saved state before another save. No persistent
management password is added to INI, device profiles or browser storage.
Consumer authentication uses a shared passphrase; it does not establish unique
device identity. Protect the Pi browser session and use a trusted endpoint.

Supported firmware permits three consumer sessions and one pending login;
older firmware may allow only one. Capacity, pending-login and pacing refusals
are distinct. Wait for a pending login or expiry, disconnect the owning client,
or use the panel's explicit occupied-login inspection/retirement workflow when
advertised. Read connection state after a lost reply. Pi tabs share the native
management session; retiring a login never retries a settings save. Unsupported
retirement requires that login's own logout or expiry.

Management remains subject to idle admission and confirmed output state.
A reachable WTP endpoint, public advertisement or built-in host capability
flag does not establish authenticated management support. There is no automatic
carrier, endpoint or mutation fallback after failure.

### Save progress on the Pico's own page

On consumer firmware, open the Pico's own page at
`http://<current-Pico-IP>/` or its current `.local` address. Sign in with the
password for the Wi-Fi network saved on that Pico. When its temporary setup
Wi-Fi is available, join it and open `http://192.168.4.1/radio`. Choose
**Station/Transmission** for station details, schedules, radio pins and message
controls; **Wi-Fi/Host** contains network, hostname and restart controls. Moving
between these two areas keeps edits in this tab. Engineering deployments use
their provisioned HTTPS credentials and authorized access instead.

The steps below apply when the page offers **Save valid station fields** or
**Save valid fields** together with a separate **Apply saved…** action. Older
firmware can require a complete configuration. WsprryPi's Fleet member editor
still uses its own [complete, atomic saves](#shared-pico-member-resources); it
does not acquire partial-save support from the Pico page.

#### Save a callsign without completing everything

1. Edit the callsign, locator or reported power that you want to keep. You can
   save a callsign alone, a locator alone or reported power alone. Leave the
   unrelated **Send a message** controls empty if you are not preparing QRSS,
   FSKCW or DFCW; **Load and arm message** is a separate action.
2. Choose **Save valid station fields**. Read the result beside each edited
   field. Valid independent fields can be saved even when another field is
   blank or invalid. An invalid entry stays visible and is labelled **Not
   saved**; correct it when ready, then make another explicit save.
3. Read the saved-progress summary. A saved callsign with a missing locator
   or reported power is incomplete progress, not an applied station or a
   transmitter ready to operate.

```{figure} pico_progress_partial.png
:alt: Pico station form showing callsign and zero dBm saved as draft while the invalid locator BAD remains unsaved
:width: 390px

Example: callsign and zero dBm were saved independently. The invalid locator
remains in the browser; the applied station has not changed.
```

**0 dBm is a valid reported power.** A blank power choice means missing power,
not zero. Choose the intended value explicitly; reported WSPR power is message
metadata, not measured RF power or output drive. Fields you do not edit retain
their previously saved values, so a station edit does not require re-entering
Wi-Fi credentials. If you clear a callsign or locator and save it, that field
is missing from saved progress; the previous applied value is not silently
substituted into the cleared draft.

Schedules are checked together as one complete set, and radio pins as one
complete allocation. An invalid schedule set or conflicting pin plan remains
unsaved as a unit while unrelated valid edits can be saved. In an engineering
network editor, the network name and password also form one unit. Consumer
**Save Wi-Fi network** and hostname controls retain their separate complete
setup/save workflows; use their own result and restart instructions.

#### Saved progress, applied settings and readiness

| State | What it means |
| --- | --- |
| Unsaved edit | Text or a selection in this tab; it has not been confirmed saved on the Pico. |
| Saved progress | Valid fields retained on the Pico, possibly incomplete. They survive page reload, a new login and a Pico restart. |
| Applied settings | A complete, validated station or configuration selected through an explicit Apply action. |
| Active settings | Settings used by this boot; saved network or pin changes can still require a restart. |
| Ready for an operation | Current access, clock, frequency/pin support, scheduling, ownership, STOP and fault state admit that particular operation. |

The WSPR plan in the saved-progress summary reports whether those saved station
values can be encoded. Hints beside edited fields may describe unsaved text.
Neither proves readiness, permission to transmit, measured power or successful
reception. An incomplete WSPR locator does not by itself impose a locator requirement on
QRSS, FSKCW, DFCW or a complete externally prepared job; those operations still
need their own valid settings and current admission.

**An already enabled schedule continues using the previously applied settings
while you save progress.** Saving a draft does not stop that schedule, replace
its station, resume STOP or clear a fault. Even saving an unchecked schedule
box is only progress until you explicitly apply it. Confirm the Pico's own
schedule state; disabling WsprryPi transmission alone does not disable Pico's
standalone schedule.

#### Apply the saved values deliberately

Complete and save the intended station fields, then check the **Saved station**
summary and its WSPR plan. Choose **Apply saved station** to apply those
*device-saved values*. Invalid or newer unsaved text still visible in a control
is not the value selected by Apply. Consumer pages keep Apply unavailable when
saved station progress is incomplete or cannot be encoded for local WSPR. The
Pico checks complete station values and current application access again when
you apply; an available button does not establish transmit readiness.

In **Schedules and radio pins**, use **Apply saved settings** after saving valid
progress. Applying an enabled schedule can allow future autonomous transmissions
when admitted; check the intended station, clock, frequency and RF path first.
An incomplete station draft can remain saved while valid radio settings apply
using the previous complete station. Changed network or pin settings can require
**Restart device** in **Wi-Fi/Host** before becoming active. In an engineering
network editor, choose **Save valid network fields**, then **Apply saved network
settings**, and follow any restart instructions. Restarting alone does not apply
a saved network draft. Restart and saving remain separate actions.

Consumer station application uses the existing setup transaction and may
reconnect or restart the Pico. Keep the tab open, follow its result instructions
and use **Check saved result** when offered. A received request or returning
page alone does not confirm application. Do not repeat Apply while its outcome
is unknown. Completing a draft, logging in, refreshing status or restarting the
Pico never applies that draft automatically.

#### Save station progress during setup

After Wi-Fi setup, the **Set your station details** page offers **Save valid
fields** on supporting firmware. It can retain a callsign without a locator or
reported power, without replacing the saved Wi-Fi network or creating a partial
applied station. Later complete and save the missing fields, then choose
**Apply saved station settings**. Read the setup result before trying again.

```{figure} pico_progress_incomplete.png
:alt: Pico setup showing a saved callsign, blank locator and unselected reported power, with Apply saved station settings unavailable
:width: 390px

Example: the callsign is saved on the Pico. Locator and reported power are
still missing, so application is unavailable.
```

#### Recover an uncertain save without losing edits

A conflict, timeout, expired login or interrupted reply can leave a save
unconfirmed even if the Pico stored some values. Keep this tab open. The page
preserves the edits and blocks another save; it does not automatically retry.

On the normal Pico page, sign in again if necessary, choose **Read saved
settings and keep draft**, compare the device's values with the retained edits,
then choose **I reviewed saved settings; enable a new save** when ready. On the
setup page, use **Read saved progress; keep edits** followed by **I reviewed
saved progress; enable a new save**. Readback shows what is stored now; matching
values alone do not identify which interrupted request committed.

Use **Reload saved settings** only when you intend to discard unsaved edits and
adopt device-saved progress. Copy any unsaved text before leaving or reloading
the page; only confirmed device-saved progress survives that loss of the tab.
Provisioning and full resets remove saved progress along with their documented
reset consequences.

### Change the Pico hostname

On supported consumer firmware, open and sign in to the
[Pico's own page](#save-progress-on-the-picos-own-page), then choose
**Wi-Fi/Host**. The hostname editor is on this Pico page, rather than
WsprryPi's Fleet settings form. Renaming a saved device profile in Fleet changes only
that profile's label.

Disable Pico's standalone schedule and resolve any pending, owned or active
job before changing the name. On a page with saved progress, save and apply the
schedule change, then verify the resulting schedule state; saving the unchecked
box alone does not disable it. Turning off WsprryPi transmission alone does
not disable Pico's own schedule. A hostname change does not require changing
the callsign, locator or message.

1. In **Device hostname**, enter the **Full local hostname**, such as
   `pico-a.local`. Use one label of 1–63 ASCII letters, digits or hyphens,
   followed by `.local`. Start and end the label with a letter or digit.
   Spaces, underscores, additional labels, IP addresses and URLs are refused.
   Letters are stored in lowercase; one final root dot is accepted and removed.
2. Choose **Save hostname**. Read **Active** and **Saved** separately:
   **Active** is the name used by the current boot; **Saved** is the name the
   next boot will use. Saving does not restart the Pico or immediately change
   its reachable address.
3. A changed name can end existing logins. Sign in again and choose **Refresh**
   to confirm the saved result. If the reply was lost, the save may already
   have succeeded. Compare the saved name before considering another save;
   when offered, choose **I reviewed the saved hostname; enable a new save**
   only after reviewing it.
4. Copy any unsaved drafts you need before leaving this tab. Choose
   **Restart device** once and confirm. The page checks the returning device;
   its countdown describes the next connection check, not a guaranteed
   restart time. A lost reply never causes an automatic second restart.
5. Use **Continue at pico-a.local (sign in again)**, with your chosen name,
   when ready to leave the old address. Sign in again and refresh. The page
   confirms success only after observing the same full Pico device ID, a new
   boot, and the intended name as both **Active** and **Saved**. A returning
   page or a finished countdown alone does not confirm the change.

```{figure} pico_hostname_saved.png
:alt: Pico Station control showing the old active hostname and pico-a.local saved pending restart
:width: 390px

Example: the saved name is waiting for a restart; the old active name still
belongs to the current boot.
```

**Cancel reconnect checks** stops this tab's checks. It does not undo the saved
name or cancel a restart already requested. Checks end after about 90 seconds
if the restart cannot be confirmed. Keep the tab open to retain its drafts,
or copy them before following the continuation link: drafts and login state
are not carried to the new address. See
[Hostname and restart troubleshooting](../../../Advanced_Operations/configuration_troubleshooting.md#pico-hostname-or-restart-is-unconfirmed)
for current-IP, setup-Wi-Fi, duplicate-name and certificate recovery.

```{figure} pico_hostname_reconnect.png
:alt: Pico restart countdown with Cancel reconnect checks and a link to continue at pico-a.local
:width: 390px

Example: the countdown offers cancellation and manual continuation while the
restart outcome is still unconfirmed.
```

To return to the stable hardware-derived name, choose **Use default hostname**,
confirm the choice, and then choose **Save hostname**. This first fills the
editor; the choice is not saved until you save it. Restart to apply a changed
name. Renaming preserves the Pico's device ID, setup Wi-Fi name, Wi-Fi password,
retained clients and unrelated settings.

The browser tab title begins with the confirmed active hostname, even when
opened by IP. It marks a pending rename or a last-confirmed observation;
typing an unsaved name does not change the title. Use these titles to help
distinguish multiple Pico tabs, and still check the intended device before
signing in or changing settings.

If setup has saved only a Wi-Fi network, complete station commissioning before
using hostname management. An engineering deployment with provisioned
certificates requires matching replacement credentials through its existing
provisioning workflow; its certified name is read-only here. Consumer renames
preserve the established certificate authority and retained client trust.
See [Updating Pi connection settings after a rename](../../../Advanced_Operations/ini_configuration/transmitter_backends.md#after-a-pico-hostname-change)
if WsprryPi also connects to this Pico.

### Shared Pico member resources

**Load member resources** reads application, station, saved/active hardware,
recurrence and supported pin choices as one reconciled observation. Confirm the
device, boot, carrier and observation time. Application/recurrence observations
are read-only here; prepared jobs and standalone schedules keep their own
authority and workflow.

1. Load the member resources explicitly while the host/member are idle.
2. For station changes, review callsign, locator and **Reported WSPR power (dBm)**
   together, then choose **Save member station**. This replaces the complete
   scoped station object. Loaded firmware determines supported station formats;
   see the automatic planning rules below. Consumer profile-owned station fields
   are read-only and must be changed through Pico transactional setup.
3. For hardware, select **Direct RF output**, optional **Active-low button**,
   and onboard, external or disabled indicator. Choices use Pico **GP** numbers,
   not Pi BCM/header numbers. Preserve the intended external indicator polarity.
   Button behavior also requires the member's button adapter to be enabled.
4. Choose **Validate candidate pins** and review conflicts and operational support.
   This preview never saves or activates pins. If the unchanged plan is supported,
   choose **Save member hardware** separately.
5. Read the result, then load resources again before any further save. Each save
   invalidates other editor contexts; unrelated drafts remain available for review.

### Pico automatic WSPR planning

These rules describe Pico's autonomous station defaults. Pi host **WSPR
Transmission Plan** preferences and prepared WTP jobs have their own planning
workflow; changing one does not select a Pico preference or re-encode a prepared
job.

With firmware advertising versioned Type 2/3 resources, Pico selects the plan
from the complete station tuple:

| Callsign and locator | Automatic Pico plan |
| --- | --- |
| Ordinary encodable call, four characters | Type 1 single |
| Ordinary call, six characters | Type 1 single, first four on air; all six retained |
| Supported compound, four characters | Type 2 single; that frame carries no locator |
| Supported compound, six characters | Type 2 followed by Type 3 |
| Explicit `<CALL>`, six characters | Type 3 single; brackets are excluded from the hash |
| Explicit `<CALL>`, four characters, or unsupported syntax | Refused by complete station saves or local-WSPR application |

Supported compound prefixes contain one to three alphanumeric characters before
an encodable base call; suffixes contain one alphanumeric or two decimal digits
after the base call. `W1A/AA0NT` is a supported prefix form even though `W1A`
is also a valid base call. `<W1A/AA0NT>` explicitly requests a single Type 3
frame. The complete station token is limited to 3–12 ASCII characters, including
brackets; malformed brackets, whitespace, multiple slashes and out-of-range
affixes are refused without truncation or substitution. Locators use A–R, two
digits and, when present, an A–X subsquare.

Two-digit suffixes `/00`–`/09` have an intrinsic Type 2 alternate spelling (for
example `/09` and `/Z`). Review the displayed ambiguity. A paired Type 3 hashes
the **requested full callsign**, not its alternate spelling. Type 3 carries a
hash rather than a full callsign; receiver context is needed to resolve it.
A valid plan or save does not prove receiver identification or RF decoding.

A two-frame plan starts its second frame 120 seconds after the first. Pico
reserves both slots before the first frame and holds one ownership lease across
the pair. Intersecting schedule occurrences are consumed conservatively. STOP,
reboot, changed configuration, lost clock/ownership or failure cannot resume a
stray second half or replay the first. There is no catch-up or automatic retry.
A failed output cutoff requires explicit recovery; saved or matching values
alone never establish inactive output.

Older firmware retains Type 1 station-write guidance and explicitly refuses
selected new formats. Unknown or malformed advertised support is refused with
no carrier or route fallback. An unchanged readable unsupported identity can
remain stored during unrelated settings saves; readability does not establish
that it can transmit. WsprryPi's member station/configuration saves remain
complete and atomic; that editor does not save incomplete drafts or accept valid
fields independently. The [Pico's own page](#save-progress-on-the-picos-own-page)
can separately retain valid fields as progress, without applying an incomplete
or unencodable WSPR station.

Reported WSPR dBm is message metadata, not measured power or RF drive. Fixed
I2C pairs are inspection-only. I2C RF, amplifier, LPF, drive, calibration and
waveform controls are unavailable in this editor. Missing resource support
leaves the compatible standalone editor available; malformed or unsupported
advertised resources are refused without silently substituting another save.

**Saved** hardware is the persisted plan; **Active** is the boot's observed
plan. Null active state means unknown, even if another pin-choice display has a
value. Changed pins require restart and latch output inhibition for the boot.
Saving the old pins again or changing station does not clear that latch. Storage
faults and hardware application faults are separate: `output_disable_failed`
may mean new settings were stored while shutdown was unconfirmed. Resolve the
fault and read back before another deliberate action.

An explicit scoped save does not restart Pico, reconnect WTP, enable recurrence,
claim ownership or transmit. A conflict, changed selection/context, timeout or
lost reply blocks further saves until explicit readback and review. Keep drafts,
compare fresh saved/active observations, validate hardware again and deliberately
save only after resolving the uncertainty. Do not automatically repeat a write.
