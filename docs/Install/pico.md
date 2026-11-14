# Add a WsprryPico

A **Pico 2 W / RP2350** running WsprryPico can provide an external RF output
for WsprryPi. The Pi prepares and schedules complete jobs; the Pico executes
them locally. USB and network delivery do not set individual symbol timing.

This guide covers adding the Pico to an existing WsprryPi installation.
WsprryPi's Fleet controls, host schedules, CLI/INI settings, and job recovery
are documented in this manual. The companion
[WsprryPico manual](https://wsprrypico.readthedocs.io/en/devel/) owns firmware
installation, the Pico's own browser controls, standalone operation, and
device recovery. Keep Pi and Pico software compatible and use documentation
that matches the installed software.

(start-with-standalone-operation)=
```{admonition} Start with standalone operation
:class: important

We strongly recommend using WsprryPico in standalone mode before adding it to
WsprryPi's Fleet. Use the Pico's own browser controls to learn its local
capabilities: station settings, time and frequency configuration, individual
messages, automatic schedules, and stop controls. This gives you a familiar
baseline before adding the Pi's connection, ownership, and scheduling controls.

Follow the [standalone setup sequence](https://wsprrypico.readthedocs.io/en/devel/)
and [first WSPR transmission walkthrough](https://wsprrypico.readthedocs.io/en/devel/operate.html#your-first-wspr-transmission),
including its RF preparation and end-of-trial shutdown steps. Before switching
to Fleet, disable the Pico's standalone schedules, save and apply the change,
and confirm inactive output and released control. See the
[handoff to WsprryPi](https://wsprrypico.readthedocs.io/en/devel/wsprrypi.html#ownership-and-schedules).

Standalone use is a learning recommendation, not a connection requirement.
USB Fleet control still works without configuring the Pico's Wi-Fi.
```

## Compatible software

Current WsprryPi development builds support the published **WsprryPico
1.0.0-rc.3** prerelease. Update WsprryPi and its supporting files before using
RC.3 member controls; an older Pi executable may use a different settings
contract. Beta 7 documents its earlier companion pair. Use the
[development installation instructions](beta7.md) for current Pi development
software and the [Pico release notes](https://wsprrypico.readthedocs.io/en/devel/reference/releases.html)
for RC.3 changes and limits. Firmware source is
`b4e966797cf016f6b8ed873dbe638522fc4d81c7`; later manual updates do not
identify a different firmware build.

RC.3 remains a prerelease. In Fleet, select **Specific version**, enter
`1.0.0-rc.3`, then choose **Download and check image**. **Stable release**
does not select RC.3. Review the version and source before installing.
Checking the image downloads and verifies it without programming the Pico.
A settings-contract mismatch is refused; selecting an older version or another
carrier does not bypass compatibility checks. See
[USB firmware updates](../User_Interface/Setup/Transmitter/index.md#install-or-update-pico-firmware-over-usb)
for preservation, confirmation, and recovery.

Software integration and image checks do not establish physical USB, installed
service behavior, timing, frequency accuracy, or RF qualification. Review the
Pico manual’s hardware and output limits for the actual configuration.

## Prepare the hardware and firmware

Use a Pico 2 W, a USB data cable, and a suitable filtered, loaded RF path.
Other Pico models are not supported WsprryPico targets. Normal firmware supports direct GPIO output and a qualified external Si5351 profile; the Pico's pins are **GP** numbers, separate from the Pi's
BCM numbers and physical header pins. Confirm the active Pico pin assignment
before wiring. Its reported WSPR dBm is message content, not measured power.
Check the Pico manual's
[wiring preparation](https://wsprrypico.readthedocs.io/en/devel/start.html) and
[output and band limits](https://wsprrypico.readthedocs.io/en/devel/reference/output.html).
Pi GPIO and Si5351 qualification tables do not qualify Pico output.

For a blank board, follow
[first firmware installation](https://wsprrypico.readthedocs.io/en/devel/install.html#first-installation)
in the Pico manual, then return here. Select the normal **WsprryPico** image;
**WsprryPico-Inhibited** simulates jobs without RF. The installer defaults to
**main**, independently of the Pi's branch; choose **devel** deliberately if
needed. Existing USB members can use
[Pico firmware over USB in Fleet](../User_Interface/Setup/Transmitter/index.md#install-or-update-pico-firmware-over-usb)
for settings-preserving updates.

## Choose a connection

| Connection | Preparation |
| --- | --- |
| USB | Connect the data cable to the Pi running WsprryPi. Fleet discovers the dedicated WTP and paired management interfaces. USB provides configuration, controller time, and jobs without Wi-Fi. |
| Plain LAN | Complete the Pico's Wi-Fi setup, then use a reachable hostname/IP and its actual WTP port. Normal consumer firmware listens on TCP `31417` after station Wi-Fi and accepted network time. |
| Network (TLS) | Use an explicitly provisioned engineering deployment with the expected certificate identity and host-side CA, client certificate, and key. There is no automatic downgrade. |

USB does not require standalone Wi-Fi commissioning. For network preparation,
follow [Connect to your Pico](https://wsprrypico.readthedocs.io/en/devel/connect.html).
Plain LAN WTP accepts reachable clients; the Pico browser's Wi-Fi password
does not protect that port. Use a trusted LAN. The browser HTTP address and
WTP TCP port are different services.

## Pico browser controls

The Pico's own browser page has **Station Control** and **Wi-Fi/Host** links in its header. Selecting a view returns to the page top and preserves the current tab's drafts. Station Control starts with transmitter status, then station identity, **WSPR Configuration**, **Radio pins**, and **CW Modes**. Saved-settings recovery and diagnostics are at the bottom. Wi-Fi/Host contains network, password, hostname, and **Logging** controls.

Status, accepted job/message details, schedules, frequencies, and redacted saved settings load without a Pico browser login. Locked fields are dimmed and cannot be edited; passwords, keys, and certificates are excluded. Use the hostname lock to authorize changes or job controls. **Save WSPR configuration** and **Apply WSPR configuration** affect WSPR schedule settings only. **Save radio pins** is independent, preserves WSPR drafts, and needs an explicit **Reset Pico** in Station Control's transmitter status to activate changed pins. Keep output inactive and confirm the physical wiring before a pin change.

These Pico controls are separate from WsprryPi's selected-member Fleet controls and the Pi's own schedules. For the complete workflow, use the [Pico configuration manual](https://wsprrypico.readthedocs.io/en/devel/configure.html). USB and UDP logging are under **Wi-Fi/Host → Logging**; see [Pico logging](../User_Interface/Logs/index.md#collect-a-picos-usb-logs). Reading a setting or selecting a log source does not take transmitter control.

## Identify the Pico in Fleet

1. Keep Pi transmission disabled. Open **Setup → Fleet** and select the
   attached USB Pico or nearby network entry. Use **Add device** for a manual
   network profile when discovery is unavailable.
2. Follow [Known and nearby devices](../User_Interface/Setup/Transmitter/index.md#known-and-nearby-devices)
   to identify the intended board, compare its full stable device ID, and save
   its connection profile. USB serial, device ID, boot ID, and a profile's
   display name serve different purposes.
3. Choose how this Pi uses it:
   - **Use this device** selects the Pi's single active WTP output. Disable
     host TX LED, amplifier, shutdown-button and band GPIO controls and CW
     fades, and set host PPM to zero before selecting it.
   - [**Assign a schedule**](../User_Interface/Setup/index.md#assign-an-output-schedule)
     creates an independent Fleet output schedule alongside other outputs.
     It does not replace the Pi's single selected output.

Saving or highlighting a profile does not select an output or start a job.
The [Fleet connection instructions](../User_Interface/Setup/Transmitter/index.md#add-a-pico-and-manage-outputs)
cover the complete selection workflow. For direct command-line use, configure
the [WTP INI settings](../Advanced_Operations/ini_configuration/transmitter_backends.md#pico-wtp)
and [Pico WTP backend options](../Command_Line_Operations/transmitter_backends.md#pico-wtp-backend).

## Review settings and start deliberately

Use [Pico standalone settings and Wi-Fi](../User_Interface/Setup/Transmitter/index.md#pico-standalone-settings-and-wi-fi)
and [member resources](../User_Interface/Setup/Transmitter/index.md#shared-pico-member-resources)
to read and manage the selected Pico from WsprryPi. Keep its autonomous
schedule disabled while using host scheduling. Turning off Pi transmission or
pausing an assignment does not disable the Pico's saved standalone schedule.
The Pico’s standalone WSPR frequency is a whole-Hz USB dial. Its four tones
surround a center 1,500 Hz above that dial, without random placement. Fleet
WSPR assignments instead take absolute RF centers: standalone dial `3568600`
and Fleet center `3570100 Hz` describe the same nominal placement. See the
[Pico manual](https://wsprrypico.readthedocs.io/en/devel/configure.html) for
standalone configuration.

Pico station defaults and Pi job parameters have separate authority; changing
one does not rewrite an already prepared job.

Before enabling a Pi transmission or resuming a Fleet assignment:

- Confirm the intended full device ID, idle ownership, and inactive output.
- Read saved and active Pico settings; resolve restart, STOP and fault states.
- Verify station, mode, frequency, filter/load and the target's reported limits.
- Confirm synchronized Pi UTC and a valid Pico time source. Read its reported UTC uncertainty; first-party submissions do not impose an additional uncertainty veto.
- Review the controller's
  [experimental frequency permissions](../Command_Line_Operations/transmitter_backends.md#experimental-frequency-policy).
  WTP combinations remain untested in host policy and require explicit
  unqualified-frequency permission. The Pico's separate policy must also allow
  the job. Consent does not expand physical limits or qualify RF output.

Pico RF correction uses its own manual PPM or supported, explicitly configured
GPS/PPS correction with residual trim. Direct GPIO and Si5351 corrections are
independent; host GPIO clock calibration does not calibrate the Pico. See
[Pico time and frequency correction](https://wsprrypico.readthedocs.io/en/devel/reference/time.html).
Continuous **Test Tone** is unavailable through the Pico WTP backend.

## Recover or maintain the member

For busy, disconnected, or uncertain jobs, use
[Pico status and recovery](../User_Interface/Setup/Transmitter/index.md#pico-status-and-recovery),
or the selected assignment's **Reconcile** control. Closing a connection or
restarting the Pi does not prove Pico RF has stopped. Confirm current state
before another job; unresolved output blocks further work.

Use [Fleet USB updates](../User_Interface/Setup/Transmitter/index.md#install-or-update-pico-firmware-over-usb)
for Pi-managed firmware work. If running the separate Pico installer on the
same Pi, follow its
[exclusive-USB-access procedure](https://wsprrypico.readthedocs.io/en/devel/wsprrypi.html#standalone-installer-on-a-wsprrypi-host)
first. For Pico browser setup, hostname changes, resets, and private backup
handling, use [Maintain and recover](https://wsprrypico.readthedocs.io/en/devel/maintain.html)
in the Pico manual. After a rename, update the
[Pi connection profile and schedule destinations](../Advanced_Operations/ini_configuration/transmitter_backends.md#after-a-pico-hostname-change).

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

The selected Pico's **Gray-line scheduling** controls read and save independent morning and evening windows and frequency overrides for its standalone schedule. The controls preserve edits during readback and require fresh saved-state review after an unconfirmed save or a change of Pico. Saving does not enable a schedule, transfer recurrence ownership, or change Pi-owned Fleet or native Pi scheduling.

Stop or relinquish a Pi-controlled schedule before using the Pico as a standalone beacon. Existing ownership and output checks still govern configuration changes. See the [Pico gray-line instructions](https://wsprrypico.readthedocs.io/en/devel/configure.html#gray-line-scheduling) for window boundaries, location requirements, precedence, paired-frame behavior, and propagation limits. Both applications must implement the current shared control descriptor to manage these settings over network or USB.
