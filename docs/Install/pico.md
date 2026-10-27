# Add a WsprryPico

A **Pico 2 W / RP2350** running WsprryPico can provide an external RF output
for WsprryPi. The Pi prepares and schedules complete jobs; the Pico executes
them locally. USB and network delivery do not set individual symbol timing.

This guide covers adding the Pico to an existing WsprryPi installation.
WsprryPi's Fleet controls, host schedules, CLI/INI settings and job recovery
are documented in this manual. The companion
[WsprryPico manual](https://wsprrypico.readthedocs.io/en/devel/) owns firmware
installation, the Pico's own browser controls, standalone operation and
device recovery. Use documentation matching the installed software; `devel`
describes development versions and does not imply a stable release.

## Prepare the hardware and firmware

Use a Pico 2 W, a USB data cable and a suitable filtered, loaded RF path.
Other Pico models are not supported WsprryPico targets. Normal firmware uses
direct GPIO output; the Pico's pins are **GP** numbers, separate from the Pi's
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
| USB | Connect the data cable to the Pi running WsprryPi. Fleet discovers the dedicated WTP and paired management interfaces. USB provides configuration, controller time and jobs without Wi-Fi. |
| Plain LAN | Complete the Pico's Wi-Fi setup, then use a reachable hostname/IP and its actual WTP port. Normal consumer firmware listens on TCP `31417` after station Wi-Fi and accepted network time. |
| Network (TLS) | Use an explicitly provisioned engineering deployment with the expected certificate identity and host-side CA, client certificate and key. There is no automatic downgrade. |

USB does not require standalone Wi-Fi commissioning. For network preparation,
follow [Connect to your Pico](https://wsprrypico.readthedocs.io/en/devel/connect.html).
Plain LAN WTP accepts reachable clients; the Pico browser's Wi-Fi password
does not protect that port. Use a trusted LAN. The browser HTTP address and
WTP TCP port are different services.

## Identify the Pico in Fleet

1. Keep Pi transmission disabled. Open **Setup → Fleet** and select the
   attached USB Pico or nearby network entry. Use **Add device** for a manual
   network profile when discovery is unavailable.
2. Follow [Known and nearby devices](../User_Interface/Setup/Transmitter/index.md#known-and-nearby-devices)
   to identify the intended board, compare its full stable device ID and save
   its connection profile. USB serial, device ID, boot ID and a profile's
   display name serve different purposes.
3. Choose how this Pi will use it:
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

Use [Pico standalone settings and Wi-Fi](../User_Interface/Setup/Transmitter/index.md#pico-standalone-settings-and-wi-fi) and [member resources](../User_Interface/Setup/Transmitter/index.md#shared-pico-member-resources) to read and manage the selected Pico from WsprryPi. Keep its autonomous schedule disabled while using host scheduling. Turning off Pi transmission or pausing an assignment does not disable the Pico's saved standalone schedule. The Pico’s standalone WSPR setting is a whole-Hz USB dial frequency; its four tones surround a center 1,500 Hz above it. Pi Fleet WSPR frequency entries are absolute RF centers. Standalone dial `3568600` and Fleet center `3570100 Hz` therefore describe the same nominal placement. Read the member’s **WSPR dial** in its recurrence summary; **not configured** means no standalone frequency is selected. Use the Pico’s own browser to select a standalone dial. Saving it affects future standalone jobs, leaves a first schedule disabled and preserves STOP.

Pico station defaults and Pi job parameters have separate authority; changing one does not rewrite an already prepared job.

Before enabling a Pi transmission or resuming a Fleet assignment:

- Confirm the intended full device ID, idle ownership and inactive output.
- Read saved and active Pico settings; resolve restart, STOP and fault states.
- Verify station, mode, frequency, filter/load and the target's reported limits.
- Confirm synchronized Pi UTC and acceptable Pico clock evidence. The selected
  single-output connection defaults to a 100 ms Pico uncertainty budget.
- Review the controller's
  [experimental frequency permissions](../Command_Line_Operations/transmitter_backends.md#experimental-frequency-policy).
  WTP combinations remain untested in host policy and require explicit
  unqualified-frequency permission. The Pico's separate policy must also allow
  the job. Consent does not expand physical limits or qualify RF output.

Pico RF correction uses its saved manual PPM; host GPIO clock calibration does
not calibrate it. See
[Pico time and frequency correction](https://wsprrypico.readthedocs.io/en/devel/reference/time.html).
Continuous **Test Tone** is unavailable through the Pico WTP backend.

## Recover or maintain the member

For busy, disconnected or uncertain jobs, use
[Pico status and recovery](../User_Interface/Setup/Transmitter/index.md#pico-status-and-recovery),
or the selected assignment's **Reconcile** control. Closing a connection or
restarting the Pi does not prove Pico RF has stopped. Confirm current state
before another job; unresolved output blocks further work.

Use [Fleet USB updates](../User_Interface/Setup/Transmitter/index.md#install-or-update-pico-firmware-over-usb)
for Pi-managed firmware work. If running the separate Pico installer on the
same Pi, follow its
[exclusive-USB-access procedure](https://wsprrypico.readthedocs.io/en/devel/wsprrypi.html#standalone-installer-on-a-wsprrypi-host)
first. For Pico browser setup, hostname changes, resets and private backup
handling, use [Maintain and recover](https://wsprrypico.readthedocs.io/en/devel/maintain.html)
in the Pico manual. After a rename, update the
[Pi connection profile and schedule destinations](../Advanced_Operations/ini_configuration/transmitter_backends.md#after-a-pico-hostname-change).

## USB diagnostic logs

After saving a USB Pico in Fleet, enable its log export under **USB logging on this Pico**, then enable that source's collection on **Logs**. See [Collect a Pico's USB logs](../User_Interface/Logs/index.md#collect-a-picos-usb-logs). This diagnostic path works without Pico Wi-Fi. Turn collection off before using Console in another terminal; firmware maintenance releases it automatically while the update is in progress.
