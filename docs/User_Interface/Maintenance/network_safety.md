# Privileged Network Safety

Privileged network safety restricts operations that can change configuration,
control the transmitter or Pi, collect diagnostics, or use the browser-facing
WebSocket connection. The default and recommended value is `enforced`.

## What enforcement protects

When enforcement is active, Apache permits these browser operations only from
a client on an eligible network directly connected to the Pi:

- replacing, patching, repairing, or resetting configuration;
- stopping and disabling transmission;
- creating, checking, downloading, or deleting a support bundle;
- changing privileged network safety; and
- opening the browser-facing WebSocket endpoint used for shutdown, reboot,
  stop, test-tone, state, and broadcast traffic.

Read-only HTTP configuration, version, status, telemetry, and support-intake
availability remain readable where practical. The WebSocket is different:
Apache authorizes the connection before it can see individual commands, so it
restricts the entire `/wsprrypi/socket` endpoint. Off-LAN browser clients lose
both control commands and read-only WebSocket updates while enforcement is
active.

An eligible LAN is derived from active, directly connected Ethernet or Wi-Fi
interfaces. Loopback peers are allowed for local proxying. VPNs, tunnels,
bridges, containers, point-to-point interfaces, and merely private or
local-looking addresses are not trusted automatically. If no eligible subnet
can be established, protected non-loopback access fails closed.

## Apply a state

Use the **Privileged network safety** panel on **Maintenance**:

1. Compare **Configured** and **Active**. If either is **Unknown**, stop and
   inspect the application and Apache logs before changing the setting.
2. Select **Enforced** or **Insecure disabled**.
3. To disable the restriction, type `DISABLE LOCAL-LAN SAFETY` exactly.
4. Select **Apply requested state**.
5. Wait for validation and confirmation. Do not close the page while the
   controls show that apply is in progress.
6. Confirm that **Configured** and **Active** show the intended value.

Enabling protection requires the same explicit Apply action but no typed
phrase. A successful apply reloads Apache; it does not reboot the Pi and does
not require normal Setup autosave.

```{warning}
When **NETWORK SAFETY OFF** is displayed, privileged operations are no longer
limited to the Pi's directly connected LAN. Host, Origin, CORS,
malformed-request, method, command, forwarded-header, and configuration
validation still apply, but this is not a substitute for LAN peer restriction.
```

## After a network change

Changing an interface address, prefix, or active Ethernet/Wi-Fi connection does
not silently regenerate Apache policy. Return to **Maintenance**, select the
intended state, and apply it again so WsprryPi can discover the current
eligible subnets, validate the complete Apache configuration, reload Apache,
and confirm the policy.

## Recover from an apply failure

An apply failure may leave the requested browser draft different from the
configured or active state. The UI preserves the draft so you can see what was
attempted, but it does not claim success.

1. Record the requested, configured, and active values shown on Maintenance.
2. Inspect WsprryPi and Apache logs for interface discovery, Host or Origin,
   candidate validation, Apache configuration test, reload, or confirmation
   errors.
3. Correct the reported network or configuration problem.
4. Reload Maintenance and verify the current values.
5. Apply **Enforced** again.

If the status remains unknown, do not assume the peer restriction is active.
Use local console or SSH access from an already trusted administrative path to
diagnose Apache and WsprryPi. Do not repeatedly disable protection to work
around a validation failure.

## Direct backend clients

Ports `31415` and `31416` are backend interfaces, not the supported browser
path. Compatible non-browser clients may connect directly only from loopback or
an eligible directly connected LAN while enforcement is active. They must send
a valid local `Host`; if they send `Origin`, it must match `Host`. Forwarded
client headers never grant access.

For endpoint details, see [REST API](../../Advanced_Operations/rest_api.md) and
[WebSocket Interface](../../Advanced_Operations/websocket.md).

## Pico hostname and management access

Changing a Pico hostname does not change the Pi's directly connected LAN
policy or Apache configuration. Keep **Privileged network safety** enforced;
disabling it does not fix `.local` discovery, a wrong destination or a
certificate mismatch. Use the intended Pico's current IP or available setup
Wi-Fi to recover access, following
[Change the Pico hostname](../Setup/Transmitter/index.md#change-the-pico-hostname).

A hostname, advertisement or browser-tab title helps locate a Pico but does
not authenticate it. Consumer Station control uses the Wi-Fi password saved
on that Pico and does not require a browser CA or client certificate. This
HTTP workflow retains its existing trust limits: use a trusted network and
endpoint, and do not treat a shared password as proof of unique device
identity. A renamed page requires a fresh login; it does not transfer a login
from the old address.

Engineering HTTPS browser addresses require a certificate valid for the URL's
hostname or IP address. Network (TLS) WTP separately checks its configured
expected certificate identity, including when the connection destination is
an IP address. A consumer rename preserves its existing
CA and retained clients while replacing the server certificate for the new
name. Engineering deployments instead require matching replacement
credentials through their provisioning workflow. Do not accept a certificate
error or silently change transport to make a renamed endpoint connect.

Keep the connection destination, expected TLS identity and full WTP device ID
separate when updating a Pi connection profile. See
[After a Pico hostname change](../../Advanced_Operations/ini_configuration/transmitter_backends.md#after-a-pico-hostname-change).
