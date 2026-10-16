# Calibration and Transmitter Backends

Use these sections for frequency calibration and RF output-path settings. See [Configure Transmitter](../../User_Interface/Setup/Transmitter/index.md), [Configure Raspberry Pi I/O](../../User_Interface/Setup/Pi_IO/index.md), [Transmission Timing and Calibration](../timing_calibration.md), [Transmitter Backend Options](../../Command_Line_Operations/transmitter_backends.md), and [RF and Electrical Reference](../rf_electrical.md) for the corresponding workflows.

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
A prior-qualified estimate can remain usable within its bounded 900-second age
window even when current qualification is unavailable. Saved inputs do not change
already committed work. See [calibration accounting](../timing_calibration.md).

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


<!-- if-wsprrypico -->
(wtp-section)=
## Pico WTP

Set `[Operation] Transmit Backend = wtp` to select a Pico on Linux. Keep
`Transmit = false` and `Enable on Boot = Never` while configuring and checking
the endpoint. The active `[WTP]` section remains the runtime's endpoint
authority. A missing `Transport` value means USB, preserving a valid legacy
configuration.

| Setting in `[WTP]` | Value and purpose |
| --- | --- |
| `Transport` | `usb` (default), `network_plain` (Plain LAN), or `network` (TLS). There is no automatic fallback between them. |
| `Endpoint` | For USB, the dedicated WTP device path under `/dev/`. Do not use the Console interface. |
| `USB Serial` | Exact USB serial string, including leading zeros. |
| `USB Vendor ID` / `USB Product ID` | Decimal USB identifiers, each from 1 through 65535 when USB is selected. |
| `Hostname` / `TCP Port` | For either network binding, the connection name or address and its actual port. DNS-SD uses the SRV port, which may differ from 31417. |
| `TLS Server Identity` | For TLS, the expected certificate name. Direct connections may use the configured hostname; a discovered TLS profile requires an explicit expected identity. |
| `TLS CA File` / `TLS Client Certificate` / `TLS Client Key` | Absolute paths to provisioned files on the WsprryPi host for TLS. The INI and catalog retain file references, not key contents. |
| `Device ID` | Expected 32-character lowercase hexadecimal WTP identity from HELLO. USB and TLS require it. A direct legacy Plain LAN endpoint may leave it blank and learn an identity for the current session, but a saved profile cannot be selected without a confirmed full ID. Plain LAN HELLO is not cryptographic authentication. |
| `Start Uncertainty ns` | Maximum permitted start uncertainty, from 1 through 1000000000 nanoseconds. Default: 1000000 (1 ms). |
| `Allow Frequency Adjustment` | Default: `false`. Permits reported realizable frequency rounding; it does not establish RF accuracy. |

Obtain identities from the intended device rather than copying another
board's values. USB identity, WTP device identity, TLS certificate identity,
and current boot identity serve different checks. A hostname, DNS-SD instance
label, or Plain LAN HELLO alone does not establish trusted identity.

The host requires synchronized UTC with at most 500 ms reported maximum error.
The Pico separately needs valid UTC within the configured start-uncertainty
budget and its own clock limits. Raising the budget is an explicit acceptance
decision, not clock calibration or proof of start accuracy.

Set host `[Calibration] PPM = 0.0`. Disable TX LED, amplifier, shutdown-button,
and band-selector GPIO controls, including per-frequency `@` selectors. CW fades
are unsupported. Settings for inactive GPIO and Si5351 backends are retained.
Unresolved WTP work blocks endpoint or backend replacement until its state is
resolved.

### Saved devices and the active endpoint

When the hidden Fleet development pane is enabled for a session, it keeps a
private, versioned catalog at `<INI-path>.wtp-devices.json`. The catalog holds
named USB, manual-network, and DNS-SD profiles with host-side TLS file
references. First access imports the currently selected valid `[WTP]` settings
without changing them. A saved profile may remain listed while its discovery
advertisement is absent.

Independent Fleet schedules use separate assignments; see
[Output schedules](../../User_Interface/Setup/index.md#assign-an-output-schedule).
A catalog profile is a connection record, not a schedule.

Adding, renaming, editing, or removing a profile does not change `[WTP]`.
**Use this device** is the explicit action that applies a saved profile through
the normal host configuration path. It requires transmission to be disabled
and the current runtime to be safely replaceable. If writing the INI fails,
the old active endpoint remains selected. If the write succeeds but runtime
application cannot be confirmed, read the current configuration and Pico
status before any further operation. The catalog does not create a second
active endpoint setting.

A DNS-SD profile keeps its saved binding, target, and SRV port. A changed
advertisement requires explicit profile review and a fresh device identity
check before another selection. TLS must still validate its expected server
identity, credentials, and full WTP device ID. Plain LAN requires renewed
operator consent and never silently retargets. Configured manual endpoints
retain their normal direct connection behavior; failed discovery does not
disable them.

### Pico standalone configuration

The `[WTP]` INI settings select how this Pi connects to a device; Pico's saved
standalone station, Wi-Fi, and schedule settings are managed separately. When
Fleet development controls are visible, **Pico standalone settings and Wi-Fi**
uses the explicitly selected management carrier while the host and Pico are
idle. Engineering HTTPS retains the selected Network (TLS) certificate policy;
supported consumer station/AP management uses a separate volatile login. USB
and Plain LAN WTP do not themselves provide JSON administration. No persistent
management secret, new WTP authority or hardware-activation setting is added.

An ordinary settings save preserves supported settings outside the form,
including pins and advanced frequency-policy settings. Older firmware is used
only when its saved settings can be preserved safely; incompatible settings
cause refusal. Standalone settings may be saved before all changes are active,
and the reported restart requirement determines the next step.
Unknown fields refuse safely rather than being discarded. Explicit scoped
station/hardware saves use complete resources under the selected member's
revision/context, separately from the legacy atomic editor. They do not reset
unrelated settings, restart, claim, reconnect WTP or transmit.

See [Pico standalone settings and Wi-Fi](../../User_Interface/Setup/Transmitter/index.md#pico-standalone-settings-and-wi-fi)
for loading, password preservation, schedule-only saves, and recovery after a
conflicting or unconfirmed result. See
[Pico development controls](../../User_Interface/Setup/Transmitter/index.md#pico-development-controls)
for the Fleet workflow and job recovery. Keep transmission disabled until the
configuration, clock evidence, and intended RF path have been checked.
<!-- endif-wsprrypico -->
