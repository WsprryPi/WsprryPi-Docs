# Runtime and Service Settings

Use these sections for process behavior, active transmission mode, service ports, transmission gating, and shared control GPIOs. For normal browser-based configuration, see [Setup Overview](../../User_Interface/Setup/index.md). Related operator references include [Configure Device I/O](../../User_Interface/Setup/Pi_IO/index.md), [REST API](../rest_api.md), [WebSocket Interface](../websocket.md), and [View Logs](../../User_Interface/Logs/index.md).

(meta-section)=
## Meta

The `[Meta]` section controls diagnostic logging.

```{literalinclude} default_wsprrypi.ini
:language: ini
:start-at: [Meta]
:end-before: [Security]
```

(security-section)=
## Security

The `[Security]` section controls privileged network-location access. This is separate from ordinary Setup autosave.

```{literalinclude} default_wsprrypi.ini
:language: ini
:start-at: [Security]
:end-before: [Operation]
```

`enforced` is the default and recommended value. Missing, empty, malformed, boolean-like, numeric, or unknown values also fail closed to enforced behavior and produce a warning. Only the exact value `insecure-disabled` bypasses the peer/subnet check for protected operations. It does not weaken Host, Origin, CORS, malformed-request, method, command, forwarded-header, or ordinary configuration validation.

Use the [Privileged Network Safety](../../User_Interface/Maintenance/network_safety.md) panel to change this value through the validated Apache apply/reload transaction. Do not edit it through normal Setup autosave.

(operation-section)=
## Operation

The `[Operation]` section selects the active mode and backend, gates RF transmission, configures service ports, and assigns shared indicator, amplifier, and shutdown controls.

```{literalinclude} default_wsprrypi.ini
:language: ini
:start-at: [Operation]
:end-before: [Experimental]
```

(experimental-frequency-section)=
## Experimental frequency policy

The `[Experimental]` section provides advanced CLI/INI-only controls for operators performing authorized experiments. These settings are intentionally absent from the Web UI and default to `false`.

```{literalinclude} default_wsprrypi.ini
:language: ini
:start-at: [Experimental]
:end-before: [Calibration]
```

`Allow Unqualified Frequency` permits a backend, hardware profile, band, and mode combination whose recorded state is **Untested** or **Unqualified**. It cannot make an **Unavailable** hardware plan usable. `Allow Non-Amateur Frequency` additionally permits a frequency outside WsprryPi's recognized amateur-band ranges, but only when `Allow Unqualified Frequency` is also `true`.

These controls do not grant permission to transmit. The operator remains responsible for authorization, RF-path safety, filtering, and compliance with applicable rules.

When the process starts with `--ini-file`, WsprryPi loads these INI values before processing the remaining CLI switches. A CLI `--allow-*` or `--no-*` switch overrides the corresponding INI value at startup and does not rewrite this file. Repeated switches are processed from left to right, so the last occurrence wins. If a later change to this monitored file is accepted, the reloaded INI values become the live settings for subsequent transmission decisions. See [Experimental Frequency Policy](../../Command_Line_Operations/transmitter_backends.md#experimental-frequency-policy) for concrete commands and the procedure for confirming the effective settings of a running process.

### Startup transmitter safety

`Enable on Boot` determines whether WsprryPi requests transmission after the daemon starts. Independently of that policy, every daemon start first attempts to place the configured backend in a disabled state. Si5351 attempts immediate all-output inhibition before ordinary programming. Legacy GPIO stops DMA/clock and returns the configured transmit GPIO to input; RP1 uses its provider's ownership and route reconciliation. Software disable/write/readback evidence is distinct from an independent RF-off measurement.

If that startup operation fails, WsprryPi keeps the web and socket services available but inhibits WSPR scheduling, CW scheduling, manual launches, startup tones, and test tones. The inhibition is latched for the lifetime of the process and does not change the saved `Transmit` or `Enable on Boot` values.

To recover, correct the reported hardware or configuration problem and restart the WsprryPi service. A configuration reload or transmission toggle cannot clear the startup inhibition. See [Configuration Troubleshooting](../configuration_troubleshooting.md#startup-transmission-is-inhibited) for operator checks.

This protection begins when the daemon runs. Use a separate hardware inhibit when the transmitter must remain disabled during the earlier power-up and operating-system boot interval.

Saved edits and repair/reset can defer runtime application while a Test Tone owns its committed backend, mode, frequency, and selectors. Saving does not replace that running snapshot or clear cleanup uncertainty. Read [Test Tone results and recovery](../../User_Interface/Maintenance/index.md#read-the-result) before treating saved settings as active.

(wtp-server)=
## Retired WTP configuration

`backend=wtp`, inbound WTP listeners, and `--wtp-server-port` are unsupported. An active legacy backend or enabled listener holds execution with a migration required message. There is no automatic local-backend fallback.

Inactive `[WTP]` and `[WTP Server]` values may remain in an existing INI. Their presence alone does not block a valid native configuration, and unrelated saves preserve meaningful dormant values. They are private legacy state, not current settings controls. Use an explicit reviewed configuration change after migration.

### Persistent ownership and assignments

Preserve the process user’s private ownership/revocation journals, protected management and retirement records, `<active-INI-path>.wtp-assignments.json`, `.wtp-fleet-contexts.json`, and `.wtp-devices.json`. Assignment records retain consumed slots and uncertain work; device profiles retain connection settings. Read-only legacy records never authorize reconnect or replay. Deleting history cannot establish cleanup. Follow [remote WTP retirement](../../User_Interface/Maintenance/index.md#retire-remote-wtp-work-before-upgrading) with WTP-capable software before replacing a deployment that still has duties.


## Native recurrence and time readiness

Enable scheduling, solar selection, Transmit, Enable on Boot, and output ownership are independent. Scheduling off prevents new occurrences and permits an accepted complete WSPR pair or message to finish. It does not release the output to a WTP client. A solar wait also retains the reservation established by Transmit. Immediate Stop remains separate from scheduling disable.

Enable on Boot applies to Transmit: Never starts with permission off, Follow uses the saved permission, and Always requests it on. These choices preserve the scheduling and solar flags. Always cannot restart a disabled schedule. Existing startup quiescence, takeover, and output-unknown safeguards still apply.

With solar selection off, native recurrence uses the ordinary mode settings without added solar time or site prerequisites. With solar on, the transmitter uses its saved locator center and target-local UTC. A qualifying morning/evening window takes precedence over day/night permissions. Both starts of a paired WSPR occurrence must select the same allowed policy and frequency intent; otherwise the whole pair waits. An accepted occurrence keeps its frozen frequency and random placement through a later solar boundary.

The supported solar clock provider is read-only Linux OS time discipline. It requires synchronized time, no leap/clock alarm, kernel maximum error plus acquisition uncertainty at most 250 ms, and a date from 2025 through 2099. After a healthy sample in this boot, bounded holdover can last up to one hour while estimated uncertainty remains at most 250 ms; it grows by 50 microseconds per second. Unavailable health, an alarm, a clock step, or suspend/resume can hold new work or invalidate preparation. This trusts the configured OS clock; it is not a UTC accuracy measurement or RF calibration. Platforms without that provider hold solar recurrence; ordinary solar-off operation remains available.

Explicit period WSPR lists rotate independently. Inherited periods share the ordinary list. Policy refusal does not advance a list; an explicit skip consumes one normal slot, and a complete pair advances once. Restart, backward time steps, and re-enabling cannot replay a consumed occurrence. Missed slots are not queued. An uncertain interrupted occurrence requires safe output reconciliation; its reserved progression can be consumed conservatively even if no RF occurred. Missing or damaged established progress holds admission. Preserve recovery files and investigate storage errors instead of deleting history.

Management connections do not transfer schedule ownership. Each selected transmitter uses its own native recurrence and solar policy. Next-start forecasts are bounded to 48 hours and 4,096 candidates and may be unknown. Neither a countdown nor a forecast proves that a transmission occurred.

## Scheduling editor

[Setup → Scheduling](../../User_Interface/Setup/Scheduling/index.md) manages the same target-owned scheduling and solar values through protected, revision-bound saves. It saves a disabled policy, confirms readback, then requires explicit enablement. Do not edit private authority or recovery files to bypass initialization, ownership, or unknown-operation holds. Disabled periods retain values and remain validated.
