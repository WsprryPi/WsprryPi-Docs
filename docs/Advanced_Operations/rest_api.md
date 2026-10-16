# REST API

WsprryPi exposes both an HTTP REST interface and a WebSocket interface for configuration, control, monitoring, and UI synchronization.

For persistent event and command connections, see {doc}`websocket`.

For normal browser and API use, access these interfaces through the Apache proxy path:

```text
http://{servername}.local/wsprrypi/
```

The WsprryPi backend still listens on its service ports internally:

- HTTP REST/UI backend: `31415`
- WebSocket backend: `31416`

Those ports are implementation details behind the proxy. Most users and documentation examples should use the proxied `/wsprrypi/` paths.

Apache is required for browser operation and uses the browser's actual peer
address for privileged network safety. Browser code does not fall back to the
direct backend ports for protected operations. Compatible direct non-browser
clients remain subject to peer, local `Host`, and optional matching `Origin`
validation. `Forwarded`, `X-Forwarded-For`, `X-Real-IP`, and similar headers do
not grant access.

The HTTP interface serves both the browser UI and the REST API through the proxied base path.

The UI entry point is:

```text
http://{servername}.local/wsprrypi/
```

## Configuration Endpoint

The primary proxied configuration endpoint is:

```text
http://{servername}.local/wsprrypi/config
```

Supported operations:

- `GET`: Returns host configuration and read-only platform observations as JSON;
  committed work can still use an earlier runtime snapshot.
- `PUT`: Replaces the configuration with a full JSON payload
- `PATCH`: Updates selected configuration fields

The backend service receives this request internally as:

```text
http://127.0.0.1:31415/config
```

The API exposes configuration for:

- WSPR Type 2/3 support
- QRSS, FSKCW, and DFCW configuration
- Si5351 backend configuration
- Band GPIO selector configuration
- Amp Control GPIO support
- Web and WebSocket port configuration
- CW timing and fade configuration
- Planner preferences and paired-frame behavior

The read-only `Platform` section of `GET /config` includes host I2C adapters
and cached compatible-address observations for the configured bus. Configuration
and status reads do not start discovery, including for inactive backends.
Unchecked presence remains unconfirmed. These observations are neither
persisted configuration nor client authority.

```text
GET /wsprrypi/config/si5351-addresses?bus=N
```

This read-only endpoint refreshes the compatible address list for a selected
host-present bus. Its JSON response contains `I2C Bus`, `Addresses`, and
`Discovery Error`. Address checks are limited to `0x60` through `0x6F` and do
not program the clock generator or enable an output. The isolated worker has
a two-second scan deadline and at most 25 ms of cleanup attempts, with one worker
outstanding. A kernel-blocked worker can remain pending after termination is
requested; further scans report busy until it exits. Busy, timeout/error and
confirmed no response are different outcomes. Failed inventory preserves a saved
address as unconfirmed; it does not establish missing hardware. Retry explicitly
after the worker/problem is resolved. Configuration updates independently perform
fresh validation of a newly selected bus/address rather than trusting this list.
A response establishes register compatibility, not definitive silicon identity.

Configuration replacement and patch requests apply the same GPIO ownership validation as startup and INI reload. With the GPIO backend, the selected GPIO4 or GPIO20 RF output cannot also be used by an enabled Band GPIO, Transmit LED, Shutdown Button, or Amp Control, regardless of the `Operation.Transmit` value. A rejected request returns the conflict instead of clearing or moving either assignment.

With privileged network safety enforced, `PUT` and `PATCH` require a browser
peer on the Pi's directly connected LAN. `GET /config` remains read-only and
available where practical. Repair/reset, stop-and-disable, support-bundle
operations, and `POST /api/network-safety` are also protected. An off-LAN
request is rejected before the operation is proxied.

A minimal host patch disabling transmission is:

```json
{"Operation":{"Transmit":false}}
```

Read `GET /wsprrypi/config` first and send its exact quoted ETag in `If-Match`
with `PATCH /wsprrypi/config`. The browser autosave does this; legacy clients
without a condition retain compatibility. A stale revision rejects the write;
preserve the draft and explicitly reload saved settings before another attempt.
Use the [INI reference](ini_configuration.md) for canonical keys. A saved edit
can await runtime application while a Test Tone owns the committed configuration.

## RP1 GPCLK Route Endpoint

Pi 5 route controls use the bounded same-origin endpoint:

```text
GET  /wsprrypi/api/rp1-gpclk-route
POST /wsprrypi/api/rp1-gpclk-route
```

`GET` is read-only and reports requested, persisted, configured, active,
eligible, generation, journal, service-restoration status, and operator state.
Detailed responses distinguish `qualificationEvidence`, `liveQualification` and
`structuralCompatibility` from readiness, application eligibility and output
inhibition. Evidence not collected is **Not inspected**; status does not download
metadata. See [RP1 diagnostics](rp1_gpclk.md#diagnostic-evidence) for cache refresh
and interpretation. The detailed diagnostic panel is hidden in the normal UI.

For the installed runtime route profile, `POST` accepts these fixed operations:

- `preflight` validates a GPIO4 or GPIO20 switch and returns the current
  transaction generation and plan digest.
- `switch` applies the preflighted GPIO4 or GPIO20 route in the current boot.
- `remove` removes the exact active GPIO4 or GPIO20 route and restores the
  prior WsprryPi service intent.
- `recover` performs exceptional fail-closed cleanup and leaves WsprryPi
  stopped and inhibited.

`switch` requires the current generation; the service binds that generation to
the reviewed preflight digest.
`remove` names the exact route being removed. A successful switch or removal
response means the bounded operation was queued; clients must poll `GET` until
the route reaches a terminal state. A temporary disconnect is not proof of
success. Normal removal finishes as route neutral with WsprryPi either online
and idle, or still stopped or masked because that was its prior state.

The compatibility development profile retains `preflight`,
`apply-and-reboot`, and `rollback`. Runtime requests are never translated into
reboot operations. Unknown operations, routes, stale generations, non-idle
state, foreign boot content, and ownership conflicts fail closed.

The endpoint never accepts a shell command, arbitrary path, overlay name, or
reboot command. Active or neutral state is not inferred until read-only status
reconciliation succeeds.

## Network Safety Endpoint

The Maintenance page uses:

```text
GET  /wsprrypi/api/network-safety
POST /wsprrypi/api/network-safety
```

`GET` is read-only and reports whether configured and active state are known,
their values when known, and the exact status text. `POST` is protected and
accepts one explicit mode:

```json
{"mode":"enforced"}
```

or:

```json
{"mode":"insecure-disabled"}
```

The apply response distinguishes whether the request was applied and reports
configured and active state. When disabled, status is exactly `NETWORK SAFETY
OFF`. A failed validation, publish, Apache reload, confirmation, or rollback
must be treated as failure; do not infer active state from the requested value.

## Version Endpoint

Version and update metadata are available through the proxied endpoint:

```text
http://{servername}.local/wsprrypi/version
```

The backend service receives this request internally as:

```text
http://127.0.0.1:31415/version
```

Modern versions expose structured metadata:

```json
{
    "wspr_version": "3.0.0-rc.4+abcdef0 (devel)",
    "ui_version": "3.0.0-rc.4+abcdef0 (devel)",
    "ui_build_id": "mtime-1234567890abcdef",
    "wspr_version_raw": "3.0.0-rc.4+abcdef0",
    "wspr_branch": "devel",
    "wspr_branch_state": "branch",
    "wspr_commit": "abcdef0123456789",
    "wspr_build_dirty": false
}
```

This endpoint is used for:

- Browser UI version display
- Automatic update polling
- UI build reload detection
- Asset cache busting
- GitHub update comparison logic

<!-- if-wsprrypico -->
## Pi endpoint and Fleet resources

Development Pi/Pico controls use the resources below. Paths are shown as the
backend receives them; browser requests prepend `/wsprrypi`, for example
`/wsprrypi/api/v1/host/wtp-endpoint`. The existing peer, Host, Origin, and
privileged-network guards apply. Browser writes use same-origin JSON intent
headers. These are local host-management resources; WTP job control uses the
separate TCP endpoint, default port `31417`.

- `GET /api/v1/host/wtp-endpoint`

  Listener, requested/effective local Enable, remote owner/job, output uncertainty, takeover generation, and launch observation.

- `POST /api/v1/host/wtp-endpoint/enable`

  Confirm target-local takeover using the current configuration `If-Match` revision.

- `POST /api/v1/host/wtp-endpoint/recover`

  Request local output reconciliation with `{"confirmed":true}`. Success requires confirmed inactive output.

- `GET /api/v1/host/fleet`

  Read assignments, per-output runtime observations, and the assignment ETag.

- `POST /api/v1/host/fleet`

  Change an assignment using its current `If-Match` revision. Operations: `assign`, `enable`, `pause`, `schedule`, `recover`, `remove`.

- `GET /api/v1/host/discovery`

  Read nearby DNS-SD observations without claiming a device.

- `GET/POST /api/v1/host/devices`

  Read or edit saved connection profiles; edits require the catalog `If-Match` revision.

- `POST /api/v1/host/discovery/identify`

  Perform explicit read-only identification of a selected candidate.

- `POST /api/v1/host/devices/use`

  Select a profile for the single `[WTP]` backend using the host config `If-Match` and body `catalog_revision`.

The takeover request contains `choice` (`end_now` or `finish_current`),
`confirmed`, `observed_owner`, and `observed_job`. Send the owner and job from
fresh endpoint status. If ownership or the job changes before confirmation,
the server requires renewed confirmation with fresh status. An unconfirmed
request does not change remotely owned state. The central controller has no
approval role. Both accepted choices revoke future assignments; finish-current
keeps effective local output inhibited until confirmed completion and output-off.

Direct `PUT` or `PATCH /config` writes explicitly setting
`Operation.Transmit=true` are noninteractive: they immediately cancel remote
work. An unrelated settings patch does not cancel a previously selected
finish-current choice. Use the dedicated takeover resource for an interactive
browser workflow.

Pi assignments use a target status HTTP port (default `31415`) as well as the
WTP port. A changed target takeover generation removes that assignment before
further dispatch, including after controller downtime. Network loss alone does
not remove an assignment or establish output-off. Failed or uncertain work
pauses that output pending reconciliation; consumed slots are not retried.

See [Fleet setup](../User_Interface/Setup/index.md#pi-and-pico-fleet-setup)
for operator actions and the
[application Fleet reference](https://github.com/WsprryPi/WsprryPi/blob/devel/docs/wtp-fleet.md)
for persistence and request contracts.

## Selected Pico application, station and hardware

These management resources belong to the selected member. They do not edit Pi
host settings or prepared jobs, and are separate from standalone schedule saves.
Use the normal Apache proxy:

```text
GET  /wsprrypi/api/v1/member/application
GET  /wsprrypi/api/v1/member/station
GET  /wsprrypi/api/v1/member/hardware
GET  /wsprrypi/api/v1/member/pins
PUT  /wsprrypi/api/v1/member/station
PUT  /wsprrypi/api/v1/member/hardware
POST /wsprrypi/api/v1/member/pins/validate
```

Each GET returns the same reconciled `wsprrypi-member-resources/1` bundle:
`target`, `carrier`, nullable `profile_generation`, `profile_owned_station`,
complete `application`, advertised `pin_choices`, and opaque `member_context`.
Application includes station, hardware, recurrence, capabilities and restart
observations. The adapter brackets resource reads with application readback and
checks the common saved revision. Live recurrence/active observations may change
independently. Preserve decimal uint64 strings as strings. Hardware
`active_revision` is an observation digest, never the save ETag.

### Versioned Pico station formats

The Pi browser paths above remain stable. The native adapter requires the exact
advertised `application_resources_v2` descriptor, together with its legacy
foundation, before selecting `transmitter-application/2`,
`transmitter-station/2` and `wspr_type123_auto`. It then uses Pico's exact
`/api/v1/application/2`, `/api/v1/station/2`, `/api/v1/config/2` and
`/api/v1/config/update/2` routes. Hardware remains `/api/v1/hardware`.
Unknown or malformed descriptors are refused without retrying legacy routes.
Old firmware keeps the frozen application/1, station/1 and `wspr_type1`
contract. Selected unsupported new formats return
`unsupported_station_encoding`, without identity substitution or mutation.
Preserve the returned error code and endpoint-specific HTTP status.

Application/2 includes `wspr_plan` (`wspr-plan/1`): supported state, frame types
and count, 120-second slot separation, rationale and ambiguity/alternate call.
A null station has a null plan. Plans describe encodability, not clock quality,
readiness, enablement, live output or transmission. See
[Pico automatic planning](../User_Interface/Setup/Transmitter/index.md#pico-automatic-wspr-planning)
for ordinary-six, compound, brackets, ambiguity and pair behavior.

Use the loaded station schema unchanged in a complete scoped PUT. For example,
a versioned station body uses `"schema": "transmitter-station/2"` with
`"station": {"callsign": "W1A/AA0NT", "locator": "EM18IG", "power_dbm": 0}`
and the exact loaded target. Zero is a valid reported-power value, not a request
to disable RF. Profile-owned station identity still requires transactional setup.
Config v1 content and config-update/1 omission/null/false/zero semantics,
credentials, flags, schedules, pins and consumed-slot watermark retain their
existing meaning. Partial updates must produce a complete valid configuration;
there is no per-field partial success or durable incomplete draft.

### Read, review and send one scoped operation

1. Select/authenticate the management carrier and explicitly GET a member
   resource. Keep its exact quoted ETag, target and opaque `member_context`.
2. Send that ETag unchanged in `If-Match`, and the context unchanged in
   `X-WsprryPi-Member-Context`. Do not derive either from a device ID or generation.
3. All mutations also require matching `Origin`, `Content-Type: application/json`
   and `X-WsprryPico-Request: 1`. `Sec-Fetch-Site` must be absent, `same-origin`
   or `none`. Existing peer/Host/proxy guards still apply; no CORS grant is added.
4. Send one complete station or supported hardware object. Read back explicitly
   before another save. Changing carrier or attempting a save invalidates other
   resource/legacy editor contexts. Preview and field edits never autosave.

This **legacy station/1** example illustrates the closed complete-station body.
For versioned firmware, replace its schema with the exact loaded
`transmitter-station/2` schema before sending; the station/1 body is refused
when station/2 is negotiated. Replace the example target with the exact loaded
target and review every station field together. These IDs and values are synthetic, not a device to contact.

```json
{
  "schema": "transmitter-station/1",
  "target": {
    "scope": "member",
    "device_id": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "boot_id": "00000000000000000000000000000001"
  },
  "station": {"callsign": "K1ABC", "locator": "FN42", "power_dbm": 20}
}
```

A complete supported hardware body has the same target and a complete pin plan:

```json
{
  "schema": "transmitter-hardware/1",
  "target": {
    "scope": "member",
    "device_id": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "boot_id": "00000000000000000000000000000001"
  },
  "pins": {
    "engine": "direct", "rf_gp": 0, "i2c_pair": null,
    "button_gp": null, "amplifier_gp": null, "lpf_gps": [],
    "indicator": "onboard_led", "indicator_gp": null,
    "indicator_active_high": true
  }
}
```

Select actual GP choices from the authenticated response and check role
conflicts. The nonpersistent preview takes only the complete `pins` object
above as its bare body, with the same host revision/context/intent headers.
The adapter does not forward `If-Match` to Pico's preview, preserving its
nonpersistent semantics. Preview distinguishes validity, conflicts and
operational support and verifies unchanged configuration on readback. A valid
structural I2C plan is not necessarily operationally supported.

Scoped PUT bodies are limited to 1,024 UTF-8 bytes; preview to 2,048. Unknown
fields, duplicate keys, wrong targets and unsupported schemas are refused.
Application is read-only; station/hardware PUT are complete scoped replacements,
not arbitrary merge patches. A successful PUT is confirmed by authoritative
application readback. Profile-owned station fields remain read-only. Match the
loaded station schema and negotiated format support; dBm is WSPR metadata,
separate from measured RF output, drive and calibration.

### Conflicts, uncertainty and ownership

Missing revisions return 428; stale remote revisions return 412. Changed or
invalidated member context/selection can return 409 `member_read_required`.
Other 409 refusals include busy/unresolved runtime or unsupported resources.
Keep the actual error code: a lost/malformed reply after dispatch can be
unconfirmed even if persistence succeeded. Preserve the draft, explicitly read
saved/active state and review before a new deliberate save. Never automatically
retry a mutation, substitute an endpoint or switch save strategy after failure.

Saved hardware, active-at-boot hardware and null/unknown active state remain
distinct. Changed pins latch restart/output inhibition for this boot; saving the
old plan or station does not clear it. Storage faults differ from application
faults. `output_disable_failed` can accompany a saved change with unconfirmed
shutdown. No save restarts, reconnects WTP, enables recurrence, claims or transmits.

Engineering mTLS and explicitly supported consumer station/AP management use
the host's existing idle admission. Built-in route flags do not prove remote
support. Missing shared-resource discovery preserves the compatible legacy
editor; malformed/unsupported advertised discovery refuses without fallback.
See [management and member controls](../User_Interface/Setup/Transmitter/index.md#management-connection-and-login)
for login expiry and supported GP/adapters.

### Similarly named configuration resources

| Browser path | Owner and update contract |
| --- | --- |
| `/wsprrypi/config` | Legacy Pi host configuration; full PUT or PATCH; conditional writes supported, legacy unconditioned compatibility retained. |
| `/wsprrypi/api/v1/host/config` | Explicit `wsprrypi-host-config/1` host envelope; PUT applies a merge patch under exact required host ETag. |
| `/wsprrypi/api/v1/member/configuration` | Coordinated selected-Pico atomic editor; GET context then POST changed known fields with exact member target/revision. |
| `/wsprrypi/api/v1/config` | Compatible remote Pico Config resource; GET/PUT retain remote revision and complete-config semantics. |

The coordinated editor negotiates one supported save strategy before mutation.
It preserves Pico-owned settings outside the form and safely refuses unknown
configuration fields rather than losing them through an older full replacement.
Null password means preserve; arrays replace atomically; explicit false/zero
retain their meaning. Ordinary edits are not whole-configuration resets.
Schedules-only saves preserve unrelated drafts. None of these resources gives
the browser independent WTP CLAIM/LOAD/ARM authority: job submission stays with
the host application. See the [compatibility contract](https://github.com/WsprryPi/WsprryPi/blob/devel/docs/wtp-configuration-compatibility.md).
<!-- endif-wsprrypico -->
