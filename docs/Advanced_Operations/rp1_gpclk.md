# Raspberry Pi 5 RP1 GPCLK

On Raspberry Pi 5-family systems, the WsprryPi installer resolves, installs
and validates the RP1-DKMS provider and route administration. Fresh setup
establishes neutral administration with no GPIO route and output disabled.
After that step, an explicitly saved `rp1-gpclk` GPIO4/GPIO20 selection can be
restored with transmission disabled. A retained pin for another backend is not
route consent. The `/dev/rp1-gpclk` execution endpoint normally appears only
when a route is selected. Si5351 remains a separate backend choice.

## Installation and ownership

Use the normal WsprryPi installer. **Passive package installation** installs
files without loading modules, applying overlays, operating services or enabling
output. **Neutral activation** is the separate managed step establishing runtime
administration. **Route selection/restoration** is another explicit transaction.
These steps do not establish live-output authorization.

RP1-DKMS reports its product version from its canonical version header.
WsprryPi requires compatible UAPI, runtime, and lifecycle interfaces.
With the default `RP1_GPCLK_DKMS_SOURCE=auto`, development application branches
resolve provider `devel` to an exact commit. Production selection requires an
eligible published stable release and fails if one is unavailable; it does not
fall back to development source. Explicit source selection remains available
for provider development. `INSTALL_RP1_GPCLK_DKMS=false` skips provider installation.

WsprryPi selects and authenticates the source, supplies its interface
requirements, and calls the provider's public lifecycle interface. RP1-DKMS owns
version classification, native installation, runtime preparation, recovery,
removal, and absence checks. Its receipt is
`/var/lib/rp1-gpclk-dkms/provider-installation.json`; WsprryPi is recorded as the
client. Existing attributable WsprryPi ownership records are verified before
conversion to provider-owned receipts.

Identical incoming inputs retain the owned installation. Changed incoming
payloads at equal semantic-version precedence replace it, and a compatible higher
version upgrades it. Build metadata does not affect semantic-version precedence;
Debian package ordering is checked separately for release transitions.
These operations preserve exact native ownership and recovery checks. Manual
edits to installed provider code are preserved and stop replacement; they are
different from deliberate changes to incoming installation files. Downgrades
require explicit owning removal and reinstall. Transmission remains disabled while the
normal installer prepares neutral administration and restores an explicitly
saved RP1 route.

By default, `REMOVE_RP1_GPCLK_DKMS=auto` removes the attributable provider
installed for WsprryPi. `true` explicitly requests owning removal; `false`
preserves the provider. Uninstall requires verified provider absence before
reporting that it was removed. It retires unchanged application-owned
files and generated defaults. Pre-existing or modified operator data, configured
fleet records, shared operating-system packages, and `picotool` are retained.
Modified code or uncertain required ownership produces a cleanup failure.
Provider recovery evidence is retained until its transaction is terminal and no
live reference requires it.

If installation or required cleanup fails, preserve the error and recovery
files. Do not delete ownership records to bypass a refusal.

The maintained [installation and migration procedure](https://github.com/WsprryPi/WsprryPi/blob/devel/docs/rp1-gpclk-dkms-installation.md)
defines the owning recovery boundaries.

RP1 plans use nominal **200 MHz pll_sys**, with intrinsic `-46.245 ppm` plus
separately selected additional correction. That default is not a board-specific
calibration or a new qualification result. See [calibration accounting](timing_calibration.md).
Runtime readiness, exclusive ownership and the application's bounded operation
confirmation remain necessary. Saving a route or starting the application does
not authorize transmission.

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
and its numbered notes as the accepted application band/mode statement. Keep
these facts independent when reading API/diagnostic output:

- **Structural compatibility**: `Compatible-unqualified` means the provider's
  structural resource checks passed. It does not overwrite application qualification.
- **External scoped evidence**: `qualification-v1.0.0-r1` supplements software
  1.0.0 / package 1.0.0-1. GPIO4 and GPIO20 have independent finite conducted
  TONE evidence at 14,097,100 Hz, 2 mA and nominal 200 MHz pll_sys. Seven accepted
  lifecycle cases per route do not prove every band, mode, board or kernel.
- **Application eligibility**: the requested band/mode/plan has its own policy.
  `not-evaluated` means no application plan was assessed. An observational route
  `eligible=false` is not a band-unavailability verdict.
- **Operational readiness, inhibition, ownership and cleanup**: current state
  determines whether work can be admitted now. Unknown output is not off.

The original immutable provider compatibility manifest remains empty with
`defaultState=Unavailable`. The separate supplement does not rewrite it, erase
the accepted application band table, enroll a target or grant transmission
permission. Pi 5's accepted table retains 2200 m through 10 m including 12 m;
6 m and 4 m remain unqualified, and 2 m/1.25 m/70 cm unavailable. Follow the
full table's mode/scope notes rather than extending finite TONE evidence.

The normal Setup UI shows compact route actions and state. The detailed RP1
fact panel is intentionally hidden; use diagnostics/API or a support bundle
for the additional evidence below.

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

The collector also includes the maintained qualification consumer's verified
local evidence status. Missing, invalid, inaccessible or uninspected evidence
remains explicit; collecting a bundle neither changes the evidence nor grants
output authority. It does not copy the private installation record, change DKMS
or routes, load modules or establish new hardware/RF qualification.

<span id="qualification-cache-and-installed-commands"></span>
### Installed evidence and status

The application installs its maintained consumer, pinned reference and complete
four-file evidence bundle under `/usr/local/lib/wsprrypi`. One application-owned
receipt covers all six files. This also happens when an update skips an unchanged
provider. Legacy helper/reference receipts can be upgraded or removed; foreign
or modified files are retained and reported. Interrupted upgrades can be retried.

The bundle preserves evidence source `bb6815446beb9b96853ad5a353b0d355d4975710`
and all four pinned SHA-256 identities. `qualification-v1.0.0-r1` identifies
that evidence; it is not a separate download requirement. Installation and status
need no evidence network refresh. The old network-populated cache is unused.
The legacy `refresh` command now verifies local bundled bytes and optionally
exports them; it does not fetch a release. A provider version alone is
insufficient attribution.

For a local diagnostic on an installed host, the maintained consumer supports:

```bash
python3 /usr/local/lib/wsprrypi/rp1_qualification.py status --route gpio4
```

Use `gpio20` when inspecting that selected route. This performs bounded passive
provider inspection and reads the verified installed bundle/ownership evidence; it never
downloads or refreshes metadata. Read permissions must permit the installed
provider and evidence inspection. Failure to inspect remains unknown; it is not
permission to infer safe output. Route, exact source/package, both UAPIs,
overlay/artifact inventory and both loaded module build notes must agree before
attribution. Wrong-route/build evidence is refused independently for each route.

- **Evidence missing**: the installed bundle is absent.
- **Evidence invalid**: corrupt or substituted bundle bytes cannot be verified.
- **Not inspected**: this response did not collect supplemental evidence.
- **Provider identity unverified** or unattributed evidence: available bytes
  cannot be bound to this installed runtime; retain the detailed reason.

These are evidence states, not substitutes for readiness or application policy.
The old diagnostic executable frozen inside Debian 1.0.0-1 cannot interpret the
new supplement; use the installed application consumer above. No package asset
was replaced to add this reporting. See the [provider acceptance scope](https://github.com/WsprryPi/WsprryPi/blob/v4.0.0-beta.1/docs/rp1-provider-acceptance.md)
for retained installation/idle-runtime evidence, excluded rollback rehearsals
and exact source/build limitations.
