# WebSocket Interface

The WebSocket interface provides:

- Runtime state broadcasts
- Browser UI synchronization
- Configuration reload notifications
- Transmission lifecycle events
- Test-tone state updates
- Real-time control integration

For normal browser use, connect through the proxied WebSocket path:

```text
ws://{servername}.local/wsprrypi/socket
```

The backend service receives this connection internally as:

```text
ws://127.0.0.1:31416/socket
```

When privileged network safety is enforced, Apache restricts the entire
browser-facing `/wsprrypi/socket` endpoint to clients on the Pi's directly
connected LAN. Apache cannot authorize individual commands after upgrade, so
off-LAN clients also lose read-only commands, ping/pong, and server broadcasts.
There is no separate off-LAN read-only socket.

Port `31416` is not a browser fallback. Compatible direct non-browser clients
must be on loopback or an eligible directly connected LAN, send a valid local
`Host`, and either omit `Origin` or send an `Origin` matching `Host`. Forwarded
client headers are ignored for authorization.

## Available Commands

Examples of supported commands include:

- `get_tx_state`
- `shutdown`
- `reboot`
- Runtime control and synchronization requests used by the browser UI

Privileged commands include `shutdown`, `reboot`, `stop`, `tone_start`,
and `tone_end`. The separate `bounded_tone` command is qualification-only and
is not a normal browser capability. Read-only protocol operations include
`get_tx_state`, `wspr_band_catalog`, `echo`, ping/pong, and server broadcasts.
This classification does not make read-only commands available off-LAN through
the protected browser-facing endpoint; the whole WebSocket connection is
restricted while enforcement is active.

Example request:

```json
{"command":"get_tx_state"}
```

Example response:

```json
{"tx_state":true}
```

On builds with the Pi 5 RP1 integration, `get_tx_state` also reports
requested/persisted/configured/active route fields,
`rp1_eligibility`, `rp1_cleanup_state`, and `rp1_journal_state`. Values such as
`unavailable`, `unknown`, and `none-reported` are intentional: clients must not
infer active hardware state from the configured route.

## Broadcast Events

As long as the socket remains connected, the server broadcasts runtime events to all connected clients.

### Configuration Reload

Broadcast when the active configuration changes:

```json
{
    "state":"reload",
    "timestamp":"2025-05-06T16:43:02Z",
    "type":"configuration"
}
```

### Transmission Start

Broadcast when a transmission begins:

```json
{
    "state":"starting",
    "timestamp":"2025-05-06T16:40:01Z",
    "type":"transmit"
}
```

### Transmission Complete

Broadcast when a transmission finishes:

```json
{
    "state":"finished",
    "timestamp":"2025-05-06T16:41:51Z",
    "type":"transmit"
}
```

### Transmission Cancelled

Broadcast when a transmission is stopped before completion:

```json
{
    "state":"cancelled",
    "timestamp":"2025-05-06T16:40:20Z",
    "type":"transmit"
}
```

### Test Tone State

Use the Maintenance [Test Tone workflow](../User_Interface/Maintenance/index.md#test-tone)
for operator actions. A custom RF Start request is:

```json
{"command":"tone_start","frequency_source":"custom_rf","frequency_hz":14097100,"client_request_id":"example-start-1"}
```

For a controller-authorized WSPR band, use `frequency_source: "wspr_band"`
and `band` instead of `frequency_hz`. The controller resolves dial plus WSPR
offset; a custom value already means RF. End uses:

```json
{"command":"tone_end","client_request_id":"example-end-1"}
```

`started=true` acknowledges acceptance and requested asynchronous startup, not
observed RF. `test_tone_status` broadcasts and `get_tx_state` include additive
`test_tone` metadata: process-local `generation`, increasing `revision`, `owned`,
`state`, `message` and `restoration`. States include starting, active, completed,
failed, cancelled, ended and unknown (idle before work). Active is controller
runtime evidence, never a frequency/power measurement. A terminal observation
can precede the Start reply; ignore older revisions and tolerate added fields.

Optional `client_request_id` (up to 128 characters) is echoed for correlation.
Reacquire evidence after reconnect; IDs/generations are not durable ownership.
A legacy uncorrelated reply cannot reliably settle a newer request. Preserve
conservative recovery controls after timeout, disconnect or uncertain cleanup.
Do not automatically retry a Start or End whose result is unknown.

End additionally reports `restoration_failed` and `output_inactive`.
`stopped=true` describes Test Tone cleanup, not a promise that all output is off:
restoration can return to scheduler flow, managed idle or a prior CLI direct
tone. Preserve restoration failure even when cleanup succeeded. A recovery End
can have `stopped=true`, `tone_was_active=false` without resuming prior work;
an inert inactive End can have both false. Cleanup uncertainty keeps further
output inhibited. Ordinary Stop fences restoration; saved edits/reload/repair
can defer runtime application until tone cleanup.

The browser UI relies heavily on these broadcasts for:

- Live status updates
- Modal synchronization
- Runtime control state
- Configuration refresh
- Multi-tab coordination
- Update notification behavior
