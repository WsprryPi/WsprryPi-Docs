# Configure WSPR

Use this page for WSPR station identity, transmission planning, frequency, power reporting, and calibration. Return to the [Signal Setup overview](index.md) to choose another mode. For calibration procedures, see [Transmission Timing and Calibration](../../../Advanced_Operations/timing_calibration.md); for output hardware, see [Configure Transmitter](../Transmitter/index.md).

WSPR or Weak Signal Propagation Reporting is the original mode for WsprryPi. The controls described below appear in the **WSPR** half of the signal-mode selector. Configuration saves automatically after each valid change.

The planning preferences on this page belong to the **Pi host**. Pico member station defaults use [Pico automatic planning](../Transmitter/index.md#pico-automatic-wspr-planning), which selects Type 1 for an ordinary six-character locator, a Type 2/3 pair for a supported compound with six characters, and a single Type 3 for explicit brackets with six characters. No Pi preference selector changes that automatic member plan. Prepared WTP jobs retain their supplied finite plan.

## Station Identity

Within the Station identity section, you will set your callsign and locator. For normal Type 1 WSPR messages, the callsign is any valid 6-character or fewer. The Grid Locator is the four- character Maidenhead locator for where you are transmitting.

If you need or desire to use callsign extensions, have a callsign longer than 6 characters, or want or need to use a six-character locator, you will need to consider using Type 2 or 3 messages.

### WSPR Transmission Type Selection Examples

| Callsign | Locator | Meaning | Allowed/Required Transmission |
| --- | --- | --- | --- |
| `AA0NT` | `EM18` | Standard callsign with 4-character locator | Type 1 single-frame |
| `AA0NT` | `EM18IG` | Standard callsign with 6-character locator | Type 1/3 paired transmission should be used if full 6-character locator reporting is required |
| `<AA0NT>` | `EM18` | Explicit Type 3 callsign with 4-character locator | Not useful; Type 3 is intended for extended locator or hashed callsign use |
| `<AA0NT>` | `EM18IG` | Explicit Type 3 callsign with 6-character locator | Type 1/3 paired transmission |
| `W0/AA0NT` | `EM18` | Compound/prefixed callsign with 4-character locator | Type 2 single-frame |
| `W0/AA0NT` | `EM18IG` | Compound/prefixed callsign with 6-character locator | Type 2/3 paired transmission |
| `<W0/AA0NT>` | `EM18IG` | Explicit Type 3 form of compound/prefixed callsign | Type 2/3 paired transmission |
| `AA0NT/P` | `EM18` | Compound/suffixed callsign with 4-character locator | Type 2 single-frame |
| `AA0NT/P` | `EM18IG` | Compound/suffixed callsign with 6-character locator | Type 2/3 paired transmission |
| `<AA0NT/P>` | `EM18IG` | Explicit Type 3 form of compound/suffixed callsign | Type 2/3 paired transmission |

#### Rule Summary

- A normal callsign with a 4-character locator uses **Type 1**.

    ```text
    AA0NT EM18
    ```

- A normal callsign with a 6-character locator requires a **Type 1/3 pair** to remain self-identifying.

    ```text
    AA0NT EM18
    <AA0NT> EM18IG
    ```

- A compound, portable, or prefixed callsign with a 4-character locator uses  **Type 2**.

    ```text
    W0/AA0NT EM18
    AA0NT/P EM18
    ```

- A compound, portable, or prefixed callsign with a 6-character locator requires a **Type 2/3 pair**.

    ```text
    W0/AA0NT EM18
    <W0/AA0NT> EM18IG
    ```

    ```text
    AA0NT/P EM18
    <AA0NT/P> EM18IG
    ```

- Angle brackets request an explicit **Type 3** callsign frame.

    ```text
    <AA0NT>
    ```

This should not make pairing invalid. Instead, when paired transmission is required, the planner should choose the appropriate companion frame:

- Standard inner callsign: **Type 1/3 pair**
- Compound inner callsign: **Type 2/3 pair**

## WSPR Transmission Plan

These settings govern the way that WSPR is transmitted or received.

### Frequencies

The Frequencies setting accepts one value or a list separated by spaces or commas. Use a bare WSPR preset such as `20m`, a qualified preset such as `60m:legacy` or `60m:wrc15`, an integral numeric USB dial frequency, or `0` to skip a position. Optional `@GPIO`, `@GPIOH`, and `@GPIOL` suffixes select Band GPIO behavior for an entry.

They may also be listed in engineering notation where these are all the same:

- 50MHz
- 0.05GHz
- 50000kHz
- 50000000Hz

Notice that there are no spaces between the number and `m` for meters, and none between the number and the engineering notation.

The frequency may also be listed in pure integral Hz, such as `21094600`.

The WSPR USB dial is `D`; the RF center is `C = D + 1500 + r`, where `r` is optional random placement. Tone `k` is `Fk = C + (k - 1.5) × 1.46484375 Hz`, for `k = 0, 1, 2, 3`. The fixed 1,500 Hz placement is the project convention. With the standard `20m` preset and no random placement:

| Reference | Frequency (Hz) |
| --- | ---: |
| USB dial | 14,095,600 |
| RF center | 14,097,100 |
| Tone 0 | 14,097,097.802734375 |
| Tone 1 | 14,097,099.267578125 |
| Tone 2 | 14,097,100.732421875 |
| Tone 3 | 14,097,102.197265625 |

Test Tone uses one steady carrier rather than four WSPR tones. The web **WSPR band → 20m** selection and CLI `--test-tone 20m` each target `14,097,100 Hz`. Numeric `--test-tone 14095600` targets exactly `14,095,600 Hz`; numeric and unit-suffixed Test Tone inputs specify the carrier directly. Test Tone never adds random placement. These are requested synthesis targets; measure RF independently.

 Using a bare band preset selects the current frequency profile's WSPR dial convention. **Frequency profile** defaults to **Existing/Common** for compatibility. The initial alternate profile is **WRC-15**; it changes only the meaning of a bare `60m`. Open **Band preferences** to choose **Default**, **Preset**, or **Custom** independently for every canonical band. Each row shows the effective USB dial and RF center / Test Tone target without random placement. **Clear** removes only that band's override. Valid edits save automatically; invalid custom values remain visible and block autosave until corrected or cleared. Explicit qualified presets and numeric values entered in **Frequencies** never change when the profile changes.

The `8m` and `5m` rows have no built-in WSPR preset. Select **Custom** and enter a positive integral USB dial frequency inside the corresponding correlation envelope before using either bare name. Configured values then participate in scheduling and the effective WSPR/Test Tone catalog.

WsprryPi does not infer a country. See [Canonical Bands and WSPR Frequency Presets](../../../Advanced_Operations/canonical_bands.md) for the complete band and preset tables, country/locality guidance, configuration precedence, and examples.

### Random offset

Turning this switch on will add a positive or negative random offset to the transmitted frequency.  This can be handy when there is a lot of traffic on WSPR, and allow you to find a more clear slice of the available bandwidth.

### Reported Power

Reported power is not the same as the actual transmission power.  The transmitters settings may be attenuated by the LPF and additional gain may be added. Possible values are:

`0, 3, 7, 10, 13, 17, 20, 23, 27, 30, 33, 37, 40, 43, 47, 50, 53, 57, 60`

dBm is added to the encoder WSPR message to be a reference for the decoded message.  The operator should choose the value that is closest to their actual transmission power.

This setting has no bearing on actual transmission power.

### Frequency calibration (PPM) & NTP Calibration

Some operators may choose to manually calibrate their rig.  This is more important with GPIO-based transmissions where the Raspberry Pi frequencies may be impacted by power, heat, and mechanical differences.

Others may opt for the simpler and "accurate enough" NTP calibration.  This uses an internet time source to calibrate the output frequency.  For most bands, this is more than reasonable.  Some operators on higher bands such as 6m and 2m may find even a small deviation puts them out of the transmission boundaries, and may need to use a calculated PPM adjustment.

When NTP is enabled, the Frequency Calibration field is dithered.  When using the Si5351 clock module, NTP is disabled and manual calibration should be used - although the combination of a TCXO and the Si5351 is often so close, it may be ignored.

In all cases, NTP will continue to keep the Pi in sync to time messages appropriately.

### Planning Mode

Planning mode relates to the use of Type 1, 2, and 3 messages, and the behavior when certain data elements are entered.

- **Automatic** - The planner attempts to choose the best transmission plan based on the data entered.
- **Prefer paired when available** - If the planner finds it can generate both Type 2 and 3 messages, it will do so in alternating windows.
- **Require paired** - Requires the planner to always use a paired Type 2 and 3 message format.  For those who want the additional data to be received and understood by even the most remote stations under challenging conditions, this is likely the best choice.