# Your first WSPR transmission

Use this walkthrough after [installing WsprryPi](Install/index.md) to configure
one local GPIO or Si5351 station through the web interface. Complete
[What you need](requirements.md), including the RF preparation, first. For a
Pico output, use [Add a WsprryPico](Install/pico.md); for direct shell operation,
use [Command-Line Quick Start](Command_Line_Operations/quick_start.md).

## Open the interface and keep transmission disabled

Open the web address printed by the installer, normally
`http://{name}.local/wsprrypi/`, using your Pi's hostname. If name resolution
fails, use its IP address. Connect from the Pi's directly connected network.

On **Operation**, keep transmission disabled while configuring. Review the
[transmission controls](User_Interface/Operations/index.md): disabling the
scheduler lets a current transmission finish, while **Stop transmission** halts
an ongoing transmission and disables future ones. Choose **Disable transmission
on (re)boot** for the initial setup so a restart does not request transmission.

Confirm the header indicator shows a backend connection. If it stays red, use
[Logs](User_Interface/Logs/index.md) and [configuration troubleshooting](Advanced_Operations/configuration_troubleshooting.md)
before proceeding.

## Select the transmitter

Open **Setup → Transmitter** and follow [Transmitter Configuration](User_Interface/Setup/Transmitter/index.md).

- For **GPIO**, select the intended RF pin and drive setting. On Pi 5, apply the
  route explicitly and confirm the requested and active route agree.
- For **Si5351**, select the intended I2C adapter, fitted address, reference
  frequency and source, and output drive. Discovery confirms register
  communication; it does not confirm RF readiness.

Check that the wiring and filter match the selected output. Review
[Pi I/O](User_Interface/Setup/Pi_IO/index.md) if using a transmit LED, amplifier
control, shutdown input, or band relays. Resolve pin conflicts before continuing.

## Enter the station and WSPR plan

Open **Setup → Signal Setup**, select **WSPR**, and use [Configure WSPR](User_Interface/Setup/Signal_Setup/wspr.md).

1. Enter the station callsign and Maidenhead locator. Begin with a standard
   callsign and four-character locator when appropriate; extended forms need
   the message planning described in that guide.
2. Enter one qualified band preset or USB dial frequency in **Frequencies**.
   For example, `20m` uses the effective preset for that band. Confirm the band
   is appropriate for the station, hardware, filter, and intended operation.
3. Set reported WSPR power to the value closest to measured station output.
   This field does not adjust transmitter drive.
4. Review frequency correction for the selected backend and confirm the Pi's
   UTC is synchronized. See [timing and calibration](Advanced_Operations/timing_calibration.md)
   when either needs attention.
5. Wait for valid changes to show **Saved**. Correct validation errors before
   leaving Setup. A saved configuration can still await runtime application.

WSPR frequency entries are USB dial frequencies. Their nominal RF center is
1,500 Hz above the dial, plus optional random placement. The Operation page
shows these separately. Fleet WSPR assignments use absolute RF centers instead;
follow their separate workflow when adding remote outputs.

## Start and observe

Use a suitable conducted test path to check the setup before connecting an
antenna. Complete any test-tone check and confirm its cleanup before starting
scheduled operation. [Maintenance → Test Tone](User_Interface/Maintenance/index.md#test-tone)
explains the test and its stop controls.

When the station and RF path are ready for the intended operation, return to
**Operation**, review the current plan and frequency, and enable transmission.
WSPR uses scheduled windows; enabling the scheduler does not imply immediate RF.
Watch the state and message progression, then use [Logs](User_Interface/Logs/index.md)
if the expected transmission does not start or completes with an error.

Open [Spots](User_Interface/Spots/index.md) to check reception reports for the
station callsign. Reports depend on reception and reporting services; an empty
spot list does not prove that the transmitter is inactive or faulty. UI status
and requested frequencies do not measure RF power, frequency accuracy, or emissions.

## Finish the trial

Disable transmission to prevent another scheduled transmission. If one is
already running and must end immediately, use **Stop transmission**. Confirm
the reported state is inactive and verify output-off through the test setup.
Keep the initial reboot policy disabled until ready to choose another policy.

For a configuration or startup problem, use [Configuration Troubleshooting](Advanced_Operations/configuration_troubleshooting.md).
For installation errors, use [FAQ and Known Errors](FAQ/index.md). If you need more help, follow [Support](Support/index.md) and its support-bundle workflow.
