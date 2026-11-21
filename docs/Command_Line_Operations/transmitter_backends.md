# Transmitter Backend Options

## Backend Selection

- `--backend <gpio\|si5351\|rp1-gpclk>`
  Select RF output method.  
  - `gpio`: Direct RF from Raspberry Pi GPIO (limited models).  
  - `si5351`: External clock generator via I2C.
  - `rp1-gpclk`: Explicit Pi 5 RP1 backend with a reconciled installed route and the existing operation-scoped development confirmation. It is never an automatic fallback from `gpio`; see the [RP1 guide](../Advanced_Operations/rp1_gpclk.md).

- `--power-level <level>`  
  Set transmit power for the active backend:  
  - GPIO: 0–7  
  - Si5351: 1–4

- `--gpio-power-level <0-7>`  
  Explicitly set GPIO drive strength.

- `--si5351-power-level <1-4>`  
  Set Si5351 output drive strength.

## Experimental Frequency Policy

These advanced options are available from the direct command line and saved local settings command. They are intentionally not exposed in the Web UI, and both default to disabled.

- `--allow-unqualified-frequency`, `--no-allow-unqualified-frequency` Allow or deny a backend, hardware profile, band, and mode combination whose recorded state is **Untested** or **Unqualified**. This option cannot enable an **Unavailable** output that the selected backend cannot safely construct.

- `--allow-non-amateur-frequency`, `--no-allow-non-amateur-frequency` Allow or deny a frequency outside WsprryPi's recognized US and international amateur-band ranges. Outside-band transmission requires both allow options.

These options do not grant permission to transmit. The operator remains responsible for authorization, RF-path safety, filtering, and compliance with applicable rules.

### Precedence

Saved experimental settings use the [local settings command](saved_settings.md). Direct CLI switches affect the current invocation without rewriting saved values; repeated switches are processed left to right, so the last occurrence wins. Active `--ini-file` startup and monitored reload are retired.

With an authorized frequency and a suitable attenuated, filtered RF path or dummy load, this command permits an Untested or Unqualified combination on a recognized amateur band for the current process:

```bash
sudo wsprrypi --allow-unqualified-frequency --test-tone 137500Hz --backend gpio
```

A frequency outside WsprryPi's recognized amateur-band ranges requires both positive switches:

```bash
sudo wsprrypi --allow-unqualified-frequency --allow-non-amateur-frequency \
  --test-tone 30000000Hz --backend si5351
```

The second command still fails if the selected backend cannot construct the requested output safely. To deny outside-band operation for a direct invocation, use `--no-allow-non-amateur-frequency`.

The last occurrence controls the effective value. This example leaves the unqualified-frequency override enabled and the non-amateur-frequency override disabled:

```bash
sudo wsprrypi --allow-unqualified-frequency \
  --allow-non-amateur-frequency --no-allow-non-amateur-frequency \
  --test-tone 137500Hz --backend gpio
```

### Confirm the active settings

Use `sudo wsprrypi --settings read` for saved and active advanced values from the running backend, or `sudo wsprrypi --diagnostic-export` for the supported diagnostic view. For a direct CLI run, also inspect the launching command and its last-occurrence overrides. A support bundle uses validated settings export rather than copying the INI or live database. These controls are not ordinary Setup controls and do not establish operating authority.

---

## GPIO Backend

GPIO qualification depends on the Raspberry Pi clock profile, band, and transmission mode. A band can be qualified for TONE, QRSS, FSKCW, or DFCW while WSPR remains unqualified. Requests for unqualified combinations are rejected before GPIO activation unless the experimental override is enabled; unavailable combinations remain blocked. Check the current [Band qualification](../About_Wsprry_Pi/index.md#band-qualification) table and its numbered notes before transmitting.

A steady test tone is not sufficient evidence that WSPR modulation will decode. See [GPIO Band Capabilities and Signal Quality](../FAQ/why_12m_looks_noisy.md) for the underlying signal-quality findings.

- `--transmit-gpio <4\|20>`  
  Select GPIO pin used for RF output.

- `--transmit-pin <4\|20>`  
  Legacy alias for transmit GPIO.

- `-n`, `--use-system-clock-frequency-estimate` Enable the qualified Chrony-derived system clock frequency estimate.

- `--no-system-clock-frequency-estimate` Disable both automatic sources for this invocation and select GPIO manual PPM.

- `-p`, `--gpio-manual-ppm <value>` Set additional manual correction (`-200` through `200 ppm`) and disable both automatic estimates. `--ppm` remains an accepted compatibility alias.

- `--gpio-frequency-residual-ppm <value>` Set the conducted residual added only to a usable current or bounded prior-qualified estimate (`-200` through `200 ppm`).

Explicitly selecting the host estimate also disables direct PPS for that invocation. Direct PPS is enabled through `GPIO.Use Direct PPS Calibration` in saved configuration through the corresponding Setup control; these CLI choices do not rewrite its saved preference. See {ref}`direct PPS calibration <direct-pps-calibration-on-pi-5>`.

Positive GPIO PPM models a fast source. Intrinsic chipset compensation remains applied once even with manual zero. Manual is a fallback, not an additional term on top of the estimate. See [calibration accounting](../Advanced_Operations/timing_calibration.md) when setting a correction.

---

## Si5351 Backend

Levels 1–4 select retained 2/4/6/8 mA drive, not calibrated RF power. Discovery, initialization, runtime readiness, and successful cleanup are separate checks. Keep output disabled after a fault, establish ownership/quiescence, and resolve any uncertain cleanup before another deliberate transmission. Recovery does not resume interrupted work automatically. See [Si5351 readiness and recovery](../User_Interface/Setup/Transmitter/index.md#readiness-and-recovery).

- `--si5351-ppm <value>` Set backend-local reference calibration (`-200` through `200 ppm`). The modeled reference is `reference_hz * (1 - ppm / 1000000)`; GPIO's sign and correction terms do not apply.

- `--si5351-i2c-bus <bus>`  
  Select I2C bus (default: 1).

- `--si5351-i2c-address <addr>`  
  Set the device address in decimal or `0x`-prefixed hexadecimal. Valid
  addresses are `0x60` through `0x6F` inclusive.

- `--si5351-reference-frequency <hz>`  
  Define reference oscillator frequency.

- `--si5351-reference-source <external_tcxo|crystal>` Select an active external clock/TCXO or a passive crystal. Missing settings default to `external_tcxo`.

- `--si5351-crystal-load-capacitance <6|8|10>` Set the internal load capacitance used only with `--si5351-reference-source crystal`. The default is 10 pF.

- `--si5351-tx-output <CLK0\|CLK1\|CLK2>`  
  Select output clock. This option is not exposed in the Web UI.


(pico-wtp-backend)=
## Pico management and native schedules

`--backend wtp` is retired. A Pico is managed through Fleet or its own browser and runs its own saved schedule. Choose a native backend for transmissions produced by this Pi. Neither a missing device nor a failed legacy connection selects a different output automatically.

(pi-wtp-server-capability)=
## Retired inbound execution

The Pi exposes no WTP listener or `_wtp._tcp` advertisement. Device-owned recurrence, local stop, management pairing, and recovery use the selected device’s native management controls.
