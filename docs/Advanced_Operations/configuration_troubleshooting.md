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

Use [Change the hostname in the Pico manual](https://wsprrypico.readthedocs.io/en/devel/maintain.html#change-the-hostname)
for the device-side save, restart and sign-in procedure. WsprryPi's settings
form does not rename the Pico; renaming a Fleet profile changes only its label.
If a Pico save or restart reply is lost, read saved and active state before
repeating it. A timeout does not prove the change failed or output stopped.

Keep Pi transmission and the affected Fleet assignment paused while reviewing
the destination. Resolve pending, owned or uncertain jobs through
[Pico status and recovery](../User_Interface/Setup/Transmitter/index.md#pico-status-and-recovery).
Disabling Pi transmission alone does not disable Pico's autonomous schedule.

| What you see | What to do |
| --- | --- |
| Browser opens at the new name, but WsprryPi cannot connect | Review the saved profile, active `[WTP]` endpoint and independent assignment destinations. A browser HTTP address is not a WTP listener port. |
| Fleet still shows the old destination | Edit and freshly identify the saved profile, then use **Use this device** if changing the single active endpoint. Editing a label or profile alone does not switch it. |
| New name is unreachable | Try the current LAN IPv4 address and verify the full device ID. Follow the Pico manual for duplicate-name or setup-Wi-Fi recovery. |
| Different full device ID | Verify the intended board and address before using it. Renaming does not change the stable ID. |
| Certificate or hostname-certificate error | Check the expected TLS identity and provisioned credentials. Keep verification enabled and preserve the chosen transport. |
| Pico restart remains unconfirmed | Follow the Pico manual's readback/reconnect procedure. A returning page or countdown alone does not establish a new boot or readiness. |

[After a Pico hostname change](ini_configuration/transmitter_backends.md#after-a-pico-hostname-change)
explains which Pi settings to update. Keep
[Privileged network safety](../User_Interface/Maintenance/network_safety.md#pico-hostname-and-management-access)
enforced; disabling the Pi's LAN policy does not repair discovery or Pico
credentials. Device-side reset and access recovery belong to the
[Pico maintenance guide](https://wsprrypico.readthedocs.io/en/devel/maintain.html)
and [Pico troubleshooting](https://wsprrypico.readthedocs.io/en/devel/troubleshoot.html).
