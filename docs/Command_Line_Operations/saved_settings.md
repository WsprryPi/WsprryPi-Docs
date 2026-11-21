# Saved Settings and Local Maintenance

These commands apply to the SQLite and separate web service source implementation. Use the installed executable's `--help` to check availability; older published releases use their version-specific instructions.

## Read and change advanced settings

Keep the backend running for settings commands. These commands contact it through authenticated local IPC; they do not edit SQLite offline. Ordinary station, transmitter, and scheduling settings remain in the existing Setup pages.

```sh
sudo wsprrypi --settings --help
sudo wsprrypi --settings read
```

Read the returned revision, then use that exact revision in a change. In this example, replace `7` with the revision just read:

```sh
sudo wsprrypi --settings write --expected-revision 7 \
  --set 'CW.Fade In Ms=25' --set 'CW.Fade Out Ms=25'
sudo wsprrypi --settings read
```

All `--set` arguments form one validated change. A stale revision or invalid value leaves every saved setting unchanged. If a reply is lost, read settings before another write. Readback distinguishes saved and active values; a successful save does not establish that a running transmission has changed.

The following supported settings have no ordinary Setup controls. Names are case-sensitive.

**Controller-only and local transmitter installations:**

- `Meta.debug_logging`: `true` or `false`.
- `Operation.Web Port`: integer 1024–49151.
- `Operation.Socket Port`: integer 1024–49151, different from Web Port.

**Local transmitter installations only:**

- `Experimental.Allow Unqualified Frequency`: `true` or `false`.
- `Experimental.Allow Non-Amateur Frequency`: `true` or `false`; requires the unqualified-frequency permission.
- `Si5351.TX Output`: `CLK0`, `CLK1`, or `CLK2`.
- `CW.Fade Shape`: `none`, `linear`, or `raised_cosine`.
- `CW.Fade In Ms`: integer 0–2147483647, milliseconds.
- `CW.Fade Out Ms`: integer 0–2147483647, milliseconds.
- `CW.Fade Slice Ms`: integer 1–2147483647, milliseconds.

Accepted numeric bounds are parser limits, not recommendations for useful RF settings. Normal cross-field and transmitter validation still applies. See [CW mode options](cw_modes.md) and [experimental frequency policy](transmitter_backends.md#experimental-frequency-policy) before changing these values.

Listener-port edits take effect after backend restart. An explicit startup override can keep an active port different from its saved value; remove that override to use the saved port on a later start. Custom Apache proxies must match active ports. Network safety keeps its separate [Maintenance workflow](../User_Interface/Maintenance/network_safety.md); it is not part of this command.

## Backup and restore from a local terminal

The [Maintenance backup and restore guide](../User_Interface/Maintenance/backup_restore.md) explains capture prerequisites, restore purposes, destination review, and persistent holds. The same worker and validations serve these local administrator commands, including when the browser or Apache is unavailable. The worker must be available, and the backend must be able to validate the selected destination. This is not an automatic repair of a corrupt established database.

```sh
sudo wsprrypi --maintenance help
sudo wsprrypi --maintenance jobs
sudo wsprrypi --maintenance backup
sudo wsprrypi --maintenance status --job-id JOB_ID
sudo wsprrypi --maintenance download --job-id JOB_ID --output /absolute/new-backup.age
```

Use the returned job ID. Backup prompts for a passphrase and confirmation with terminal echo disabled. Keep the passphrase separately from the downloaded file. Download refuses to overwrite an existing file and verifies the artifact digest. Read `status` until the job finishes; an admitted job is not a completed backup.

For a restore, upload once and choose exactly one validation purpose: `recover` for this installation, or `move` for another computer.

```sh
sudo wsprrypi --maintenance upload --file /absolute/backup.age
sudo wsprrypi --maintenance validate --job-id JOB_ID --purpose recover
sudo wsprrypi --maintenance status --job-id JOB_ID
```

For a move, replace `--purpose recover` with `--purpose move`. Validation prompts for the backup passphrase and does not change the selected destination. Review the full preview before confirming with its exact digest:

```sh
sudo wsprrypi --maintenance confirm --job-id JOB_ID --preview-digest PREVIEW_SHA256
sudo wsprrypi --maintenance status --job-id JOB_ID
```

A lost reply calls for status readback, not another mutation. An interrupted confirmed job keeps its recovery evidence and holds. Correct the reported condition, then resume the same job. Cancel applies only before confirmation:

```sh
sudo wsprrypi --maintenance resume --job-id JOB_ID
sudo wsprrypi --maintenance cancel --job-id UNCONFIRMED_JOB_ID
```

After successful restore, read a fresh destination review. Release only the holds reviewed, using the returned current digest:

```sh
sudo wsprrypi --maintenance review
sudo wsprrypi --maintenance release --review-digest CURRENT_REVIEW_SHA256 --local
```

For remote-authority review, read `review` again and use its fresh digest with `--remote` instead of `--local`. Controller-only destinations have no local transmitter hold to release. Local release leaves transmission stopped; use the normal Start control after checking settings and the RF path. Remote release does not pair, adopt, stop, or command another device.

Passphrases must not appear in arguments, environment variables, or shell history. For automation, the help describes private descriptors numbered 3 or higher; account for the privilege tool's descriptor policy rather than passing a secret on the command line.

## Resume interrupted initial state admission

The installer checks an existing state root and refuses incomplete or damaged state; it does not guess whether to initialize or migrate again. If installation was interrupted during the first state admission, keep the compatible executable, application root, `.prepare` staging, migration backup, and original installer log. Keep the backend stopped while resuming this operation. An admitted restore job uses its own status/resume workflow above, not these commands.

Resume only when the original operation (INI migration or fresh initialization), role, and absolute paths are known from the installation context. The installer log may not contain the inner admission command; do not infer the operation from a missing database or guess between the two commands. Repeat only the known original operation. For the standard Pi installation, an interrupted migration from the standard original INI uses:

```sh
sudo wsprrypi --migrate-state \
  --state-directory /var/lib/wsprrypi/application-state \
  --ini-source /usr/local/etc/wsprrypi.ini
```

Keep the original `--ini-source` path even if retirement already moved that file to its `.sqlite-migrated` backup. The backend resumes its admitted private snapshot; do not recreate or edit the old INI to make the command succeed. Earlier preparation still requires the unchanged original source. A mismatch remains a refusal requiring investigation.

For an interrupted fresh initialization, repeat its original `--initialize-state --state-directory /absolute/original/state` command instead. Preserve `--controller-only` if it was part of either original operation. These commands validate and resume the existing admission; they are not permission to create replacement state for an established installation. Do not switch operation, remove generations, or select another directory to bypass an error.

After the original admission succeeds, rerun the installer to finish listener publication and service packaging. If the original operation cannot be established or resume is refused, preserve the reported state and request recovery assistance; a generic installer rerun alone cannot repair that condition.

## Diagnostic settings export

```sh
sudo wsprrypi --diagnostic-export
```

This read-only administrator command reports supported settings, advanced values, storage/hold status, and observed listener ports through the backend. It excludes raw databases, credentials, and inactive recovery evidence. A changing export or unavailable backend returns an explicit unavailable document and exit status 3, rather than partial settings or guessed defaults. Treat a successful export as private station information; use the [reviewed support-bundle workflow](../User_Interface/Maintenance/support_bundle.md) for sharing diagnostics.
