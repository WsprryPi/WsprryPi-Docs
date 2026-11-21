# Back Up or Restore an Installation

Use **Maintenance → Backup and restore** to save an encrypted installation backup, download it, and restore it on this installation or move supported settings to another computer. This workflow applies to the SQLite source implementation; it is separate from [Support Bundle](support_bundle.md), which creates diagnostics for troubleshooting.

## Create and download a backup

1. Stop local transmission and Test Tone, and disable armed local work. Backup refuses a busy or uncertain output state; it does not stop RF automatically. A controller-only installation has no local output to stop.
2. Enter **Backup passphrase** and **Confirm passphrase**, then select **Create backup**.
3. Read the job status until creation finishes, then select **Download backup**.
4. Keep the downloaded `.age` file somewhere other than this computer's SD card, and retain the strong, unique passphrase separately.

A lost passphrase cannot be recovered. A failed download can retry the same completed artifact without creating another snapshot. Local job history is bounded: one active job and up to three prior terminal jobs. Download backups you intend to keep; the local job list is not a permanent archive.

The backup includes supported local settings, Fleet definitions, the coordinated SQLite snapshot, and necessary private identity, credential, authority, and recovery records. It excludes the operating system, application executable, logs, and transient browser sessions. It is not an SD-card image. Each remote Pi or Pico retains its own state and needs its own backup procedure; this backup does not capture their independent schedules or output state.

Backups use the supported age passphrase-encrypted recovery format, with a maximum encrypted archive size of 2 GiB. Arbitrary age files are not installation backups. Keep enough free space on the source and destination for staging, validation, and retained recovery copies. An authenticated file still needs full installation validation before restore.

## Upload and validate

1. Under **Encrypted backup file**, choose the downloaded backup and select **Upload backup**.
2. Enter its passphrase and choose **Recover this installation** or **Move settings to another computer**.
3. Select **Validate backup** and wait for the preview. Validation does not replace the destination settings.
4. Review the source installation, date, role, concrete setting changes, retained destination values, connection warnings, and listener-port changes.

**Recover this installation** is for the same installation's recovery. **Move settings to another computer** preserves the destination's identity, authority, transmitter backend, wiring and GPIO assignments, calibration, Si5351 adapter/reference setup, Band GPIO, network safety, and experimental frequency policy. Portable station/signal settings, custom CW fades, startup preferences, debug logging, and listener ports can move. Restore does not convert a controller-only installation into a transmitter or the reverse.

Source credentials and old operation results do not become fresh destination permission. Unmatched network definitions remain unresolved; moved USB definitions require destination transport selection. Review connections and use the existing pairing/recovery workflow where required. Restore neither stops remote transmitters nor adopts or replays their work. Retire the old installation before reusing relocated credentials; the backup does not provide clone detection.

## Confirm and reconnect

Select **I reviewed this destination and the proposed changes.**, then **Confirm restore** only after reviewing the preview. The independent maintenance worker prepares holds, drains and stops the backend, publishes a complete replacement generation with a protected prior copy, restarts the backend, and verifies the result.

If the browser disconnects, reconnect, select the existing job under **Recent backup or restore**, and use **Refresh results** to read its status. Do not upload or confirm again merely because a reply was lost. Recovery requests and downloads retain the previously admitted endpoint across a listener change; ordinary controls use the active destination endpoints. Results distinguish saved ports from startup overrides. Only installer-managed Apache upstreams are reconciled; custom proxy configuration needs administrator review.

An unconfirmed upload can be cancelled. Once confirmed, a failed restore remains held with its job and recovery evidence; it cannot be discarded as an upload. Correct the reported condition, then use **Recover this restore** or resume that job through the [local maintenance command](../../Command_Line_Operations/saved_settings.md#backup-and-restore-from-a-local-terminal) if browser access is unavailable. The worker can retain completed downloads while the backend is down. Missing or corrupt established destination state still requires explicit recovery; deleting the database or initializing a new identity is not a restore procedure.

## Review the restored destination

A completed restore keeps independent persistent **local output** and **remote authority** holds across restart. Completion is not permission to transmit.

1. Select **Read current destination** and check the current saved settings, output path, and device connections.
2. Select only the review acknowledgements that match the holds reviewed.
3. Select **Release selected holds** and read its result.
4. For a local transmitter, verify the RF path and use the existing Start control when ready. Local hold release leaves transmission stopped; saved Enable on Boot intent remains saved.

A controller-only destination offers remote-authority review without a local transmitter control. Releasing the remote hold removes the additional restore gate; current pairing, revocation, ownership, and scheduling checks still apply. A process exit, Stop receipt, or reboot alone is not proof of physical output cleanup. If status remains uncertain, preserve the reported evidence and resolve the owning transmitter's recovery condition before further work.
