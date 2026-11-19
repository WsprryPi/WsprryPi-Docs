# Add a WsprryPico

A **Pico 2 W / RP2350** running WsprryPico schedules and executes its own
transmissions. WsprryPi manages the Pico’s settings and native schedules through
USB or supported network management. The Pi does not dispatch occurrences.

(start-with-standalone-operation)=
## Start with standalone operation

Use the Pico’s own browser to learn station settings, time readiness, native
WSPR and keyed-message schedules, and stop controls. Follow the
[WsprryPico manual](https://wsprrypico.readthedocs.io/en/devel/) for hardware,
RF filtering, supported bands and modes, firmware installation, and local recovery.
Management does not require the Pico’s Wi-Fi when it is attached by USB.

## Compatible software

Use matching Pi and Pico management contracts. A device that lacks the required
native schedule or management capability must remain on compatible software or
receive a separately planned update. Before replacing WTP-capable software,
complete [migration and cleanup](../User_Interface/Maintenance/index.md#scheduling-ownership)
for every legacy controller and transmitter. Keep usable recovery binaries and
configuration backups until their duties are resolved.

## Prepare the hardware and firmware

Follow the Pico manual’s installation and hardware checks before enabling a
schedule. Compilation or a successful management read does not qualify the RF
output, filter, antenna path, or frequency accuracy. Firmware installation and
physical checks are separate operator actions.

## Choose a connection

- **USB**: attach the Pico to the Pi running WsprryPi. Management and time use
  interface 4; Console remains on 0 and Logging on 6. Interfaces 2/3 are reserved
  and inert in application firmware. RFBench uses that allocation only for its
  independent bench commands.
- **Consumer Wi-Fi (encrypted)**: use the Pico’s reachable hostname or address,
  its full device ID, and its password. Management uses HTTP port 80 with the
  existing encrypted Consumer-Radio channel.
- **Engineering HTTPS**: use explicitly provisioned certificates, server
  identity, and management port. Certificate and hostname verification remain
  mandatory. There is no WTP port, WTP ALPN, or automatic carrier fallback.

## Pico browser controls

The Pico’s own browser configures its native schedules and provides native stop.
Closing it does not cancel an accepted occurrence. Continued execution still
requires qualified time under the device’s existing clock policy.

(identify-the-pico-in-fleet)=
## Add the Pico in Fleet

### Attached USB Pico

Open **Setup → Fleet**, select the attached Pico, read its identity, and compare
the full device ID and USB serial. Save the named profile. Direct management
discovery does not require a WTP sibling interface.

### Nearby network Pico

Discovery supplies connection hints, not authentication. Duplicate names can
represent different devices. Verify the full ID through a trusted local or USB
observation before saving a Consumer Wi-Fi profile. Engineering HTTPS additionally
checks its configured certificate identity.

### Manual network profile

Enter the explicit management destination, connection type, and full expected
device ID. Keep custom hostnames, ports, and certificate references when editing
an existing profile. A display name or profile handle is not device identity.

### Choose how the Pi uses the saved profile

Choose the saved Pico under **Setup → Device**, connect using its management
carrier, and read current settings. Saving or selecting a profile never changes
this Pi’s RF backend, claims output, or enables a schedule.

## Review settings and start deliberately

Read the exact device and boot, edit its native schedule, save it disabled, and
read it back. Resolve unsupported mappings explicitly; do not seed a replacement
from controller defaults. Enable the reviewed schedule deliberately after checking
its time, frequency, hardware, and authority readiness. WSPR dial frequencies
remain dial frequencies; keyed-message base and shift retain their documented
units. No Fleet RF-center conversion is applied.

## Recover or maintain the member

Use **Read device status** for a current observation. **Stop native schedules**
disables saved WSPR and keyed-message schedules and confirms inactive, unowned
output when successful. An unknown or refused result requires **Read stop status**;
do not repeat an unconfirmed mutation. If the Pico cannot be reached, use its
local USB Console recovery. Console STOP remains a separate local control.

Settings drafts survive connection changes in the open browser. Reconnect and
read before reviewing an unknown save; do not infer success from a lost ACK,
restart, or disconnect. Firmware maintenance uses the independent
[Pico installer](https://wsprrypico.readthedocs.io/en/devel/install.html).
Resolve active work and legacy duties first, confirm the exact device, and
release conflicting Console or management users as the installer directs.
The former selected-output firmware panel is unavailable.

## UDP diagnostic logging

A Pico can send diagnostic events directly over station Wi-Fi, or its attached Pi can forward already collected USB logs. These controls are independent of Fleet radio ownership and schedules. Use **UDP logging on this Pico** for the selected member's sender and **Logs → Logging on this Pi** for the local Pi's sender, USB forwarding, and network collector. Verify the displayed device/boot and management carrier before saving. See [Logs](../User_Interface/Logs/index.md#receive-udp-logs-on-this-pi) for the collector and forwarding procedure and the [Pico UDP guide](https://wsprrypico.readthedocs.io/en/devel/udp.html) for direct export.

UDP settings use independent saved state and remain disabled initially. Ordinary firmware updates preserve them. Retain the exact installer bundle for later updates from another computer. Disable export and read it back before rollback; the shared installer refuses an image that reaches the UDP settings reservation. Do not erase a board to bypass that refusal. USB control and USB logging keep their separate settings and interfaces.

Install compatible Pi worker, API, and UI assets together before updating Pico firmware. Leave all UDP policies disabled until the intended sender and collector are configured and read back. Incompatible peers show unavailable; they do not use a different management resource or collect Console output. A logging check needs no radio job: use a finite test event, or USB startup/management-connection events, and verify the destination journal and Logs view independently of the sender's submission count.

## Amplifier lead and tail

In the selected Pico's member hardware area, next to the pin settings, use **Read saved timing** before editing **Enable before RF (ms)** and **Disable after RF (ms)**. Each defaults to **200 ms** and accepts **0–1000 whole milliseconds**. Save while the Pico is idle and unowned, then explicitly restart the Pico to activate the change. Readback distinguishes saved values from those active for the current boot. A disabled amplifier-enable pin uses neither interval.

Lead gives the amplifier time to settle before the scheduled RF start. Tail holds it enabled after normal RF completion. These intervals surround the timed transmission and do not change the encoded message duration. Zero removes the corresponding interval. Jobs submitted too late for lead are refused; stop and fault cleanup bypass tail. Timing readback reports the last observed phase and does not measure amplifier readiness or RF power. Configure the amplifier-enable GPIO and pin polarity in the selected Pico’s member hardware controls or on its own **Radio pins** page. Both editors preserve timing and drive settings; changed hardware requires an explicit Pico restart. These controls require supporting Pico firmware and leave native Raspberry Pi amplifier settings independent.

## LPF and band selector

In Fleet, open the selected Pico's member hardware controls and **LPF / band selector**, then choose **Read saved selectors**. Name each output, choose an unused Pico **GP** number and polarity, and add its usable frequency ranges in whole Hz. Several ranges may share one selector; ranges on different selectors cannot overlap. Up to five selectors and ten ranges are supported. Local Pi Band GPIO settings remain separate.

**Fixed / manual filtering** leaves selector outputs inactive. **Require a declared filter for every job** refuses a job unless one selector covers every nominal and programmed RF frequency, including modulation and correction. Declare usable coverage around the actual RF frequencies, rather than just the WSPR dial. An empty required mapping refuses jobs.

**Release before selection (ms)** and **Settle after selection (ms)** each default to 20 ms and accept 0–250 whole milliseconds. The selected filter settles before amplifier enable and stays selected through keyed gaps and amplifier tail. It releases after amplifier disable. These intervals are independent of amplifier lead and tail; a job submitted too late for preparation is refused.

Save while the Pico is idle and unowned, explicitly restart it, then read back saved and active settings. Every selector change requires restart. Reads and errors retain entries; after an uncertain save, read and review before another deliberate save. No configuration save tests GPIO or transmits. Unsupported firmware shows the controls as unavailable. The same settings are available on the Pico's own Radio pins page; see [Configure the Pico selector](https://wsprrypico.readthedocs.io/en/devel/configure.html#lpf-and-band-selector).

Use suitable 3.3 V logic drivers and external bias that keeps the bank inactive during reset and loss of Pico power. Never connect relay coils directly to GPIO. Declared ranges and GPIO readback do not measure filter response, relay position, power handling, or emissions.

## Si5351 RF output

In the selected Pico's member hardware controls, choose **Load member resources**, then select **Si5351** as the **RF output engine**. These are Pico settings, separate from WsprryPi's local Si5351 backend. Choose a complete I²C SDA/SCL pair, the fitted reference frequency and source, and the transmit clock. Passive crystals also require their specified load. External clock/TCXO uses the supported XA arrangement rather than CLKIN.

Loopback can be **None**, **CLK0**, **CLK1**, or **CLK2**, with a distinct transmit clock and an eligible counter input. None releases the capture input and dependent trusted use. **Measure only** reports a clock ratio and uncertainty. **Trust local reference for Pico rate** requires a declared reference uncertainty. Hardware selection, that allowance, and hardware qualification are operator responsibilities; shared bench results do not certify an operator’s hardware. After NTP or phone time is accepted, it can reduce Pico timer drift while preserving that time source's age, uncertainty, and expiry. It supplies no UTC epoch or automatic RF calibration. Manual Si5351 correction is in ppb and remains separate from direct GPIO correction. Output drive is electrical current, independent of reported WSPR power.

Choose **Validate candidate pins**, then **Save RF output settings**. The complete engine and reference allocation saves together. Draft edits do not program hardware. Restart the Pico explicitly to activate the accepted allocation; changing it back does not clear the restart requirement. Selecting Direct GPIO restores its controls and retains inactive Si5351 settings.

Ordinary firmware supports the documented **QRP Labs Rev. 6 module with a 25 MHz external-XA TCXO**, **SDA GP4 / SCL GP5**, **CLK0 at 8 mA**, and no independent RF-gate assignment. Loopback is **None** or **CLK2 → GP7**, using the normal **138 MHz** Pico clock. Other configurations require an explicit engineering Pico build. The same normal image also supports Direct GPIO. Register readback does not prove RF inactivity or accuracy. Engineering tests require verified I²C pull-ups and bus timing, a conducted RF path, and shutdown/reset checks. Automatic Si5351 correction remains experimental. GPS/PPS input and automatic correction require supported wiring, saved settings, and qualified UTC/PPS association; see [Pico GPS/PPS setup](https://wsprrypico.readthedocs.io/en/devel/configure.html#gps-and-pps). See [Si5351 settings in the Pico manual](https://wsprrypico.readthedocs.io/en/devel/configure.html#si5351-output-settings) for supported module settings and measurement limits.

## Pico standalone gray-line scheduling

The selected Pico's **Gray-line scheduling** controls read and save independent morning and evening windows and frequency overrides for its standalone schedule. The controls preserve edits during readback and require fresh saved-state review after an unconfirmed save or a change of Pico. Saving does not enable a schedule, transfer recurrence ownership, or change another device’s native scheduling.

Stop or relinquish a Pi-controlled schedule before using the Pico as a standalone beacon. Existing ownership and output checks still govern configuration changes. See the [Pico gray-line instructions](https://wsprrypico.readthedocs.io/en/devel/configure.html#gray-line-scheduling) for window boundaries, location requirements, precedence, paired-frame behavior, and propagation limits. Both applications must implement the current shared control descriptor to manage these settings over network or USB.
