# Maintenance Card

The maintenance page allows you to perform tasks that are not necessarily related to the business of transmitting WSPR or QRSS modes, but that you may need from time to time.

![Maintenance Page](maintenance.png)

## Repair Configuration

In rare cases, you may find that your configuration is present and readable but has missing sections or is otherwise not fully functional. If you hand-edit your INI, for example, and mistakenly delete sections or keys.

![Repair Configuration](repair.png)

When you press the "Repair current configuration" button, you will not be prompted before execution because it is considered a safe operation. A stock configuration file will be created, and your current configuration values will be applied on top. Missing or invalid data will be restored from the stock configuration.

![Configuration Repaired](repaired.png)

After this action, you should review all your settings to ensure they are still correct.

## Reset to Stock

This process is helpful if your INI file is damaged on disk or completely missing.

![Reset Configuration](reset.png)

Unlike the Repair Configuration button, it does not preserve existing user values. It copies a new stock `wsprrypi.ini` file in place of your current one if it exists, and reloads the configuration shipped with the application.

When you press the "Reset to defaults" button, you will be presented with a confirmation modal because this will destroy your existing configuration.

![Reset Confirmation](confirmation.png)

Confirm the action, and the process will complete and return the status.

![Reset Complete](reset_complete.png)

You will need to reconfigure all of your preferences before continuing to transmit.

## Privileged Network Safety

**Privileged network safety** limits configuration changes, device controls, support-bundle operations, and the browser WebSocket connection to clients on the Raspberry Pi's directly connected Ethernet or Wi-Fi networks. It is network-location access control, not authentication: it does not distinguish between users already on an allowed LAN and does not encrypt traffic.

The Maintenance page reports three values separately:

- **Requested** is the unsaved choice currently selected in the browser.
- **Configured** is the value stored in `wsprrypi.ini`.
- **Active** is the policy confirmed in the backend and Apache.

Keep **Enforced** selected for normal operation. Browser operation uses the normal port-80 Apache site; the UI does not fall back to the direct backend ports for this control. When enforcement is active, Apache also restricts the entire browser-facing WebSocket endpoint. Off-LAN clients therefore cannot use read-only WebSocket commands or receive its broadcasts.

The insecure override is intended only for deliberate administrator recovery or an explicitly accepted network design. Select **Insecure disabled**, type `DISABLE LOCAL-LAN SAFETY` exactly, and then select **Apply requested state**. The setting is not part of Setup autosave. When the insecure override is active, the page displays **NETWORK SAFETY OFF**.

Applying either value validates the candidate WsprryPi and Apache configuration, reloads Apache without rebooting, and confirms the active policy. If validation, reload, or confirmation fails, the page preserves your requested choice and reports that the requested, configured, and active values may differ. Resolve the reported problem and verify the displayed state before trying again.

Disabling this LAN check does not disable Host, Origin, CORS, malformed-request, HTTP method, command, forwarded-header, or ordinary configuration validation. See [Privileged Network Safety](network_safety.md) for protected operations, direct-backend behavior, network-change handling, and recovery guidance.

## Test Tone

A test tone is useful for checking the transmit path, calibration, and tuning. Connect the transmitter to a suitable dummy load or attenuated test path before starting. Keep the test brief, and select **End** as soon as the check is complete.

[![Test Tone accepted while awaiting controller runtime confirmation](test_tone.png)](test_tone.png)

This retained current-UI fixture shows acceptance before runtime confirmation. It uses synthetic responses and demonstrates feedback, not a live transmitter or measured RF state. Open the image for full resolution.

Select **Test tone** to open the manual tone controls. This does not change the frequency saved in Setup.

### Choose the frequency source

Choose one of these frequency sources:

- **WSPR band** uses the effective USB dial preset, profile and saved per-band preference supplied by the connected controller. The preview adds the fixed 1,500 Hz placement to obtain the RF center / steady carrier target. The standard `20m` choice targets `14,097,100 Hz`, matching CLI `--test-tone 20m`.

- **Custom RF frequency** accepts a whole-number carrier target in Hz. Entering `14095600` targets exactly `14,095,600 Hz`, matching numeric CLI `--test-tone 14095600`. No WSPR placement is added.

Neither source applies random placement. A preview is an unsaved selection; the result confirms the accepted synthesis target and runtime state separately. It does not measure output frequency. When the accepted target matches the preview, the result need not repeat the calculation.

![Test Tone frequency-source controls with Custom RF frequency selected](test_tone_frequency_source.jpg)

The example above shows the safe disconnected state: the frequency source and exact RF preview remain visible, while **Start** and **End** are unavailable.

Test Tone targets the RF carrier shown in the preview. On the legacy GPIO backend, a frequency that crosses a hardware clock-divider boundary is rejected rather than replaced with a nearby carrier. Choose another valid frequency if this happens. The reported frequency is the controller's synthesis target; actual RF accuracy still depends on clock calibration and the measurement path. See [Transmission Timing and Calibration](../../Advanced_Operations/timing_calibration.md#interpreting-test-tone-measurements) when using a tone to measure frequency error.

The WSPR band list is controller-authorized rather than a fixed list in the browser. **Start** remains unavailable until the controller is connected, its catalog is available, a valid frequency source is selected, and normal transmission interlocks permit a test tone. A disabled button is visually muted and cannot be selected.

See [Canonical Bands and WSPR Frequency Presets](../../Advanced_Operations/canonical_bands.md) for the effective preset rules and the distinction between a WSPR dial preset and the exact RF carrier used by **Custom RF frequency**.

If scheduled WSPR or CW-family transmission is enabled, the page prompts you to stop and disable it before starting a test tone.

![Disable Transmissions](disable_transmissions.png)

You must re-enable normal transmissions on the Operations page after testing.

### Read the result

Before **Start**, the frequency summary is a preview of the request. After the controller replies, the execution status reports what the controller actually committed. When the committed frequency matches the preview, the status does not repeat the full dial-frequency, offset, and RF-frequency calculation.

The execution status calls out information that changes what you should do, including:

- a committed frequency that differs from the request;
- controller selector details or warnings;
- a rejected or failed start; and
- whether **End** remains available for recovery.

**Accepted** means asynchronous startup was requested. **Active** means the controller observed runtime activity; it is not an RF measurement. Startup or execution can fail after acceptance. Read the failure and cleanup status before another Start; failed startup does not automatically resume prior work.

**End** feedback names cleanup and restoration separately. A successful Test Tone end can restore scheduler configuration, return to managed idle, or restore an earlier CLI direct tone. Ending this transaction therefore does not always mean all output is off. If restoration fails, the status retains that failure even when Test Tone cleanup succeeded. An ordinary **Stop** disables work and prevents later tone restoration from restarting it.

Saved Setup edits and **Repair current configuration** / **Reset to defaults** can be stored while the tone owns runtime, but application is deferred until cleanup. They do not replace the running backend, mode, frequency or selectors. Review the resulting configuration and restoration feedback before re-enabling normal transmission.

### Recover from an uncertain result

If Start or End times out, or connection drops before a confirmed result, the outcome is uncertain. Reconnect and read current status; a lost connection does not establish output-off. While connected, **End** remains available whenever active or uncertain state requires recovery, even without the WSPR catalog. During a pending End it stays disabled to prevent duplicate requests.

Request End once and inspect its result before another Start. Cleanup uncertainty inhibits further output. A recovery End can confirm cleanup without restoring prior work; a repeated inactive End need not report a new stop. If uncertainty persists, keep transmission disabled and use the reported local/backend recovery procedure. Conservative feedback from an older controller may lack correlation or restoration evidence; do not infer a fresh success from an unattributed reply.

## Update Checker

The WsprryPi UI automatically checks the running build against eligible releases and its trusted upstream branch on GitHub. A newer tagged release is shown as an **Update available**. A non-main development build may instead show **Newer branch build available** when its upstream branch contains the running commit and has newer commits.

Tagged-release notifications provide a link to the [Releases page](https://github.com/WsprryPi/WsprryPi/releases/). Branch-build notifications identify the target branch and commit and direct prerelease users to their designated update channel; they do not present an unrelated Releases link.

![Update Available Modal](update_avail.png)

You may also check manually on the Maintenance page, and force an immediate check.

![Force Update Check](manual_update_check.png)

You may dismiss the modal, and the footer will continue to quietly show the release or branch-build notification.

![Update Available Footer](update_footer.png)

You may also choose to "Never check again" either in the modal, or by selecting "About" in the footer.

![About - Never Check](about_update.png)

If you choose to never check again and wish to re-enable the checking, the opposite setting is available in the "About" footer, as well as in the update check section in the maintenance panel.

Technical information on the update check process is available in the [WsprryPi Automatic Update Polling](update_check.md) technical page.

## Support Bundle

Use **Support Bundle** when the WsprryPi maintainer asks for diagnostic information. The workflow records useful support context, creates a readable `.tar.gz` candidate locally, lets you inspect it, encrypts the exact bytes you approve, and hands only the encrypted `.age` file to a private Dropbox File Request.

Review the readable archive before encryption. See [Create and Share a Support Bundle](support_bundle.md) for privacy guidance, collection inventory, encrypted upload, receipt handling, truthful upload states, GitHub correlation, and cleanup.

```{toctree}
:maxdepth: 1
:hidden:

Create and Share a Support Bundle <support_bundle>
Privileged Network Safety <network_safety>
```
