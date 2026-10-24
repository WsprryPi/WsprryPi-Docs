# Transmission Timing and Calibration

Use these procedures when transmission timing or RF frequency accuracy needs direct attention beyond normal web UI operation.

## Transmission Timing

WsprryPi uses wall-clock time to determine the start of WSPR transmissions, so keep the system clock synchronized to within one second. A WSPR transmission starts on an even UTC minute and runs for about two minutes.

Wall-clock synchronization and GPIO frequency calibration are related but distinct. Synchronization keeps UTC time correct. A system clock frequency estimate describes the rate error of the Raspberry Pi clock in parts per million (PPM). WsprryPi can use that rate estimate to correct GPIO RF frequency.

## Frequency Calibration

### GPIO-Based Transmissions

The GPIO backend has three separate calibration values in **Setup > Transmitter > GPIO Output > Frequency calibration**:

- **System clock estimate** enables a provider-derived estimate of Raspberry Pi clock-rate error. WsprryPi currently supports chrony.
- **Residual PPM** is the remaining conducted RF error measured while the provider estimate is active.
- **Fixed/manual PPM** is the fallback used when the provider estimate is disabled or cannot be used.

The UI and committed request report the **additional** correction. The GPIO backend adds its intrinsic chipset compensation once:

```text
usable current/prior-qualified estimate: additional A = estimate E + residual R
otherwise:                              additional A = fixed/manual M
manual zero:                            additional A = 0
RF divider model: nominal parent * (1 + (intrinsic I + additional A) / 1000000)
```

Residual is unused in manual/zero mode; manual is not added to an estimate. Zero additional correction retains intrinsic compensation. Current defaults are BCM2835: -2.5 ppm; BCM2836/BCM2837 and BCM2711: 0 ppm; RP1: -46.245 ppm. These are product defaults with their recorded evidence limits, not individual board measurements. RP1 uses nominal **200 MHz pll_sys**; the historical 50 MHz XOSC planning assumption is not the current RF parent contract.

Positive GPIO additional PPM models a fast source: the larger calculated divider lowers physical RF. Each configured GPIO correction input and selected additional term must be finite and within `-200` through `200 ppm`. The intrinsic term is separate. No live estimate or composed total is persisted as a custom correction.

#### Qualification and retained estimates

Read estimate qualification and selected correction mode separately:

- **Qualified**: synchronized, selected-source, normal-leap and quality checks pass, with at least three stable evaluations (spread at most 0.1 ppm), at least three retained provider samples, skew at most 1 ppm and absolute Chrony residual-frequency statistic at most 0.5 ppm. Current reported age must be known and at most 300 seconds. These evaluations do not prove independent PPS samples or RF accuracy.
- **Converging**, **Stale**, or **Unavailable**: a previously qualified estimate can still supply bounded stale correction plus **Residual PPM**, even if the current report is unavailable. Its qualification-time reported age plus monotonic elapsed time must remain within 900 seconds. An old first observation cannot qualify itself; source changes reset qualification history.
- Without a usable current or retained estimate, use **Fixed/manual PPM**. A zero manual value selects zero additional correction and reports the uncalibrated additional state. Disabling the estimate also selects manual.

Missing/malformed age remains **age unknown**, not zero. Cached reports accrue elapsed age before selection for future work. Source provenance considers only selected/combined Chrony records and their local/network modes. Names containing PPS, GPS or GNSS, unselected sources, and a local-reference label do not establish verified GNSS lock, reference routing or independent RF measurement. Mixed means local and network source kinds were combined; unknown provenance remains unknown. Chrony's residual-frequency quality statistic is not the configured conducted **Residual PPM** and must not be added as another correction.

#### Candidate and committed correction

Candidate correction describes the next preparation decision. Committed work retains its selected correction, clock plan and provenance for its lifetime. New estimates, source loss, expiration and saved configuration changes affect future work; they do not rewrite the immutable committed request. The operation panel's effective/correction PPM fields are additional-only, with provenance.

Chrony may use NTP servers, GNSS, PPS, or a mixture of sources. The administrator owns that source configuration outside WsprryPi. See the official [chronyc documentation](https://chrony-project.org/doc/4.4/chronyc.html) for the `tracking` data that supplies the current frequency estimate, residual frequency, source identity, age, and uncertainty information.

Existing configurations that contain the retired `GPIO.Use NTP` key are actively migrated when saved. WsprryPi maps the legacy value to `GPIO.Use System Clock Frequency Estimate`, adds the new GPIO calibration keys when absent, and removes `GPIO.Use NTP`. New configuration writes and web requests use the canonical keys. An existing canonical value takes precedence during migration. Saved custom correction values are not silently rewritten to compensate for a changed baseline.

#### GPIO calibration workflow

1. Configure and verify the system time provider independently. Allow its clock-rate estimate to settle.
2. Enable **System clock estimate** and confirm the runtime status is **Qualified**.
3. Set **Residual PPM** to `0`, transmit a low-power test tone through a shielded 50-ohm load, suitable filtering, and attenuation, and measure the RF error with a receiver using a shared or traceable reference.
4. Convert the remaining error to PPM and enter it as **Residual PPM**. Keep **System clock estimate** enabled.
5. Repeat the conducted measurement across multiple samples. Confirm the combined correction improves both frequency accuracy and repeatability.
6. Record a separately measured additional **Fixed/manual PPM** if operation without a usable current or retained estimate is required. Disable the estimate when measuring this fallback, while retaining intrinsic compensation.

A residual measures what remains with intrinsic compensation and the estimate already applied. Do not enter a measured full parent error again as a residual. If an independent measurement gives full source error `P`, reconcile it as `M = P - I` or `R = P - I - E`. For example, a historical RP1 total correction of `-46.245 ppm` corresponds to zero additional correction under the current intrinsic default. Review older custom settings explicitly; the application does not rewrite them. Correct receiver/SDR error once in the measurement path.

Frequency calibration matters because WSPR occupies a narrow band. The Raspberry Pi reference crystal has both static error and temperature-dependent drift. Recheck the residual after meaningful hardware, temperature, power-supply, or reference-source changes.

### Interpreting Test Tone Measurements

Use the final requested RF carrier as the nominal frequency for Test Tone measurements. Both Maintenance's **WSPR band** selection and CLI `--test-tone 20m` add 1,500 Hz to the effective USB dial, targeting `14,097,100 Hz` with the standard 20m preset. Custom RF and numeric or unit-suffixed CLI inputs specify the carrier directly: `--test-tone 14095600` targets `14,095,600 Hz`. Test Tone never uses random placement. Apply the dial conversion once and keep receiver calibration separate from transmitter PPM. An accepted synthesis target is not a measured output frequency.

When reviewing older records, identify the exact executable version used. Legacy GPIO builds before the [test-tone frequency correction](https://github.com/WsprryPi/WsprryPi/commit/ef9a76a5be4d8223b89bcd64df1e1a376d48a0a5) nominally emitted Test Tone **2.197265625 Hz below the requested RF frequency**, before oscillator error and any hardware-limit adjustment. For those affected measurements, compare the retained raw frequency with `requested RF - 2.197265625 Hz`, accounting separately for any reported hardware adjustment. Reassess a GPIO PPM value derived from such a tone before reusing it with a corrected build.

The displacement is fixed in hertz, so its apparent PPM changes with frequency. Do not absorb it into a universal clock correction or apply it again to a corrected build. It does not apply to Si5351 or RP1 Test Tone, or to the configured QRSS, FSKCW, and DFCW carriers. WSPR intentionally transmits four tones centered around the requested WSPR RF frequency.

### Si5351-Based Transmissions

The Si5351 reference is independent of the Raspberry Pi system clock estimate and GPIO calibration values. Its planner uses `reference_hz * (1 - calibration_ppm / 1000000)`: positive Si5351 calibration reduces the modeled reference, unlike positive GPIO PPM. Switch **Setup > Transmitter > RF Output Path** to Si5351, then configure **Reference calibration (PPM)** in the same RF Output panel. WsprryPi applies that value only to Si5351 synthesis planning.

Measure the Si5351 correction against its actual crystal or external reference through a suitable conducted RF path. Do not copy the GPIO estimate, GPIO residual, or GPIO fixed/manual value into the Si5351 setting.

### Remote transmitter correction

A remote transmitter owns its own frequency correction. Outbound jobs carry no Pi-host estimate, intrinsic or manual correction. A receiving Pi selects its local correction before preparing its plan. Host UTC synchronization is still needed for scheduling, independently of the remote RF clock.

### AM Calibration

Zero-beating a nearby AM carrier can provide a rough manual comparison when its frequency is independently known. It is not a substitute for an identified, calibrated RF reference. Record the backend, current correction, requested RF frequency and comparison frequency before changing a value.

If a GPIO tone requested at `F` zero-beats a known carrier `F_ref`, the approximate additional adjustment is `(F_ref / F - 1) * 1000000 ppm`, added to the correction already active during that comparison. A positive result means the output was fast. For Si5351, the reference-calibration adjustment has the opposite sign. Recheck through the conducted RF path; do not copy a full correction between backends or count intrinsic compensation twice.

Chrony remains the UTC/slot authority. Administrator-configured PPS may support Chrony timing and estimates; WsprryPi 4.0 adds no direct PPS RF calibration or alternative RP1 clock-parent experiment. Host timestamps do not independently measure the RF clock.