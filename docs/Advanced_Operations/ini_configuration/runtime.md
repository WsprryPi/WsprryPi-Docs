# Runtime and Service Settings

Use these sections for process behavior, active transmission mode, service ports, transmission gating, and shared control GPIOs. For normal browser-based configuration, see [Setup Overview](../../User_Interface/Setup/index.md). Related operator references include [Configure Raspberry Pi I/O](../../User_Interface/Setup/Pi_IO/index.md), [REST API](../rest_api.md), [WebSocket Interface](../websocket.md), and [View Logs](../../User_Interface/Logs/index.md).

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

The `[Security]` section controls privileged network-location access. This is
separate from ordinary Setup autosave.

```{literalinclude} default_wsprrypi.ini
:language: ini
:start-at: [Security]
:end-before: [Operation]
```

`enforced` is the default and recommended value. Missing, empty, malformed,
boolean-like, numeric, or unknown values also fail closed to enforced behavior
and produce a warning. Only the exact value `insecure-disabled` bypasses the
peer/subnet check for protected operations. It does not weaken Host, Origin,
CORS, malformed-request, method, command, forwarded-header, or ordinary
configuration validation.

Use the [Privileged Network Safety](../../User_Interface/Maintenance/network_safety.md)
panel to change this value through the validated Apache apply/reload transaction.
Do not edit it through normal Setup autosave.

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

`Allow Unqualified Frequency` permits a backend, hardware profile, band, and
mode combination whose recorded state is **Untested** or **Unqualified**. It
cannot make an **Unavailable** hardware plan usable. `Allow Non-Amateur
Frequency` additionally permits a frequency outside WsprryPi's recognized
amateur-band ranges, but only when `Allow Unqualified Frequency` is also
`true`.

These controls do not grant permission to transmit. The operator remains responsible for authorization, RF-path safety, filtering, and compliance with applicable rules.

When the process starts with `--ini-file`, WsprryPi loads these INI values
before processing the remaining CLI switches. A CLI `--allow-*` or `--no-*`
switch overrides the corresponding INI value at startup and does not rewrite
this file. Repeated switches are processed from left to right, so the last
occurrence wins. If a later change to this monitored file is accepted, the
reloaded INI values become the live settings for subsequent transmission
decisions. See [Experimental Frequency Policy](../../Command_Line_Operations/transmitter_backends.md#experimental-frequency-policy)
for concrete commands and the procedure for confirming the effective settings
of a running process.

### Startup transmitter safety

`Enable on Boot` determines whether WsprryPi requests transmission after the daemon starts. Independently of that policy, every daemon start first attempts to place the configured transmitter backend in a disabled state. The Si5351 backend disables all clock outputs. The GPIO backend stops its DMA and clock path and returns the configured transmit GPIO to an input state.

If that startup operation fails, WsprryPi keeps the web and socket services available but inhibits WSPR scheduling, CW scheduling, manual launches, startup tones, and test tones. The inhibition is latched for the lifetime of the process and does not change the saved `Transmit` or `Enable on Boot` values.

To recover, correct the reported hardware or configuration problem and restart the WsprryPi service. A configuration reload or transmission toggle cannot clear the startup inhibition. See [Configuration Troubleshooting](../configuration_troubleshooting.md#startup-transmission-is-inhibited) for operator checks.

This protection begins when the daemon runs. Use a separate hardware inhibit when the transmitter must remain disabled during the earlier power-up and operating-system boot interval.

<!-- if-wsprrypico -->
## WTP Server

The managed Pi listener uses these defaults:

```ini
[WTP Server]
Enabled = true
Port = 31417
Interface = auto
```

`Enabled` controls inbound WTP admission. It does not enable local RF or an
outbound Fleet schedule. `Port` accepts `1` through `65535`.
`--wtp-server-port` overrides it for one process without changing the saved INI.
Direct one-shot CLI transmissions do not start the managed listener or Fleet.

`Interface = auto` requires exactly one operational physical LAN IPv4 address.
With multiple eligible addresses, specify an interface such as `eth0` or
`wlan0`. Only private RFC1918 addresses on up/running physical interfaces are
eligible; Wi-Fi must be in station mode. Loopback, bridges, tunnels, access-point
interfaces, and public addresses are excluded. The listener retries after
interface recovery. Address loss withdraws its DNS-SD advertisement. A settings
or route change waits for current ownership/work to end and suspends admission
of new remote jobs while pending.

The listener defaults to active after confirmed startup quiescence. Local
Enable off permits a claim only when output is safe and idle. Local Enable on
reserves the local output even between jobs; the listener still permits
inspection but refuses claims. `Enable on Boot` remains the local startup
policy. Listener admission and each outbound assignment remain independent.

An external INI transaction enabling local transmission immediately cancels
remote-controlled work and revokes future assignments. The browser's confirmed
**Let it finish** transaction is recognized on file reload and retains that
choice. See [local takeover](../../User_Interface/index.md#local-control-and-remote-ownership)
for the interactive choices and output-unknown recovery.

Avahi publishes `_wtp._tcp.local.` with the actual port and `binding=plain`.
Discovery failure does not remove the direct listener. Pi inbound WTP uses
unencrypted Plain LAN with the shared `local-network` principal; TLS is not
implemented for this listener. Outbound TLS profiles for compatible Pico
servers remain available, with no automatic fallback to Plain LAN.

### Persistent ownership and assignments

The process user's private `~/.wsprrypi-wtp/revocation-v1` journal preserves
local takeover history. Keep it across restarts and use a consistent service
user. An unreadable or malformed journal inhibits admission; deleting it can
erase takeover history.

`<active-INI-path>.wtp-assignments.json` stores independent remote schedules,
consumed slots, and unresolved dispatch state. It is separate from
`<active-INI-path>.wtp-devices.json`, which stores connection profiles, and from
`[WTP]`, which selects the single-endpoint backend. Manage assignments through
Fleet or its [HTTP resource](../rest_api.md#pi-endpoint-and-fleet-resources).
After interrupted work, reconcile the affected output before resuming it.
<!-- endif-wsprrypico -->
