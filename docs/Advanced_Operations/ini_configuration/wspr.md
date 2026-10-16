# WSPR Settings

Use this section for WSPR station identity, reported power, frequency, transmission planning, and random offset. For the complete message-type and pairing workflow, see [Configure WSPR](../../User_Interface/Setup/Signal_Setup/wspr.md). Direct command-line users should also see [General and WSPR Options](../../Command_Line_Operations/wspr_options.md); frequency accuracy is covered in [Transmission Timing and Calibration](../timing_calibration.md).

<!-- if-wsprrypico -->
The planning preferences on this page belong to the **Pi host**. Pico member
station defaults use [Pico automatic planning](../../User_Interface/Setup/Transmitter/index.md#pico-automatic-wspr-planning),
which selects Type 1 for an ordinary six-character locator, a Type 2/3 pair for
a supported compound with six characters, and a single Type 3 for explicit
brackets with six characters. No Pi preference selector changes that automatic
member plan. Prepared WTP jobs retain their supplied finite plan.
<!-- endif-wsprrypico -->

(wspr-section)=
## WSPR

The `[WSPR]` section accepts standard, compound, and extended callsigns;
Maidenhead locators; transmit power in dBm; bare or qualified WSPR presets;
numeric USB dial frequencies; the frequency profile; per-band preferences; one
of the documented planner preferences; and optional random offset. See
[Canonical Bands and WSPR Frequency Presets](../canonical_bands.md) before
choosing a country/locality convention or editing `Band Preferences` directly.
`Band Preferences` accepts a quoted built-in preset for the same band or a
positive integral numeric USB dial frequency. A numeric preference changes the
meaning of the bare band name; a number in `Frequency` changes only that plan
entry. Preferences do not create aliases or replace canonical envelopes.

Examples:

```ini
; Keep the selected profile generally, but pin bare 60m to WRC-15.
Band Preferences = {"60m":"60m:wrc15"}

; Supply local dial defaults for configured-only 8m and 5m.
Band Preferences = {"8m":40680000,"5m":60000000}

; Remove every per-band override.
Band Preferences = {}
```

The object must remain on one line. JSON strings and numbers retain their types
when loaded and saved. Existing preset-only configurations require no migration.

```{literalinclude} default_wsprrypi.ini
:language: ini
:start-at: [WSPR]
:end-before: [CW]
```
