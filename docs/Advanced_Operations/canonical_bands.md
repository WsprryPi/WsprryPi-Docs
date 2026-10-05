(canonical-bands-and-wspr-presets)=
# Canonical Bands and WSPR Frequency Presets

WsprryPi uses two related frequency concepts:

- A **canonical band** correlates a numeric frequency with one stable band name.
  WsprryPi uses that result for Band GPIO/filter selection and transmitter
  qualification decisions in WSPR, QRSS, FSKCW, and DFCW modes.
- A **WSPR preset** converts a WSPR-only name such as `20m` or `60m:wrc15`
  into a USB dial frequency.

These are capability and convenience features. They are not a regulatory
database and do not establish whether an operator may transmit on a frequency.
Check the current licence, national allocation, band plan, emission rules,
power limit, and unattended-operation rules that apply at the station.

## Canonical band catalog

The catalog covers ordinary amateur allocations from 2200 m through 70 cm that
exist in at least one jurisdiction. Its envelopes intentionally accommodate
worldwide allocations and can therefore contain gaps or frequencies that are
not available in a particular country.

| Canonical name | Correlation envelope | Built-in WSPR preset |
| --- | ---: | ---: |
| `2200m` | 130–190 kHz | 136,000 Hz |
| `630m` | 472–479 kHz | 474,200 Hz |
| `160m` | 1.8–2.0 MHz | 1,836,600 Hz |
| `80m` | 3.5–4.0 MHz | 3,568,600 Hz |
| `60m` | 5.25–5.45 MHz | Profile-dependent; see below |
| `40m` | 7.0–7.3 MHz | 7,038,600 Hz |
| `30m` | 10.1–10.15 MHz | 10,138,700 Hz |
| `20m` | 14.0–14.35 MHz | 14,095,600 Hz |
| `17m` | 18.068–18.168 MHz | 18,104,600 Hz |
| `15m` | 21.0–21.45 MHz | 21,094,600 Hz |
| `12m` | 24.89–24.99 MHz | 24,924,600 Hz |
| `10m` | 28.0–29.7 MHz | 28,124,600 Hz |
| `8m` | 40–45 MHz | None |
| `6m` | 50–54 MHz | 50,293,000 Hz |
| `5m` | 54,000,001–68,000,000 Hz | None |
| `4m` | 69.9–70.5 MHz | 70,091,000 Hz |
| `2m` | 144–148 MHz | 144,489,000 Hz |
| `1.25m` | 219–225 MHz | 222,100,000 Hz |
| `70cm` | 420–450 MHz | 432,300,000 Hz |

All envelope endpoints are inclusive. Exactly 54 MHz correlates to `6m`; `5m`
begins at the next integral hertz so one frequency cannot have two identities.
The compatibility aliases `lf` and `mf` are accepted for `2200m` and `630m`,
but WsprryPi reports the canonical names. `22m` is not an amateur-band
identity and is rejected rather than remapped.

The catalog does not imply that the entire envelope was tested. Qualification
records apply the project's representative-frequency evidence to the
correlated band, backend, hardware profile, and mode. An unqualified
combination may be blocked even when the frequency correlates successfully.

## Choose a WSPR frequency input

Enter one or more values in **Setup → Signal → WSPR → Frequencies**, separated
by spaces or commas:

- Use a bare preset such as `20m` for the selected frequency profile's default.
- Use a qualified preset such as `60m:wrc15` when the exact convention must not
  change with the profile.
- Use an integral numeric USB dial frequency such as `14095600` when a built-in
  preset does not represent the required local convention.
- Use `0` to skip that position in a multi-frequency plan.

WSPR presets and numbers entered here are USB dial frequencies. WsprryPi adds
the WSPR audio offset when it plans the RF tones. A **Custom RF frequency** in
Test Tone is different: it is the emitted carrier frequency and receives no
WSPR offset.

Frequency selection follows this order:

1. Explicit numeric frequency
2. Explicit qualified preset
3. Saved per-band preference
4. Selected frequency profile
5. Built-in Existing/Common default

Changing the profile therefore does not rewrite numeric entries, qualified
presets, or a saved per-band preference.

## 60 m presets and profiles

60 m currently has two qualified WSPR presets. Both correlate to the one
canonical `60m` band.

| Preset | USB dial frequency | Purpose |
| --- | ---: | --- |
| `60m:legacy` | 5,287,200 Hz | Retains WsprryPi's established bare-`60m` behavior |
| `60m:wrc15` | 5,364,700 Hz | Selects the WRC-15-oriented WSPR convention |

The **Frequency profile** control determines the meaning of a bare `60m`:

| Frequency profile | Bare `60m` resolves to |
| --- | --- |
| **Existing/Common** | `60m:legacy` |
| **WRC-15** | `60m:wrc15` |

Open **Band preferences** when a bare band name should differ from the selected
profile or built-in default. In the `60m` row, choose **Preset**, then
`60m:legacy` or `60m:wrc15`. Choose **Default** to follow the frequency profile.
The preference affects only a bare `60m`; an explicit `60m:legacy`,
`60m:wrc15`, or numeric frequency remains unchanged.

## Band preferences in detail

`Band Preferences` pins the meaning of a bare WSPR band preset without changing
the selected profile. A value can select a built-in preset for the same band or
assign a positive integral USB dial frequency. Only 60 m currently has multiple
built-in presets; numeric preferences support local conventions on any
correlated band.

The INI value is a JSON object written on one line:

```ini
Band Preferences = {"60m":"60m:legacy"}
```

Each entry has these rules:

- The key is a canonical band name such as `60m`.
- The value is either a quoted, built-in preset identifier that resolves inside
  the same canonical band or a positive integral USB dial frequency written as
  a JSON number.
- A 60 m value must be qualified: use `60m:legacy` or `60m:wrc15`, not bare
  `60m`.
- `{}` removes all per-band overrides, so bare presets follow the selected
  frequency profile.
- A preference changes only a bare occurrence of its key in `Frequency`.
  Qualified presets and numeric frequencies remain explicit.

For example:

```ini
[WSPR]
Frequency = 60m, 60m:wrc15, 5364700
Frequency Profile = wrc15
Band Preferences = {"60m":"60m:legacy"}
```

The three entries resolve, in order, to 5,287,200 Hz, 5,364,700 Hz, and
5,364,700 Hz. The saved preference overrides the profile for the first bare
`60m`; it does not rewrite the qualified or numeric entries.

These examples are invalid:

```ini
Band Preferences = {"60m":"20m"}
Band Preferences = {"60m":"5364700"}
Band Preferences = {"20m":5364700}
```

The first resolves to a different canonical band, the second is a numeric value
encoded as a string instead of a preset, and the third correlates the assigned
frequency to `60m` rather than its `20m` key. An invalid preference prevents
that configuration from being applied instead of silently falling back.

`Band Preferences` does not redefine canonical band envelopes and cannot create
new named presets. A numeric preference reassigns a bare band name while an
integral number entered directly in `Frequency` affects only that occurrence.
Both forms are correlated to a canonical band for filter selection and
qualification.

For example, this makes every bare `60m` entry use a locality-specific dial
frequency while leaving qualified and explicit numeric entries unchanged:

```ini
Band Preferences = {"60m":5379500}
```

The Setup page provides the same workflow: open **Band preferences**, select
**Custom** for `60m`, enter `5379500`, and review the effective dial and RF
previews. **Clear** removes that one override. Valid changes save automatically;
an invalid or empty custom value remains visible and blocks autosave until it is
fixed or cleared.

### 8 m and 5 m

`8m` and `5m` are canonical correlation bands but have no built-in WSPR dial
preset. A bare `8m` or `5m` is therefore unavailable until assigned a numeric
band preference:

```ini
Band Preferences = {"8m":40680000,"5m":60000000}
```

After configuration, bare `8m` and `5m` entries resolve through scheduling and
appear in the effective WSPR/Test Tone catalog. The numeric dial must correlate
back to the matching envelope. This is capability configuration, not an
operating authorization.

## Country and locality guidance

WsprryPi does not infer a country from an IP address, callsign, or locator, and
it does not currently provide country-named profiles. Select the closest
built-in convention, then use a named preset or numeric per-band preference for
the locality-specific exceptions that should follow a bare band name.

### Continuous WRC-15 allocation

**Use:** **WRC-15** profile, or explicit `60m:wrc15`.

Use this only where the country implements the continuous 5,351.5–5,366.5 kHz
allocation and permits the intended WSPR operation. The preset's WSPR tones
fall within that continuous allocation.

### Established 5,287,200 Hz convention

**Use:** **Existing/Common**, or explicit `60m:legacy`.

Use this where the applicable WSPR plan specifically identifies the 5,287,200
Hz USB dial convention. It preserves WsprryPi's established behavior; the
name `legacy` is not a country authorization.

### United States

**Use:** No built-in country preset.

US 60 m access is channelized, and ARRL guidance says automatic operation is
not permitted. Do not treat `60m:legacy` or `60m:wrc15` as a US preset.

### United Kingdom

**Use:** No built-in country preset.

The UK uses multiple bandlets and its current usage plan identifies a separate
WSPR segment. Neither built-in preset represents that plan.

### Other channelized, bandlet-based, or nationally different plans

**Use:** An integral numeric USB dial frequency, if the intended operation is
permitted.

A numeric entry preserves the exact local convention without inventing a
country preset.

This guidance is a selection aid, not a list of countries authorized on 60 m.
National implementations and operating conditions change. Consult the
[ARRL 60 m channel information](https://www.arrl.org/60m-channel-allocation),
the [current RSGB band plan](https://rsgb.org/main/operating/band-plans/), or
the appropriate national society and regulator before configuring a station.

### Examples

Keep the compatibility profile but pin 60 m to WRC-15 in the web interface:

1. Set **Frequency profile** to **Existing/Common**.
2. Open **Band preferences**, set `60m` to **Preset**, and select
   `60m:wrc15 — 5,364,700 Hz`.
3. Enter `60m` in **Frequencies**.

Pin different conventions in one plan without changing preferences:

```text
20m, 60m:legacy, 60m:wrc15
```

Use an exact local USB dial frequency that has no built-in preset:

```text
5379500
```

The numeric example demonstrates input syntax only. Verify the actual local
frequency and operating conditions before transmitting.

## Direct INI configuration

The same controls are stored in the `[WSPR]` section:

```ini
[WSPR]
Frequency = 60m
Frequency Profile = existing_common
Band Preferences = {"60m":"60m:wrc15"}
```

`Band Preferences` is a JSON object on one line. Keys are canonical bands and
values are either quoted built-in preset identifiers for the same band or
positive integral numeric USB dial frequencies. An empty object (`{}`) means
every bare preset follows the selected profile or built-in default. See
[Band preferences in detail](#band-preferences-in-detail) for validation rules,
precedence, and examples.

## Migration notes

- Existing configurations without `Frequency Profile` continue to use
  `existing_common`.
- Missing or empty `Band Preferences` preserves historical bare-band behavior.
- Existing preset-string preferences remain valid and keep their JSON type.
- Numeric preferences are additive; no conversion of existing INI files is
  required.
- The former dedicated 60 m control is now the `60m` row in **Band
  preferences**. Clearing it removes only the `60m` entry.
- `22m` remains rejected. `8m`, `5m`, `1.25m`, and `70cm` are canonical band
  names, but only `8m` and `5m` require custom dial preferences before they can
  be used as bare WSPR presets.
