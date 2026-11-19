# Calibration and Transmitter Backends

Use these sections for frequency calibration and RF output-path settings. See [Configure Transmitter](../../User_Interface/Setup/Transmitter/index.md), [Configure Device I/O](../../User_Interface/Setup/Pi_IO/index.md), [Transmission Timing and Calibration](../timing_calibration.md), [Transmitter Backend Options](../../Command_Line_Operations/transmitter_backends.md), and [RF and Electrical Reference](../rf_electrical.md) for the corresponding workflows.

(calibration-section)=
## Calibration

The `[Calibration]` section supplies **Reference calibration (PPM)** for the Si5351 backend. GPIO calibration uses the separate values in `[GPIO]`.
Si5351 models `reference_hz * (1 - PPM / 1000000)`; do not copy GPIO's
correction sign or intrinsic/estimate terms into this setting.

```{literalinclude} default_wsprrypi.ini
:language: ini
:start-at: [Calibration]
:end-before: [GPIO]
```

(gpio-section)=
## GPIO

The `[GPIO]` section configures the supported direct RF pin, GPIO-backend power level, provider-derived system clock estimate, conducted residual, and fixed/manual fallback. When `Operation.Transmit Backend = gpio`, the configured transmit pin is reserved even if `Operation.Transmit = false`. The other supported transmit pin remains available to ordinary GPIO roles. When the Si5351 backend is selected, a retained GPIO transmit-pin value reserves nothing.

GPIO qualification depends on the Raspberry Pi clock profile, band, and
transmission mode. Requests for unqualified combinations are blocked by default,
while combinations the backend cannot construct remain unavailable. Check the
[Band qualification](../../About_Wsprry_Pi/index.md#band-qualification) table
and its numbered notes for the current mode-specific status. See
[GPIO Band Capabilities and Signal Quality](../../FAQ/why_12m_looks_noisy.md)
for the measured signal-quality findings.

The estimate/residual/manual values describe additional correction. The backend
adds its intrinsic chipset compensation once, including when additional PPM is
zero. A usable estimate selects estimate plus residual; otherwise manual applies.
A prior-qualified host estimate can remain usable within its bounded 900-second age
window even when current qualification is unavailable. Saved inputs do not change
already committed work. See [calibration accounting](../timing_calibration.md).

On Pi 1–4, `Use System Clock Frequency Estimate = True` applies Chrony's
host-frequency estimate to GPIO RF output. GPS/PPS is optional and belongs
to the OS time-source configuration; WsprryPi has no direct PPS capture or
PPS-input GPIO setting for these hosts. Chrony can also use network time
sources. See {ref}`Pi 1–4 host-frequency calibration <pi1-4-host-frequency-calibration>`.

`Use Direct PPS Calibration = True` selects the optional Pi 5/RP1 measurement
against an existing `pps0` input on GPIO17. It defaults to `False`. It replaces
the host frequency estimate for RP1 while retaining that separate saved
preference. Direct measurements need three stable ten-second observations,
expire after 30 seconds, and do not use the host estimate's 900-second
holdover. Unavailable acquisition selects `Manual PPM`. Qualify the reference
and review any existing residual before enabling it; see
{ref}`direct PPS prerequisites and operation <direct-pps-calibration-on-pi-5>`.

```{literalinclude} default_wsprrypi.ini
:language: ini
:start-at: [GPIO]
:end-before: [Si5351]
```

(si5351-section)=
## Si5351

The `[Si5351]` section configures the I2C device, reference frequency, reference hardware, transmit output, and drive strength. `Reference Source = external_tcxo` is the compatibility default for an active clock or TCXO. Select `crystal` only when a passive crystal is connected across XA/XB.

`I2C Address` accepts decimal or `0x`-prefixed hexadecimal values from `0x60`
through `0x6F` inclusive. The web interface further limits its address menu to
register-compatible devices detected on the selected, host-present I2C bus.
Direct CLI and INI configuration still undergo range and transmission-readiness
validation.

Cached or failed discovery can retain a saved unconfirmed address. A fresh scan
is explicit and bounded; see the [I2C address workflow](../../User_Interface/Setup/Transmitter/index.md#i2c-address).
Drive levels 1–4 retain 2/4/6/8 mA, not calibrated RF power. CW fades are
full-drive duty-cycle chopping with event deadlines, not analog amplitude control.

For a passive crystal, `Crystal Load Capacitance` accepts only `6`, `8`, or `10` pF and defaults to `10`. WsprryPi programs this value only in crystal mode. It retains the setting without applying it in `external_tcxo` mode, so TCXO users should not treat it as a calibration control.

```{literalinclude} default_wsprrypi.ini
:language: ini
:start-at: [Si5351]
:end-before: [WSPR]
```


(wtp-section)=
(pico-wtp)=
## Pico management

A Pico runs its own saved schedules. Save its management profile in
**Setup → Fleet**, then choose it under **Device**. USB management uses interface
4, with Console on 0 and Logging on 6. Interfaces 2/3 are reserved and inert in
application images. The optional RFBench image uses them for its bench commands.

Use encrypted Consumer Wi-Fi management with the Pico’s password, or explicitly
configured Engineering HTTPS with certificate and hostname verification. There
is no WTP execution carrier or automatic security fallback. Preserve explicit
hostnames, ports, USB serials, device IDs, and credential references when editing
profiles. A display name is not identity.

### Saved devices and the active endpoint

Saved profiles select management connections. They never choose this Pi’s RF
output or grant transmission ownership. Use each device’s native schedule controls.

### After a Pico hostname change

Read the saved and active names. A saved name may require a deliberate restart.
Update the connection destination only after checking the full device ID.
Engineering HTTPS must still match its provisioned certificate identity; a DNS
hint or new hostname does not replace certificate verification.

### Pico standalone configuration

Read current settings, review the device and boot, save the replacement schedule
disabled, and read it back. Enable it explicitly only after reviewing target
readiness and authority. Preserve drafts after a refused or unknown save. See
[Add a Pico](../../Install/pico.md) and
[native stop](../../User_Interface/index.md#local-control-and-remote-ownership).
