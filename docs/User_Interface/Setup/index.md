# Setup Card

Use **Device** beside the Setup tabs to choose whose settings you are editing.
On a phone, the selector appears on its own row. **This Pi** opens the local
settings. A saved Pico or a verified paired Pi opens its independent settings without selecting it as this controller’s output. Confirm the name, device identity, connection, and
status below the selector before editing.

The five tabs are:

- [Signal Setup](Signal_Setup/index.md): local WSPR/CW settings, or the selected
  Pico's station progress and station defaults.
- [Scheduling](Scheduling/index.md): the selected Pi’s device-owned schedule permission and solar policy, or the Pico’s supported independent recurrence controls.
- [Transmitter](Transmitter/index.md): the selected device's supported output
  settings. Pico amplifier timing, drive, filters, and Si5351 have explicit actions.
- [Device I/O](Pi_IO/index.md): local Pi pins, or Pico connections, logging, and
  the complete RF-engine, pin, and GPS plan.
- **Fleet**: discovery, saved management connection profiles, and read-only
  legacy scheduling and retirement records.

## Choose and edit a device

Selection alone never saves, enrolls, claims ownership, enables transmission,
changes the backend, or changes accepted work. A nearby or unverified choice
opens Fleet for identification and profile review; it grants no settings access.
A controller-only installation has no local transmitter settings, but can manage
supported saved Picos, paired Pis, and supported Picos attached to those Pis through the same tabs. Establish a Pi connection through [Controller access](../Maintenance/index.md#controller-access) first. Attached Picos use that existing connection automatically.

### Edit a paired Pi

Select the verified Pi under **Device**, confirm its identity, and use **Read saved settings**. Its settings appear under the existing Signal Setup, Transmitter, and Device I/O tabs. Changes stay in that Pi’s browser draft until you select **Save this Pi’s settings**; switching tabs does not save them. Use the separate [Scheduling](Scheduling/index.md) tab for device-owned schedule permission and solar policy. Signal Setup saves do not enable scheduling.

Switching devices retains each Pi’s draft, including an invalid entry. **Discard draft and read again** asks before replacing it with current saved values. These drafts remain in the open browser page; resolve needed entries before reloading or closing it.

After a lost save reply, use **Check earlier request**. This checks the accepted operation without resending the save. If its outcome remains unknown, read current settings for review and use **I reviewed these settings** only after comparing them with your retained draft. Review allows a later deliberate change; it does not assert that the earlier save succeeded. Changed ownership, boot, or unavailable management pauses saving until a fresh verified read.

**Stop this Pi’s output** is a separate action. Select **Read current output**, verify the identified output, and then select **Stop the output shown above**. Read again when the observation is stale. This action turns off the Pi’s saved Transmit permission; it does not change pairing or schedule enablement. Stop remains available when an earlier settings save is unconfirmed. Its own result is tracked separately, and the earlier request and your draft remain available for review. Acceptance does not prove that output is inactive; read the current output again.

### Edit local or Pico settings

Local settings autosave after validation. Read the status beside the Setup title;
a saved value may still await application while committed work owns the output.
When you leave an unsaved local draft to manage another device, it is retained
and autosave pauses. On returning, review it and choose **Save retained local
draft** to resume saving. Returning alone does not publish the draft.

Pico settings use explicit resource-specific reads, validation, saves, and,
where supported, separate application or restart actions. Feedback belongs to
the selected resource and device. **Saved** is different from active or awaiting
restart. Existing jobs and schedules keep their own authority; reading settings
does not stop or take over work. A device can refuse a change while work is active.

Switching between Picos retains each browser draft. A write already accepted on
the old device remains in **Target request outcomes**. A lost reply requires
saved-value readback and explicit review before a new deliberate save. Profile
replacement, changed boot, or lost capability pauses the editor; **Reconnect
selected device** negotiates a fresh context. Replaced-profile drafts remain available for read-only inspection. Reconnecting
the same profile can retain its entries, but a fresh resource read and deliberate
review are required before saving through the new context. These browser drafts
do not survive a page reload; resolve or copy needed non-secret entries before
leaving. Passwords are excluded from retained-draft inspection.

**Controller time and power** belongs to this Pi. Pico settings and native
schedules belong to the device selected under **Device**. Selecting a Pico
does not change this Pi’s RF backend.

## Pi and Pico Fleet setup

Open **Setup → Fleet** to discover devices and save their management connection
profiles. Confirm the full device ID; names may be duplicated. A saved profile
and an authenticated connection are separate steps. Open the selected device’s
settings through **Device**. Saving a connection never enables a schedule.

### Manage existing output schedules

**Legacy output schedules** displays saved controller assignments and unresolved
recovery duties. These records do not dispatch work. **Migration required** means
that WTP-capable software must resolve the old authority and accepted work before
replacement. **Retired** means the recorded controller retirement completed; it
does not establish that the target is online or stopped. View the saved identity
and retirement status without deleting the recovery files.

Complete the [pre-upgrade WTP retirement procedure](../Maintenance/index.md#retire-remote-wtp-work-before-upgrading)
for every affected controller and transmitter. Offline targets, unknown output,
and unresolved retirement keep the affected deployment on WTP-capable software.
Other devices can still be managed independently.

### Review action results and unsaved entries

Pico saves and native stop can become unconfirmed after a lost reply. Read the
current value from the same device and boot, compare it with your retained draft,
and explicitly review the outcome. Do not resubmit an unknown write. A changed
identity, boot, profile, or authority requires a fresh connection and readback.
Closing the browser does not stop a device-owned schedule.

### Configure the target Pi

Choose a paired Pi under **Device**. Its native schedule, local Enable state,
status, and stop controls belong to that Pi. Pairing grants only the approved
management purposes; it does not create a remote transmission endpoint.
