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
- **Fleet**: discovery, saved connection profiles, output assignments, and
  explicitly labeled controller output and firmware actions.

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

**Controller time and power**, the output connection, and USB firmware actions
belong to the controller. Select **This Pi** before using its output connection controls. Firmware
status/recovery remains available through its separate maintenance guard; it
always refers to the controller’s active USB output, not the Device selection.
**Use this device** in Fleet remains the separate, confirmed output-selection
action. The shared Device selector does not perform it.

## Pi and Pico Fleet setup

Open **Setup → Fleet** to manage saved Pi and Pico devices and independent
output schedules. No developer-console setting is required. The
[device catalog workflow](Transmitter/index.md#add-a-pico-and-manage-outputs)
explains how to identify and save a profile. Browsing Fleet does not start
transmission. Pi WTP servers use **Plain LAN**. Paired Pi settings management uses a separate authenticated TLS connection; pairing does not encrypt or replace WTP.

### Manage existing output schedules

Fleet frequency inputs are absolute RF references: WSPR RF center, finite tone
or QRSS carrier, FSKCW space, or DFCW dot. For standard 20m WSPR enter
`14097100`, rather than USB dial `14095600`. Fleet applies no dial conversion
or random placement. FSKCW mark and DFCW dash add the positive shift. Changing
modes updates the labels while preserving draft and saved frequency values.

Fleet assignments and listener settings use explicit save buttons, unlike
ordinary Setup autosave. Review the feedback beside the action before leaving.

Adding a remote-output schedule is unavailable. Existing assignments remain
available for review and management. Open **Edit schedule** beside an existing
output to review its saved mode, frequency, timing, and connection. Changes use
**Save schedule**; ordinary Setup autosave does not save this editor. Earlier
new-assignment drafts remain available for inspection, with Save disabled.

A central Pi supports zero through 32 remote output schedules alongside its
own local schedule. **Use this device** selects the separate single-endpoint
`[WTP]` backend; it does not create an independent output assignment. Saving or
removing a catalog profile also does not create or remove an assignment.

Pico settings use the shared **Device** selector independently of output
assignments. USB firmware maintenance remains bound to the controller's active
output; confirm its full identity before using that separate Fleet workflow.

The local schedule does not consume a remote slot. The saved-device catalog holds
up to 64 connection profiles independently of these assignments. The capacity
shown under **Output schedules** includes unresolved contexts retained after a
local takeover; use **Reconcile** to resolve their recovery duties.
Saved schedules survive restart, including paused states and consumed slots.
Uncertain jobs remain blocked until explicitly reconciled and resumed.

Keep a private backup of Fleet settings. Pause and reconcile affected outputs
before removing assignments; do not edit away recovery barriers or prune the
assignment file by hand.

Each target must advertise support for the assigned job. Native GPIO, RP1 and
Si5351 Pi servers report their WSPR, TONE, QRSS, FSKCW and DFCW capabilities.
The selected backend's processor, route, and frequency policies still apply.
RP1 retains its exact-operation host confirmation; Fleet does not create it.
Pi and Pico jobs are checked against the selected target's reported capabilities. For a Pi profile, set the start-uncertainty limit
to accommodate the reported clock uncertainty, no higher than `500000000` ns
(500 ms); the existing 1 ms default can reject ordinary NTP timing. Values are
never silently increased.

Remote scheduling requires the controller's explicit
[unqualified-frequency permission](../../Command_Line_Operations/transmitter_backends.md#experimental-frequency-policy).
A saved profile or discovered device does not grant that permission.

**Pause and stop**, **Edit schedule**, **Reconcile**, and **Remove assignment**
affect only the selected output. Editing requires a paused, reconciled output.
Failed or uncertain work pauses that assignment; after an interrupted job,
use **Reconcile**, inspect the result, then **Resume**. A consumed schedule slot
is not automatically retried. Other remote outputs and the local schedule
remain independent. A disconnected target has unknown output state; loss of
contact does not prove it stopped.

### Review action results and unsaved entries

Fleet assignment controls report acceptance separately from completion. Read the result beside the affected output before starting another action. An unconfirmed response may follow a successful change; read current status and review it rather than repeating a command blindly. If a controller reply cannot be matched to your action, its result remains unconfirmed and unsaved entries are retained. Reconcile is unavailable while an earlier assignment action is still being processed or the controller inhibits reconciliation. Operations provides the same assignment controls for one selected device, with controller controls kept separate.

Unsaved schedule entries retain their original assignment and reviewed revision. Opening another schedule offers **Continue existing draft**, **Discard draft and open selected schedule**, or **Cancel**. A changed or replaced assignment cannot inherit the draft's authority. New-assignment drafts also retain the reviewed saved output. If that profile changes or its earlier review is unavailable, entries remain visible for inspection and Save is disabled. Discard the draft and reopen the intended output to review it before saving. Failed saves preserve entries. Confirmed persistence clears only unchanged submitted entries. Edits made while Save was pending, and entries that cannot be matched to that submission, remain available for inspection with their original reviewed revision. Reopen the current assignment and review it before another save.

To stop this controller from starting further occurrences of an existing
assignment, select **Retire schedule**, then **Review retirement**. This review
is available for offline and busy outputs as well as paused schedules. Confirm the named
output and select **Retire this controller’s schedule**. Already accepted work
finishes first. Offline output, uncertain work, or foreign ownership keeps the
result pending. Use **Check saved result** after an interrupted reply. Retirement
survives restart and restoration of an older assignment file; **Resume** cannot
reopen it. Retirement does not create or enable a replacement target schedule.

Removing an output first pauses it and requires confirmed cleanup of this controller's owned work. Failed cleanup retains the paused assignment and recovery duty. Reconcile it, inspect the result, then explicitly remove it again if required. A target-local takeover can remove an assignment independently; its unresolved retained context continues consuming capacity until cleanup is established. Keep the private Fleet recovery files with the assignment state when backing up or restoring configuration. Do not delete them to bypass a recovery block.

### Configure the target Pi

Expand **This Pi's WTP listener** to configure inbound admission, port, and
interface, then choose **Save listener settings**. The listener defaults to enabled on port `31417`. With local Enable
off, it accepts ownership claims after startup confirms safe, idle output.
Local Enable on reserves the output, including gaps between local jobs;
inspection remains available but new claims are refused. Outbound Fleet
schedules do not change either setting.

`auto` selects a single eligible physical LAN IPv4 interface. If several are
eligible, select one explicitly, such as `eth0` or `wlan0`. Avahi advertises the
listener through DNS-SD. If discovery is unavailable, a manual Plain LAN profile
can still use the configured address and port. A discovery entry is only a
connection hint; identify the device before saving it. Plain LAN is unencrypted,
and its observed device ID is not cryptographic authentication.

See [local takeover](../index.md#local-control-and-remote-ownership) before
reclaiming an output from a remote controller, and the
[listener INI reference](../../Advanced_Operations/ini_configuration/runtime.md#wtp-server)
for interface and recovery details.
