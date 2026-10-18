# Configuration Troubleshooting

## Troubleshooting CW Configuration Saves

When a QRSS, FSKCW, or DFCW message would take longer than its configured repeat interval, Setup marks the Message field invalid and displays **Save failed** with the calculated duration and repeat interval. The invalid draft remains in the browser so it can be corrected, but it is not applied to the running configuration. Autosave resumes automatically when the adjusted duration is less than or equal to the repeat interval.

This inline state identifies a timing problem that can be corrected on the Setup page. Other configuration reload failures that cannot be tied safely to an editable field may still appear in the general reload-failure dialog and may require checking the application log or configuration file.

See {ref}`cw-message-too-long` for the duration inputs and correction steps.

## GPIO RF Output Conflicts

When the GPIO transmitter backend is selected, its configured GPIO4 or GPIO20 RF output cannot also be assigned to an enabled Band GPIO, Transmit LED, Shutdown Button, or Amp Control. Setup marks both conflicting controls with `GPION is reserved by GPIO RF Output.` and keeps the invalid draft visible without saving it.

Resolve the conflict by changing either pin, disabling the ordinary GPIO role, or selecting the Si5351 backend. The reservation depends on the selected backend, not the **Transmit** switch, so turning transmission off does not release the GPIO RF output pin. Disabled ordinary roles may retain their pin values.

(startup-transmission-is-inhibited)=
## Startup Transmission Is Inhibited

At every daemon start, WsprryPi attempts to disable the selected transmitter backend before it starts services or schedules any transmission. If the safe state cannot be confirmed, the daemon continues running for diagnosis but blocks all transmission paths. This startup inhibition is separate from the saved **Transmit** switch and **Enable on Boot** policy.

Review the WsprryPi log for the startup-quiescence error, then check the hardware selected on the **Setup > Transmitter** page:

- For **Si5351**, verify the configured I2C bus and address, device wiring and power, and that the device is visible to the operating system.
- For **GPIO**, verify that the Raspberry Pi model supports direct GPIO-clock transmission, that the configured transmit pin is GPIO4 or GPIO20, and that the service has the permissions required to access the Pi peripherals.

Also correct any configuration error identified in the log. The daemon deliberately does not clear this safety latch after an INI reload, mode change, or transmission-toggle change.

After correcting the cause, restart the service:

```console
sudo systemctl restart wsprrypi.service
```

Then confirm in the log that the configured backend was selected without a startup-inhibition error. After a successful restart, the saved **Enable on Boot** policy determines whether transmission scheduling is enabled.

Do not repeatedly restart the service without correcting the reported cause. If the failure persists, leave transmission disabled and collect a support bundle from **Maintenance** before requesting help.

## Pi 5 RP1 Route Is Unavailable or Mismatched

Leave transmission disabled when the route panel reports **Unavailable**,
**Mismatch**, **Restoration failed**, or **Recovery required**. Do not edit
provider files, unload modules, or try to select a route manually.

The normal installer supplies and validates the RP1 provider and route manager
on Pi 5-family systems. Re-run the
[WsprryPi installer](../Install/index.md#install-wsprrypi) first. It can
recover and update an exact installer-owned runtime, but it refuses foreign,
modified, mixed, or unproven provider state rather than overwriting it.

After installation, `/dev/rp1-gpclk` is normally absent until a route is
selected. Route switching and removal happen in the current boot. For a
selected route, requested, persisted, configured, and active routes must all be
GPIO4 or all be GPIO20. For a removed route, configured and active must both be
None and the transmission consumer endpoint must be absent. Eligibility and
cleanup must also be accepted; WsprryPi does not fall back to another route or
backend.

For **Restoration failed**, correct the reported service error and follow the
command shown in the route panel. For **Mismatch** or **Recovery required**,
preserve the displayed state and collect a support bundle before making manual
changes. The exceptional **Recover to no route** action intentionally leaves
WsprryPi stopped and inhibited; use **Remove route** for normal removal. The
RP1 diagnostics include endpoint, route-manager socket, persisted-route, and
journal-inventory observations when readable. If the installer reports an
ownership, identity, or recovery refusal, preserve that state and the retained
installer failure details; do not unload modules, delete journals, or edit
provider files manually.

## Pico hostname or restart is unconfirmed

Use the Pico's own **Station control** page for hostname changes. WsprryPi's
settings form does not edit the Pico hostname, and renaming a Fleet device
profile changes only that profile's label. See
[Change the Pico hostname](../User_Interface/Setup/Transmitter/index.md#change-the-pico-hostname)
for the save, restart and sign-in steps.

If a save times out or the page disconnects, keep the tab open. Sign in again,
choose **Refresh**, and compare **Active** with **Saved**. The save may already
have succeeded. Review the saved hostname before enabling another save; do not
repeat a save or restart merely because its reply was lost. Copy unsaved drafts
before reloading the page or leaving for the new address.

| What you see | What to do |
| --- | --- |
| Invalid hostname | Enter one 1–63 character label of ASCII letters, digits or hyphens plus `.local`, starting and ending with a letter or digit. Do not enter a URL, IP address or port. |
| Busy or save unavailable | Disable Pico's standalone schedule and resolve pending, owned, active or failed work. Turning off the Pi's Transmit switch alone is insufficient. |
| Saved differs from Active | The current boot still uses the old name. Confirm the saved value before one explicit restart. |
| Original boot is still running | Restart has not been observed. A countdown or reachable old page does not prove a restart occurred. Read current state before a new explicit attempt. |
| New name is unreachable | Try the Pico's current LAN IPv4 address on the same network. `.local` discovery may be unavailable even when IP access works. Use setup Wi-Fi if needed. |
| Duplicate name or discovery conflict | Open by current IP or setup Wi-Fi, choose a unique name and repeat the explicit save/restart workflow. Pico does not automatically add a suffix. |
| Different Pico or wrong device ID | Do not sign in or change settings there. Verify the intended board, address and saved connection profile first. |
| Certificate or hostname-certificate error | For engineering HTTPS/TLS, verify the expected certificate identity and provisioned credentials. Do not bypass verification or switch to Plain LAN to hide the failure. |

For setup-Wi-Fi recovery on the standard button configuration, hold the
configured button for at least nine seconds to request setup after output
shutdown, then release it. The temporary access window lasts ten minutes from
release; a saved custom or disabled button assignment takes precedence. Join
the Pico's setup Wi-Fi and open `http://192.168.4.1/radio`. If saved Wi-Fi is
unavailable, supported consumer firmware also requests automatic fallback
after a minute; it can withdraw that fallback when the normal connection
recovers. The setup Wi-Fi name and fixed address do not change with the
hostname.

If the editor is absent, confirm that the installed firmware supports it.
Complete station commissioning if only Wi-Fi setup is saved. Engineering names
remain bound to their provisioned certificates. If a consumer certificate
update is refused, restore working time synchronization and read the reported
error before trying again. A storage or recovery fault must be resolved through
the existing recovery workflow; repeated saves do not clear it.

**Cancel reconnect checks** cancels checking, not a saved change or an already
requested restart. Checks stop after about 90 seconds and never resend the
restart. After returning, sign in and refresh: success requires the same full
device ID, a different boot and the intended name as both Active and Saved. Review
[Pico network access](../User_Interface/Maintenance/network_safety.md#pico-hostname-and-management-access)
before changing trust or connection settings.
