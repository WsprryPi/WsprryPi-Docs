# Saved Settings and INI Migration

The backend owns authoritative SQLite state for supported local configuration and Fleet management. Normal edits still use the existing [Setup pages](../User_Interface/Setup/index.md); advanced settings without UI controls use the validated [local settings command](../Command_Line_Operations/saved_settings.md). The browser process and CLI do not open the database directly. Do not edit SQL tables or copy a live database file as a backup.

## One-time migration

The SQLite implementation imports an existing INI once and retains the original as a `.sqlite-migrated` backup. The installer performs state admission and migration. After migration, changing the old INI does not change saved or active settings: there is no INI watcher, autosave, restart import, or fallback. Active `-i` / `--ini-file` startup is rejected. Preserve the migration backup and established application state.

Unknown migration fields are reported rather than activated. Use the exact canonical casing of supported names; an incorrectly cased replacement for a supported key is refused. Do not remove state directories to force migration again. An established database that is missing or corrupt requires recovery, not fresh initialization.

The references below describe canonical settings and the old INI import representation. INI examples are migration references, not files to maintain after migration. Installed defaults and valid values remain subject to current backend validation.

```{toctree}
:maxdepth: 1
:hidden:

Runtime and Service Settings <ini_configuration/runtime>
Calibration and Transmitter Backends <ini_configuration/transmitter_backends>
WSPR Settings <ini_configuration/wspr>
CW and Band GPIO Settings <ini_configuration/cw_and_band_gpio>
One-time INI Import Example <ini_configuration/complete_example>
```

## Configuration areas

- [Runtime and Service Settings](ini_configuration/runtime.md) covers diagnostic logging, network safety, mode, listener ports, transmission gating, and scheduling readiness.
- [Calibration and Transmitter Backends](ini_configuration/transmitter_backends.md) covers GPIO and Si5351 hardware settings.
- [WSPR Settings](ini_configuration/wspr.md) covers identity, frequency, reported power, planning, and random offset.
- [CW and Band GPIO Settings](ini_configuration/cw_and_band_gpio.md) covers timing, scheduling, fades, and band switching.
- [One-time INI Import Example](ini_configuration/complete_example.md) provides the import syntax; ordinary edits use Setup or the local settings command.

## Device-owned scheduling configuration

The backend stores the local Pi scheduling policy and coordinated operation receipts with its authoritative application state. Its `pi-scheduling` capability reports `next_occurrence`. Complete **Set up this transmitter** when required, then review the saved policy before explicitly enabling native recurrence. Saving solar settings does not enable scheduling, Transmit, or Enable on Boot. Use [Setup → Scheduling](../User_Interface/Setup/Scheduling/index.md) or the [protected target API](rest_api.md#local-pi-device-owned-scheduling) to edit the policy.

Keep application state, private identity/authority records, management journals, and recurrence progress together through the supported [backup and restore workflow](../User_Interface/Maintenance/backup_restore.md). Some companion journals retain their own persistent owners. Do not hand-edit or delete them to repair an error. Solar fields are not INI migration keys.

A draft has independent day and night permissions and optional morning and evening windows. Windows use integer millidegrees from −90000 to 90000, with a lower bound strictly below the upper bound. Defaults are −6000 and +6000. The lower bound is included and the upper bound excluded. The evaluator treats day as solar-center elevation at least −0.833°; a qualifying morning or evening window takes precedence over day/night policy. Null frequency overrides inherit the saved mode settings. WSPR overrides retain their list, skip entries, frequency profile, band preferences, and per-entry selector metadata. CW bases are positive decimal hertz with at most nine fractional digits; trailing fractional zeroes are omitted. FSKCW and DFCW use the saved positive CW shift, with both derived tones validated. Changed overrides are validated even when their period is disabled. Unchanged, well-formed values that a backend no longer supports can be retained for repair; retention does not qualify them for transmission.

The site is the center of the saved uppercase 4-, 6-, or 8-character Maidenhead locator. Native Pi GPS is unavailable. Saving a draft does not require time synchronization; actual solar admission requires healthy target-local UTC in 2025–2099. Geometry uses UTC without timezone or daylight-saving rules. See [native recurrence and time readiness](ini_configuration/runtime.md#native-recurrence-and-time-readiness) for the supported provider, uncertainty, holdover, and recovery behavior.
