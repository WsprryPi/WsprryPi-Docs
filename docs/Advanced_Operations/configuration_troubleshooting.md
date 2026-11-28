# Configuration Troubleshooting

## Troubleshooting CW Configuration Saves

When a QRSS, FSKCW, or DFCW message would take longer than its configured repeat interval, Setup marks the Message field invalid and displays **Save failed** with the calculated duration and repeat interval. The invalid draft remains in the browser so it can be corrected, but it is not applied to the running configuration. Autosave resumes automatically when the adjusted duration is less than or equal to the repeat interval.

This inline state identifies a timing problem that can be corrected on the Setup page. Other configuration reload failures that cannot be tied safely to an editable field may still appear in the general reload-failure dialog and may require checking the application log or saved settings.

See {ref}`cw-message-too-long` for the duration inputs and correction steps.

## GPIO RF Output Conflicts

When the GPIO transmitter backend is selected, its configured GPIO4 or GPIO20 RF output cannot also be assigned to an enabled Band GPIO, Transmit LED, Shutdown Button, or Amp Control. Setup marks both conflicting controls with `GPION is reserved by GPIO RF Output.` and keeps the invalid draft visible without saving it.

Resolve the conflict by changing either pin, disabling the ordinary GPIO role, or selecting the Si5351 backend. The reservation depends on the selected backend, not the **Transmit** switch, so turning transmission off does not release the GPIO RF output pin. Disabled ordinary roles may retain their pin values.

(startup-transmission-is-inhibited)=
## Startup Transmission Is Inhibited

At every daemon start, WsprryPi attempts to disable the selected transmitter backend before it starts services or schedules any transmission. If the safe state cannot be confirmed, the daemon continues running for diagnosis but blocks all transmission paths. This startup inhibition is separate from the saved **Transmit** switch and **Enable on Boot** policy.

Review the WsprryPi log for the startup-quiescence error, then check the hardware selected on the **Setup > Transmitter** page:

- For **Si5351**, verify the configured I2C bus and address, device wiring and power, and that the device is visible to the operating system.
- For **GPIO**, verify that the Raspberry Pi model supports direct GPIO-clock transmission, that the configured transmit pin is GPIO4 or GPIO20, and that the service has the permissions required to access the Pi peripherals.

Also correct any configuration error identified in the log. The daemon deliberately does not clear this safety latch after a validated settings application, mode change, or transmission-toggle change.

After correcting the cause, restart the service:

```console
sudo systemctl restart wsprrypi.service
```

Then confirm in the log that the configured backend was selected without a startup-inhibition error. After a successful restart, the saved **Enable on Boot** policy requests Transmit permission subject to the independent scheduling setting, restore holds, and other admission checks.

Do not repeatedly restart the service without correcting the reported cause. If the failure persists, leave transmission disabled and collect a support bundle from **Maintenance** before requesting help.

## Pi 5 RP1 Route Is Unavailable or Mismatched

Leave transmission disabled when the route panel reports **Unavailable**, **Mismatch**, **Restoration failed**, or **Recovery required**. Do not edit provider files, unload modules, or try to select a route manually.

The normal installer supplies and validates the RP1 provider and route manager on Pi 5-family systems. Re-run the [WsprryPi installer](../Install/index.md#install-wsprrypi) first. It can recover and update an exact installer-owned runtime, but it refuses foreign, modified, mixed, or unproven provider state rather than overwriting it.

After installation, `/dev/rp1-gpclk` is normally absent until a route is selected. Route switching and removal happen in the current boot. For a selected route, requested, persisted, configured, and active routes must all be GPIO4 or all be GPIO20. For a removed route, configured and active must both be None, and the transmission consumer endpoint must be absent. Eligibility and cleanup must also be accepted; WsprryPi does not fall back to another route or backend.

For **Restoration failed**, correct the reported service error and follow the command shown in the route panel. For **Mismatch** or **Recovery required**, preserve the displayed state and collect a support bundle before making manual changes. The exceptional **Recover to no route** action intentionally leaves WsprryPi stopped and inhibited; use **Remove route** for normal removal. The RP1 diagnostics include endpoint, route-manager socket, persisted-route, and journal-inventory observations when readable. If the installer reports an ownership, identity, or recovery refusal, preserve that state and the retained installer failure details; do not unload modules, delete journals, or edit provider files manually.

## Pico hostname or restart is unconfirmed

Use [Change the hostname in the Pico manual](https://wsprrypico.readthedocs.io/en/devel/maintain.html#change-the-hostname) for the device-side save, restart, and sign-in procedure. WsprryPi's settings form does not rename the Pico; renaming a Fleet profile changes only its label. If a Pico save or restart reply is lost, read the saved and active state before repeating it. A timeout does not prove the change failed or output stopped.

Keep the affected transmitter’s schedule disabled while reviewing the destination. Resolve pending, owned, or uncertain jobs through [Pico status and recovery](../User_Interface/Setup/Transmitter/index.md#pico-status-and-recovery). Disabling Pi transmission alone does not disable Pico's autonomous schedule.

| What you see | What to do |
| --- | --- |
| Browser opens at the new name, but WsprryPi cannot connect | Review the saved management profile, hostname, carrier, and management port. Verify the full device ID after reconnecting. |
| Fleet still shows the old destination | Edit and freshly identify the saved management profile, then reconnect the selected device. Editing a profile label does not change its address or identity. |
| New name is unreachable | Try the current LAN IPv4 address and verify the full device ID. Follow the Pico manual for duplicate-name or setup-Wi-Fi recovery. |
| Different full device ID | Verify the intended board and address before using it. Renaming does not change the stable ID. |
| Certificate or hostname-certificate error | Check the expected TLS identity and provisioned credentials. Keep verification enabled and preserve the chosen transport. |
| Pico restart remains unconfirmed | Follow the Pico manual's readback/reconnect procedure. A returning page or countdown alone does not establish a new boot or readiness. |

[After a Pico hostname change](ini_configuration/transmitter_backends.md#after-a-pico-hostname-change) explains which Pi settings to update. Keep [Privileged network safety](../User_Interface/Maintenance/network_safety.md#pico-hostname-and-management-access) enforced; disabling the Pi's LAN policy does not repair discovery or Pico credentials. Device-side reset and access recovery belong to the [Pico maintenance guide](https://wsprrypico.readthedocs.io/en/devel/maintain.html) and [Pico troubleshooting](https://wsprrypico.readthedocs.io/en/devel/troubleshoot.html).

## Device management remains unavailable or unconfirmed

Read the reported connection, storage, or identity error before retrying. Confirm the selected device’s full identity, management profile, and current connection. A controller that cannot reach a transmitter cannot establish that its output is off.

After an unconfirmed save or stop, read authoritative current status and review the original result. Do not repeat an unknown mutation. A changed boot, profile, or authorization requires a fresh connection and readback. Preserve configuration and recovery records when requesting support.

## First scheduling setup remains held

An upgrade from a version earlier than 4.x to version 4.x migrates the existing local schedule once and saves scheduling disabled after verifying ownership and inactive output. Fresh installations use **Set up this transmitter**; later 4.x updates do not repeat the upgrade migration. If setup cannot finish, scheduling remains held. Read the reported output, ownership, or storage error, preserve the established settings and history, and correct the cause before retrying normal startup. Do not delete recovery files or use Reset to bypass a hold.

After **Migration completed; schedule disabled pending review.**, review the saved policy under [Setup → Scheduling](../User_Interface/Setup/Scheduling/index.md) and enable it when ready. No separate migration action is required.

## Native scheduling is held or a solar save is rejected

Read the target's current settings and status separately. A saved policy does not establish active output. Enable scheduling must be on, Transmit must permit output, and initial scheduling and transmitter setup must be complete. Scheduling off and solar waits do not release output ownership. After a lost reply, recover the original receipt and read authoritative settings before another action.

For a time hold, check Linux OS synchronization and leap/clock alarms, the 2025–2099 date range, and the 250 ms uncertainty limit. Holdover requires a healthy sample during this boot and expires within one hour. Without the approved clock-health provider, solar recurrence stays held. Check the transmitter's saved locator for a location hold. A backward clock step waits beyond the consumed watermark; a forward step does not queue missed transmissions.

For a storage or recovery hold, preserve the progress and transaction records. An interrupted reservation is not proof of RF output. Confirm output is safely reconciled before resuming; missing or corrupt established history cannot be repaired by deleting files or repeating initial setup. See [native recurrence and time readiness](ini_configuration/runtime.md#native-recurrence-and-time-readiness).

Check the uppercase site locator, ordered millidegree window bounds, decimal CW base, and every WSPR list entry, including overrides for disabled periods. A changed frequency must satisfy the selected Pi backend and current frequency policy. Repair a rejected draft through a fresh validated save; do not remove managed history or edit private state files. Preserve the reported storage or recovery error when seeking help.

## Scheduling remains disabled or held

In [Setup → Scheduling](../User_Interface/Setup/Scheduling/index.md), distinguish the editable draft from **Saved scheduling** and active application. Save the disabled policy and confirm readback before explicitly enabling it. Complete Maintenance initialization when required and resolve any reported ownership hold. For solar holds, check the target’s saved locator and clock observation; browser location and timezone cannot repair a target prerequisite. After a lost reply, check the original operation rather than repeat a save. Keep the draft during a conflict, disconnect, or busy response.

## Browser unavailable or saved state cannot open

For a controller-only host, start with the [platform service and log checks](../Install/controller.md#local-command-and-service-paths).

For a Raspberry Pi transmitter with the SQLite implementation, check the three services separately before restarting anything:

```sh
systemctl status wsprrypi.service wsprrypi-web.service wsprrypi-maintenance.service
journalctl -u wsprrypi.service -u wsprrypi-web.service -u wsprrypi-maintenance.service --since "10 minutes ago"
```

A browser-service failure does not stop the backend's schedule or a remote device's autonomous work. A backend failure makes ordinary browser operations unavailable; it does not authorize default settings or replay. Check Apache proxy configuration against the active listener ports after a manual port change. Use the [local settings read command](../Command_Line_Operations/saved_settings.md#read-and-change-advanced-settings) to distinguish saved ports from explicit startup overrides.

If the established SQLite state is missing, corrupt, or held, preserve the application root, migration backup, credentials, and recovery records. Do not delete generations, reimport the INI, initialize replacement identity, or use Repair/Reset to bypass admission. Collect available diagnostics and follow the reported recovery requirement. The standalone support collector can gather service/log observations even when settings export is unavailable.

For an interrupted restore, select the existing job under **Recent backup or restore** and use **Refresh results**. After correcting the reported condition, **Recover this restore** resumes a confirmed held job. The [local maintenance commands](../Command_Line_Operations/saved_settings.md#backup-and-restore-from-a-local-terminal) provide status and resume if browser access is unavailable. Do not cancel a confirmed job as an upload or repeat confirmation after a lost reply.

For an installer interruption during first state admission, use [Resume interrupted initial state admission](../Command_Line_Operations/saved_settings.md#resume-interrupted-initial-state-admission). This resumes the original admitted migration or initialization while the backend is stopped; it does not replace corrupt established state or resume a restore job.
