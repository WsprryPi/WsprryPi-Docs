# Device-owned scheduling

Choose the device beside the Setup tabs, then open **Scheduling**. The same controls manage **This Pi** and a verified paired Pi. Confirm the full identity, connection, execution owner, and output destination before editing. The selected transmitting device owns and runs its native schedule. A controller manages that device's settings; it does not dispatch WTP transmissions.

An updated Pi can still retain its previous local scheduler. Use
[local scheduling migration](../../Maintenance/index.md#migrate-a-local-pi-schedule)
in the current software before enabling native recurrence. Migration saves the
schedule disabled; explicit enable is a separate step. Older remote WTP
deployments require [retirement before upgrading](../../Maintenance/index.md#retire-remote-wtp-work-before-upgrading).

The selected Pi runs accepted schedules without an open browser or management controller. Closing the page does not stop a schedule. Reading, changing the selected device, and **Review draft** do not save or enable anything.

## Prepare, save and enable

**Enable scheduling** prepares a browser choice and makes dependent fields editable. It does not change the saved permission. **Saved scheduling** shows the last confirmed permission; **Application** and target observations describe application separately.

1. If saved scheduling is enabled, select **Disable saved schedule** and confirm the result. Disabling prevents new admissions; previously accepted work may finish.
2. Turn on **Enable scheduling** to prepare a draft, then choose the policy below. Leave **Use solar day/night selection** off for ordinary scheduling without solar location or clock prerequisites.
3. Select **Save disabled policy**. Wait for the confirmed saved-value readback. A failed or unconfirmed save retains the draft and does not enable it.
4. Select **Enable saved schedule** only after reviewing the confirmed saved policy. Unsaved or invalid entries keep this action unavailable.

Schedule permission, solar selection, **Transmit**, boot behavior, ownership and immediate **Stop** are independent. Scheduling alone cannot grant ownership or turn on Transmit. Complete **Set up this transmitter** or the applicable takeover workflow on [Maintenance](../../Maintenance/index.md) when ownership is not ready. Review the target’s supported output and frequency policy before permitting transmission.

## Solar periods and frequency inheritance

Solar selection uses the selected target’s saved locator center. Enter a 4, 6 or 8 character Maidenhead **Target-site locator**. A blank locator holds solar occurrences; it does not inherit the browser’s or controller’s location. Native Pi GPS is unavailable through these controls. Browser timezone and location do not determine execution.

Expand **Day** or **Night** to allow or skip occurrences. Expand **Morning** or **Evening** to enable its gray-line period. Elevation limits are degrees, with up to three decimal places, between −90 and +90. The lower limit must be below the upper limit; lower is inclusive and upper exclusive. The target evaluates periods at the actual candidate start, with its own clock and saved policy.

A blank **WSPR frequency list override** inherits the selected Pi’s saved Signal Setup WSPR list, skips, profile and band preferences. An explicit override retains the full list syntax and its selected list profile. A blank **CW base override (Hz)** inherits that target’s saved CW base. Explicit CW values accept up to eight decimal places and preserve the saved shift. Review the [WSPR](../Signal_Setup/wspr.md) and [CW](../Signal_Setup/cw.md) frequency meanings; these fields do not change mode semantics or bypass backend limits.

Disabled periods keep their saved values, and those values must still validate. Turning solar selection off preserves its policy. **Review draft** summarizes entries without saving, predicting a guaranteed transmission, or granting authority.

## Observe and recover

**Target observations and forecasts** separates saved and active revisions, clock state, selected period, frequency, waiting reason and observation age. A forecast may be unknown and is not evidence that output occurred. Target clock uncertainty, missing location, unsupported output, or ownership can hold an occurrence. Native Pi solar-clock qualification is supported on Linux; Mac solar health remains unknown, while ordinary scheduling with solar selection off does not require solar prerequisites.

Switching devices retains each Pi’s valid or invalid draft in the open page. Changing identity, boot, pairing or capability pauses editing until a fresh verified read. Unavailable Pis with scheduling drafts or earlier requests remain selectable for read-only review. Selecting such an entry does not reconnect or send settings. These browser drafts do not survive a reload. Scheduling and the other Pi settings editors retain separate drafts; after another editor saves, review a revision conflict instead of overwriting its changes.

After an interrupted reply, use **Check earlier scheduling request**. This looks up the original operation and never resends the save or enable. If its outcome stays unknown, read current scheduling for review, compare it with the retained draft, and explicitly confirm the review. Review clears a recovery barrier; it does not declare the historical operation successful. **Discard draft and read again** asks before replacing entries.

Scheduling retains at most 64 target editing entries in the open page. If device changes fill that cache, a new target stays unavailable and existing entries remain intact. Return to retained devices to resolve or copy needed drafts before reloading. No save is sent by reaching the limit.

When the device is busy, retain the draft and check or read again. Loss of contact does not prove output stopped. Use the separate output-stop workflow and verify its current observation when immediate shutdown is needed; disabling scheduling only stops new admissions.

## Pico scheduling

For a supported Pico, Scheduling exposes its existing WSPR recurrence, WSPR periods/phases and gray-line controls with their own reads, saves and activation feedback. WSPR recurrence and keyed-message recurrence are independent; there is no combined master switch. The verified adapter cannot read or edit the independent keyed-message schedule state, so that state remains unavailable here; use the Pico’s own controls.

Pi day/night frequency profiles are unavailable on Pico. The controller does not emulate them with sunrise writes. Unsupported controls stay unavailable, and reading or selecting a Pico does not change its schedule or output ownership. See [device selection and resource recovery](../index.md#choose-and-edit-a-device) before switching devices or reviewing an unknown Pico write.
