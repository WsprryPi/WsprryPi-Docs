# Maintenance Card

On a transmitter installation, use the Maintenance page to repair or reset configuration, check the RF path with Test Tone, check for updates, create a support bundle, and download or restore an encrypted installation backup.

On a [controller-only installation](../../Install/controller.md), Maintenance provides encrypted backup and restore, controller access, and scheduling ownership review for supported paired Pis. Local transmitter setup, repair, reset, Test Tone, privileged network settings, and Pi support bundles are unavailable on the controller.

## Set up this transmitter

On a new installation, open **Maintenance** and use **Set up this transmitter**. Review the **Station** and **Operation** sections, including your call sign, locator, and output selection. Other settings are available in the expandable sections. Select **Save initial settings** when the configuration is ready.

Reviewing or editing the form does not save it. If validation fails, the form retains your entries. If the connection is interrupted during a save, use **Check saved result** before attempting another change.

Setup saves transmission and scheduling disabled. It does not start a tone, transmit a message, or enable a schedule. After the saved configuration and startup are verified, the ordinary Maintenance controls become available.

Updates and configuration resets retain the installation's scheduling history. If established history is missing or damaged, the page opens read-only recovery; it cannot use initial setup or Reset to bypass that condition. Review and enable the saved schedule under [Setup → Scheduling](../Setup/Scheduling/index.md).

## Controller access

Use **Controller access** to pair a controller-only installation or a transmitter Pi with the Pi it will manage. Keep the target Pi’s **Privileged network safety** policy enforced. The controller-only host applies its installer-managed browser access policy.

1. On the Pi you want to manage, open **Maintenance** and select **Pair this Pi**. Keep that page open to view its temporary code.
2. On the controller’s **Maintenance** page, find **Manage another Pi**. Select **Refresh devices**, choose the Pi displaying the code, enter its eight characters, and select **Connect to Pi**.
3. Wait for confirmation. Open **Setup** and choose the paired Pi under **Device**. Supported Picos attached to it by USB also become available through that connection automatically.

The code expires after two minutes and appears only in the page that opened the pairing window. If it expires or that page closes, return to that Pi’s Maintenance page and open pairing again to generate a new code. Security is configured automatically on the devices. Pairing does not change output selection, Transmit permission, schedules, or running work.

To change who manages a Pi, open that Pi’s own Maintenance page and select **Replace controller**. Pair from the new controller using the new temporary code. The old controller can be offline; its ordinary management access is revoked when replacement completes. **Remove controller…** offers an explicit confirmation to remove management access. Running work and saved schedules continue. **Pair again** is offered when access recovery is required.

If a controller-access change is unconfirmed, use **Check saved result**. Refreshing status or checking the result does not repeat the change. Keep an unknown result pending and follow its recovery feedback before another action.

## Repair Configuration

![Maintenance configuration repair and reset controls](recovery.jpg)

Use **Repair current configuration** to repair supported saved settings through the backend. It retains valid values and fills missing or invalid values from current defaults. Review all settings afterward. Repair does not replace a database file, erase established authority/history, or bypass a storage or recovery hold.

## Reset to Stock

**Reset to defaults** asks for confirmation before replacing supported local configuration values with defaults through the owning backend. Reconfigure station and hardware preferences before transmitting. Reset retains established scheduling and ownership history; it cannot repair a missing or corrupt established database or clear output uncertainty.

## Backup and restore

Use **Backup and restore** to create and download a passphrase-encrypted backup, or upload and validate one for recovery or a computer move. Restore requires explicit preview confirmation and destination review before releasing persistent output/authority holds. See [Back Up or Restore an Installation](backup_restore.md) for the full workflow and [local maintenance commands](../../Command_Line_Operations/saved_settings.md#backup-and-restore-from-a-local-terminal) if browser access is unavailable.

## Privileged Network Safety

**Privileged network safety** limits configuration changes, device controls, support-bundle operations, and the browser WebSocket connection to clients on the Raspberry Pi's directly connected Ethernet or Wi-Fi networks. It is network-location access control, not authentication: it does not distinguish between users already on an allowed LAN and does not encrypt traffic.

The Maintenance page reports three values separately:

- **Requested** is the unsaved choice currently selected in the browser.
- **Configured** is the saved backend-owned policy.
- **Active** is the policy confirmed in the backend and Apache.

Keep **Enforced** selected for normal operation. Browser operation uses the normal port-80 Apache site; the UI does not fall back to the direct backend ports for this control. When enforcement is active, Apache also restricts the entire browser-facing WebSocket endpoint. Off-LAN clients therefore cannot use read-only WebSocket commands or receive its broadcasts.

The insecure override is intended only for deliberate administrator recovery or an explicitly accepted network design. Select **Insecure disabled**, type `DISABLE LOCAL-LAN SAFETY` exactly, and then select **Apply requested state**. The setting is not part of Setup autosave. When the insecure override is active, the page displays **NETWORK SAFETY OFF**.

Applying either value validates the candidate WsprryPi and Apache configuration, reloads Apache without rebooting, and confirms the active policy. If validation, reload, or confirmation fails, the page preserves your requested choice and reports that the requested, configured, and active values may differ. Resolve the reported problem and verify the displayed state before trying again.

Disabling this LAN check does not disable Host, Origin, CORS, malformed-request, HTTP method, command, forwarded-header, or ordinary configuration validation. See [Privileged Network Safety](network_safety.md) for protected operations, direct-backend behavior, network-change handling, and recovery guidance.

## Test Tone

A test tone is useful for checking the transmit path, calibration, and tuning. Connect the transmitter to a suitable dummy load or attenuated test path before starting. Keep the test brief, and select **End** as soon as the check is complete.

An accepted Test Tone request can still be waiting for runtime confirmation. Read the execution status before treating the tone as active. Status feedback is not a measurement of RF output.

Select **Test tone** to open the manual tone controls. This does not change the frequency saved in Setup.

### Choose the frequency source

Choose one of these frequency sources:

- **WSPR band** uses the effective USB dial preset, profile, and saved per-band preference supplied by the connected controller. The preview adds the fixed 1,500 Hz placement to obtain the RF center / steady carrier target. The standard `20m` choice targets `14,097,100 Hz`, matching CLI `--test-tone 20m`.

- **Custom RF frequency** accepts a whole-number carrier target in Hz. Entering `14095600` targets exactly `14,095,600 Hz`, matching numeric CLI `--test-tone 14095600`. No WSPR placement is added.

Neither source applies random placement. A preview is an unsaved selection; the result confirms the accepted synthesis target and runtime state separately. It does not measure output frequency. When the accepted target matches the preview, the result need not repeat the calculation.

When the controller is disconnected, **Start** and **End** are unavailable.

Test Tone targets the RF carrier shown in the preview. On the legacy GPIO backend, a frequency that crosses a hardware clock-divider boundary is rejected rather than replaced with a nearby carrier. Choose another valid frequency if this happens. The reported frequency is the controller's synthesis target; actual RF accuracy still depends on clock calibration and the measurement path. See [Transmission Timing and Calibration](../../Advanced_Operations/timing_calibration.md#interpreting-test-tone-measurements) when using a tone to measure frequency error.

The WSPR band list is controller-authorized rather than a fixed list in the browser. **Start** remains unavailable until the controller is connected, its catalog is available, a valid frequency source is selected, and normal transmission interlocks permit a test tone. A disabled button is visually muted and cannot be selected.

See [Canonical Bands and WSPR Frequency Presets](../../Advanced_Operations/canonical_bands.md) for the effective preset rules and the distinction between a WSPR dial preset and the exact RF carrier used by **Custom RF frequency**.

If scheduled WSPR or CW-family transmission is enabled, the page prompts you to stop and disable it before starting a test tone.

You must re-enable normal transmissions on the Operations page after testing.

### Read the result

Before **Start**, the frequency summary is a preview of the request. After the controller replies, the execution status reports what the controller actually committed. When the committed frequency matches the preview, the status does not repeat the full dial-frequency, offset, and RF-frequency calculation.

The execution status calls out information that changes what you should do, including:

- a committed frequency that differs from the request;
- controller selector details or warnings;
- a rejected or failed start; and
- whether **End** remains available for recovery.

**Accepted** means asynchronous startup was requested. **Active** means the controller observed runtime activity; it is not an RF measurement. Startup or execution can fail after acceptance. Read the failure and cleanup status before another Start; failed startup does not automatically resume prior work.

**End** feedback names cleanup and restoration separately. A disabled or held schedule remains disabled when Test Tone ends. Review the cleanup and restoration result before enabling normal transmission.

Tone end can restore scheduler configuration, return to managed idle, or restore an earlier CLI direct tone. Ending this transaction therefore does not always mean all output is off. If restoration fails, the status retains that failure even when Test Tone cleanup succeeded. An ordinary **Stop** disables work and prevents later tone restoration from restarting it.

Saved Setup edits and **Repair current configuration** / **Reset to defaults** can be stored while the tone owns runtime, but application is deferred until cleanup. They do not replace the running backend, mode, frequency, or selectors. Review the resulting configuration and restoration feedback before re-enabling normal transmission.

### Recover from an uncertain result

If Start or End times out, or connection drops before a confirmed result, the outcome is uncertain. Reconnect and read current status; a lost connection does not establish output-off. While connected, **End** remains available whenever an active or uncertain state requires recovery, even without the WSPR catalog. During a pending End, it stays disabled to prevent duplicate requests.

Request End once and inspect its result before another Start. Cleanup uncertainty inhibits further output. A recovery End can confirm cleanup without restoring prior work; a repeated inactive End need not report a new stop. If uncertainty persists, keep transmission disabled and use the reported local/backend recovery procedure. Conservative feedback from an older controller may lack correlation or restoration evidence; do not infer a fresh success from an unattributed reply.

## Update Checker

The WsprryPi UI automatically checks the running build against eligible releases and its trusted upstream branch on GitHub. A newer tagged release is shown as an **Update available**. A non-main development build may instead show **Newer branch build available** when its upstream branch contains the running commit and has newer commits.

Tagged-release notifications provide a link to the [Releases page](https://github.com/WsprryPi/WsprryPi/releases/). Branch-build notifications identify the target branch and commit and direct prerelease users to their designated update channel; they do not present an unrelated Releases link.

You may also check manually on the Maintenance page and force an immediate check.

You may dismiss the modal, and the footer continues to quietly show the release or branch-build notification.

You may also choose to "Never check again" either in the modal or by selecting "About" in the footer.

If you choose to never check again and wish to re-enable the checking, the opposite setting is available in the "About" footer, as well as in the update check section in the maintenance panel.

Technical information on the update check process is available in the [WsprryPi Automatic Update Polling](update_check.md) technical page.

## Support Bundle

Use **Support Bundle** when the WsprryPi maintainer asks for diagnostic information. The workflow records useful support context, creates a readable `.tar.gz` candidate locally, lets you inspect it, encrypts the exact bytes you approve, and hands only the encrypted `.age` file to a private Dropbox File Request.

Review the readable archive before encryption. See [Create and Share a Support Bundle](support_bundle.md) for privacy guidance, collection inventory, encrypted upload, receipt handling, truthful upload states, GitHub correlation, and cleanup.

```{toctree}
:maxdepth: 1
:hidden:

Back Up or Restore an Installation <backup_restore>
Create and Share a Support Bundle <support_bundle>
Privileged Network Safety <network_safety>
```
