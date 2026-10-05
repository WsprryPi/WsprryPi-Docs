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

When a usable provider estimate is available, the effective GPIO correction is:

```text
effective GPIO PPM = system clock estimate PPM + residual PPM
```

The residual is not a replacement for the provider estimate. Measure it through a conducted, suitably attenuated RF path after the provider estimate has qualified. Provider qualification confirms the clock-rate estimate is usable; it does not prove that the transmitted RF is calibrated.

WsprryPi qualifies the estimate before using it:

- **Qualified** means current samples are stable and meet the provider checks. WsprryPi uses the current estimate plus **Residual PPM**.
- **Converging** means the current estimate is not yet stable. If a previously qualified estimate is available, WsprryPi latches that value and adds **Residual PPM**; otherwise it uses **Fixed/manual PPM** when nonzero.
- **Stale** means the last qualified estimate is older than the current-sample limit but remains within the permitted stale window. WsprryPi uses that latched estimate plus **Residual PPM**.
- **Unavailable** means no usable provider sample is available. WsprryPi uses **Fixed/manual PPM** when nonzero; otherwise it transmits without a frequency correction and reports the uncalibrated state.

Chrony may use NTP servers, GNSS, PPS, or a mixture of sources. The administrator owns that source configuration outside WsprryPi. See the official [chronyc documentation](https://chrony-project.org/doc/4.4/chronyc.html) for the `tracking` data that supplies the current frequency estimate, residual frequency, source identity, age, and uncertainty information.

Existing configurations that contain the retired `GPIO.Use NTP` key are actively migrated when saved. WsprryPi maps the legacy value to `GPIO.Use System Clock Frequency Estimate`, adds the new GPIO calibration keys when absent, and removes `GPIO.Use NTP`. New configuration writes and web requests must use the new keys.

#### GPIO calibration workflow

1. Configure and verify the system time provider independently. Allow its clock-rate estimate to settle.
2. Enable **System clock estimate** and confirm the runtime status is **Qualified**.
3. Set **Residual PPM** to `0`, transmit a low-power test tone through a shielded 50-ohm load, suitable filtering, and attenuation, and measure the RF error with a receiver using a shared or traceable reference.
4. Convert the remaining error to PPM and enter it as **Residual PPM**. Keep **System clock estimate** enabled.
5. Repeat the conducted measurement across multiple samples. Confirm the combined correction improves both frequency accuracy and repeatability.
6. Record a separately measured **Fixed/manual PPM** if operation without a usable provider estimate is required.

Frequency calibration matters because WSPR occupies a narrow band. The Raspberry Pi reference crystal has both static error and temperature-dependent drift. Recheck the residual after meaningful hardware, temperature, power-supply, or reference-source changes.

### Interpreting Test Tone Measurements

Use the final requested RF carrier as the nominal frequency for a current Test
Tone measurement. The Maintenance page's **WSPR band** choice adds the displayed
WSPR offset to the dial frequency; **Custom RF frequency** already specifies RF.
An explicit numeric `--test-tone` value also specifies RF directly. Apply that
conversion once, and keep receiver calibration separate from transmitter PPM.
The displayed or reported carrier is a synthesis target, not a measurement.

When reviewing older records, identify the exact executable version used. Legacy
GPIO builds before the [test-tone frequency correction](https://github.com/WsprryPi/WsprryPi/commit/ef9a76a5be4d8223b89bcd64df1e1a376d48a0a5)
nominally emitted Test Tone **2.197265625 Hz below the requested RF frequency**,
before oscillator error and any hardware-limit adjustment. For those affected
measurements, compare the retained raw frequency with
`requested RF - 2.197265625 Hz`, accounting separately for any reported hardware
adjustment. Reassess a GPIO PPM value derived from such a tone before reusing it
with a corrected build.

The displacement is fixed in hertz, so its apparent PPM changes with frequency.
Do not absorb it into a universal clock correction or apply it again to a
corrected build. It does not apply to Si5351 or RP1 Test Tone, or to the configured
QRSS, FSKCW, and DFCW carriers. WSPR intentionally transmits four tones centered
around the requested WSPR RF frequency.

### Si5351-Based Transmissions

The Si5351 reference is independent of the Raspberry Pi system clock estimate
and GPIO calibration values. Switch **Setup > Transmitter > RF Output Path** to
Si5351, then configure **Reference calibration (PPM)** in the same RF Output
panel. WsprryPi applies that value only to Si5351 synthesis planning.

Measure the Si5351 correction against its actual crystal or external reference through a suitable conducted RF path. Do not copy the GPIO estimate, GPIO residual, or GPIO fixed/manual value into the Si5351 setting.

### AM Calibration

A practical manual method is to tune the transmitter near a medium-wave AM broadcast station, zero-beat the signal, and calculate the remaining frequency error from the known station frequency.

Suppose your local AM station is at 780 kHz. Use `--test-tone` to produce nearby tones, such as `780100`, until you achieve zero beat. If the zero-beat tone on the command line is `F`, calculate the correction as `ppm=(F/780000-1)*1e6`. You can then supply that value with `--ppm` on future transmissions.
