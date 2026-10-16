# Raspberry Pi 5 RP1 GPCLK

On Raspberry Pi 5-family systems, the WsprryPi installer resolves, installs,
and validates a compatible RP1-GPCLK-DKMS provider and its route-management
service. Installation establishes neutral administration: neither GPIO4 nor
GPIO20 is selected, the transmission consumer remains absent, and output is
disabled. The `/dev/rp1-gpclk` endpoint normally appears only after an operator
selects and applies a route. Si5351 remains a separate backend choice.

## Installation and ownership

Use the normal WsprryPi installer. Do not manually install an additional RP1
provider over an installer-managed one. A repeat installation verifies exact
ownership and identity, safely recovers an existing owned route or neutral
runtime, updates or validates the provider and application, and restores neutral
administration. Foreign, modified, mixed, or unproven provider state is
preserved and reported as a failure for operator review.

Normal uninstall removes the RP1 provider and runtime administration only when
the ownership record and installed identity still match. It does not remove or
adopt an unproven provider. Retained installer failure details and a support
bundle are the preferred evidence when recovery is refused.

Installing the provider does not select a route, change GPIO state, or start a
transmission.

Runtime checks establish application compatibility, not qualification of a
transmitter, band, power level, filter, or RF chain. RP1 development output
requires a current, bounded operation confirmation; saving a route or starting
the application does not authorize transmission.

## Route identities

GPIO4 (header pin 7) and GPIO20 (header pin 38) are separate controller-managed
routes. WsprryPi tracks five distinct facts:

- **Requested**: the operator's current draft or transaction request.
- **Persisted**: the route saved in WsprryPi configuration.
- **Configured**: the route reported by the managed route service.
- **Active**: the route reported by the loaded provider.
- **Eligible**: runtime protocol, capability, route, exclusive ownership, and
  cleanup checks permit the requested operation. Package versions and build
  labels are not an application provisioning whitelist.

Transmission is blocked unless all route identities match and eligibility is
confirmed. There is no automatic route or backend fallback.

## Understand the status

Use the [band qualification table](../About_Wsprry_Pi/index.md#band-qualification)
for the accepted operating scope. The RP1 panel reports separate facts:

- **Resource compatibility**: `Compatible-unqualified` means the RP1
  compatibility checks passed. Accepted band qualification still applies.
- **Route evidence**: describes testing for the selected GPIO route and its
  scope. A TONE result does not replace the broader band table. `Evidence missing`
  or `Evidence invalid` means this information could not be verified; it does
  not make qualified bands unavailable.
- **Operational readiness** and **Output inhibition**: describe whether the
  route can operate now. If it reports **Not ready** or inhibition is **Enabled**,
  follow the reported route or recovery instructions before transmitting.

## Change or remove a route

1. Stop transmission and wait for committed work, cancellation, cleanup,
   provider leases, and backend transactions to finish.
2. Open **Setup > Transmitter** and review Requested and Active.
3. Select GPIO4 or GPIO20 and choose **Switch route**, or select None and
   choose **Remove route**. Choose **Cancel** to discard the draft.
4. Keep the status dialog open while WsprryPi briefly disconnects. Confirm it
   reports the selected route as Active, or reports **Route removed**.

The application delegates route changes to the managed route service through
its bounded interface. Route switching and removal happen in the current boot;
they do not require a reboot. WsprryPi checks transaction generations and
reconciles the reported route before it permits transmission.

**Remove route** returns the controller to a verified neutral state, removes
the transmission consumer endpoint, keeps output disabled, and releases only
the inhibitor owned by the route manager. If WsprryPi was running before the
operation, the manager restarts it online and idle. If the service was already
stopped or administrator-masked, it remains stopped or masked.

The separate recovery action is for an incomplete or inconsistent route
transaction. Recovery is intentionally fail-closed: it stops WsprryPi and
leaves the controller inhibited for operator investigation. It is not the
normal way to remove a route.

If the route is removed but WsprryPi cannot be restored, transmission remains
disabled and the panel reports **Route removed; service unavailable**. Correct
the reported service error, then retry the removal with the installed client,
substituting the route that was removed:

```bash
sudo python3 /usr/lib/rp1-gpclk-dkms/runtime_route_client.py remove gpio4 --execute
```

If the manager is unavailable or reports an ownership conflict, leave
transmission disabled and preserve the error details for troubleshooting.

## Diagnostic evidence

Runtime status reports the route facts known to the running application.
Unknown active, eligibility, cleanup, or journal
facts remain explicitly unknown rather than being inferred.

A support bundle adds independent read-only host evidence under
`bundle/hardware/rp1-gpclk` and the corresponding command reports. It records
scoped DKMS registration; the running kernel and header availability;
kernel-specific filename, version, and `vermagic` for the consumer and route
controller modules; loaded-module state; WsprryPi installation-record presence;
endpoint and route-manager socket state; a route-journal inventory; the
persisted route; and the runtime provider's read-only `inspect` result when
available. Missing, inaccessible, unsafe, timed-out, or nonzero inspection
results remain in the bundle as diagnostic evidence instead of stopping
collection.

The collector does not copy the WsprryPi installation record, attest the Debian
provider package or overlay hashes, change DKMS or route state, load a module,
or authorize output. A support bundle does not establish hardware or RF
qualification.
