# Item 12: consolidated operator documentation

Status: repository implementation/review accepted; hosted publication pending. This record is not release
acceptance. Items 13–14, #412/#423 closeout and WsprryPi 4.0 publication remain
outside this task.

## Baseline and source authority

October 16, 2026: docs `devel` starts clean at
`8d6d037f7e1ae1bb9f0a525735ddcf5a6ee57d3a`, equal to freshly fetched
`origin/devel` (0 ahead/behind). No fast-forward was needed. No feature branch,
reset, stash, discard or rebase is used.

- Application: `a2437d1bf026e91ea95ac7e2a7a0101e3c4f11a1` (`devel`). Its
  unrelated local `release_tools/Release Punchlist.md` edit includes item 11
  closure and item 12 in-progress status; preserved read-only.
- Pico checkout: `14478d2b7509b356d1f146bc2f520ac16d188427`. Concurrent dirty
  Phase 15.8 implementation is excluded as documentation authority. The Pi's
  current accepted P15.7 dependency is
  `26ae596b540e92f25da37f978321ba1ec5934bdc`; shared-resource contracts and the
  Pi's actual closed adapter/fixtures define this update. No new Type 2/3
  member-write capability is inferred from local Pico work.
- Provider checkout: `80c43dc5dceb10b52e85358d30ae16e4d7b58c4a` (one local
  commit ahead; dirty ROADMAP preserved). Release authority is frozen software
  `8c16d3c237cb1267cbedafb5da2bb74132ca5de0`, tree
  `4c1ad8acf513b36ba32e58a636942655accbb52d`, v1.0.0 / Debian 1.0.0-1.
  Supplement authority is `bb6815446beb9b96853ad5a353b0d355d4975710`, tree
  `b659a6e27ac07e77dff6f0ec89490afbe9e0ceb4`, qualification-v1.0.0-r1,
  independently pinned in the application lock.

All application paths below are reviewed at `a2437d1`. Its UI, transmitter,
PPM-Manager and Chipset-Offsets are ordinary tracked trees, not separately
advancing submodules. Source/reference review is read-only, with no Pi access,
service operation, installation, I2C scan, route operation or RF generation.

## Source-to-page coverage matrix

Prepared before operator-page edits. Paths in the source column are application
paths unless explicitly marked otherwise. Dispositions are updated after checks.

| Topic | Authoritative source/revision | Current pages | Discrepancy | Planned change | Verification | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Host/member/job ownership | `docs/wtp-browser-api.md`, `src/wtp_integration/browser_api.cpp`, `src/wtp_runtime_bridge.cpp` | REST; Setup; Transmitter | Shared member resources absent; blanket autosave | Distinguish scopes and explicit controls | Methods, routing, UI producer | Implemented; validated below |
| Resource bodies/revisions | `src/wtp_integration/configuration.cpp`, `browser_http.hpp`; P15.4 record | REST | No complete scoped examples or editor context | Complete station/hardware/preview; ETag/context/intent/readback | Closed adapter and Pico schema; JSON parse | Implemented; validated below |
| Management and preservation | `docs/wtp-configuration-compatibility.md`, `data/wtp-management.js`, P15.7 record | Transmitter; backend INI | TLS-only management; missing login/resource state | Explicit carriers/expiry; unknown settings/refusal; saved/active/faults | Templates, adapter, fixture | Implemented; validated below |
| Test Tone lifecycle | `docs/development/test-tone-lifecycle-review.md`, `docs/bounded-tone.md`, scheduler, WebSocket commands, `data/site.js` | Maintenance; WebSocket | Blanket ended/off implication; serialized internals | Acceptance/activity; cleanup/restoration; deferred edits; recovery | Production responses and browser fixtures | Implemented; validated below |
| Intrinsic/additional correction | `system_clock_frequency_estimate.*`, `Chipset-Offsets`, planner | Timing; Transmitter; CLI; INI | Formula omits intrinsic; fallback wording too broad | Additional-only formula and no double counting | Selector, composition, defaults/serialization | Implemented; validated below |
| Chrony age/provenance | `PPM-Manager`, appended Calibration Scope Decisions closeout | Timing; Transmitter | Unavailable implies immediate manual; repaired findings absent | Unknown age, bounded prior-qualified reuse, selected/combined attribution | Parser/mapper/qualifier and UI | Implemented; validated below |
| Calibration ownership | `arg_parser*`, backend resolution, Si5351 planner, WTP execution plan | CLI; backend INI; Timing | Old aliases presented as canonical | Canonical switches with accepted aliases; Si5351 sign; remote-local correction | Source syntax/defaults and offline checks | Implemented; validated below |
| Si5351 readiness/recovery | Accepted readiness review; `wspr_transmit_backend_si5351.cpp` | Transmitter; runtime INI; CLI | Discovery conflated with readiness; output-off promise | Phase-specific faults, uncertain cleanup, owned recovery, no active resume | Backend admission and retained cleanup | Implemented; validated below |
| Drive/fade limits | Si5351 backend/planner | Transmitter; CLI/CW; INI example | Estimated dBm; analog-envelope wording | 1–4 = 2/4/6/8 mA; duty chopping/deadlines | Backend and envelope validation | Implemented; validated below |
| Inventory | `si5351_inventory_process.*`, inventory isolation report/review, UI | Transmitter; REST; backend INI | Saved address disappears; no deadline/cache | Two-second scan/25 ms cleanup; unchecked/busy/error/not-found | Worker and UI branches; no target scan | Implemented; validated below |
| RP1 install/restore | `docs/rp1-gpclk-dkms-installation.md`, `runtime-route-workflow.md`, installer/reconcile source | Install; RP1; Transmitter | Every install said to erase route | Passive package; neutral activation; explicit saved-route restoration idle | Owning installer and runtime workflow | Implemented; validated below |
| RP1 metadata/diagnostics | `scripts/rp1_qualification.py`, lock/tests; item 10 record | RP1; REST; Install | Missing cache/refresh; hidden panel described as visible | Pinned evidence, passive status, explicit refresh, independent route/build checks | Consumer parser and support integration | Implemented; validated below |
| Historical/qualification boundary | Existing About band table/notes; item 10; historical Issue 399 | About; Experimental RP1 | Historical policy can read as current | Preserve About bytes; label historical scope throughout | Hash equality; nosearch/navigation checks | Implemented; validated below |
| Screenshots/item 11 | Existing assets; current templates and retained fixture captures | Setup; Maintenance; Transmitter | Old Utility Test Tone image materially inaccurate | Replace that image only; retain accurate preview and other images | Actual UI fixture, light/dark desktop/mobile review | Implemented; validated below |
| PDF export blockers | Existing About_WSPR prose and Internals SVG; real pdfLaTeX errors | About_WSPR; Internals | Unsupported Unicode minus and direct SVG | ASCII minus and same-diagram vector print PDF with explicit builder-only markup | Actual default/Pico PDF compilation; rendered page checks; SVG hints retained | Repaired; passed |
| Navigation/gating/exports | `docs/_ext/feature_flags.py`, `image_delivery.py`, existing tests | All affected pages | New content must retain delivery behavior | Existing Pico markers; no build-code redesign | Tests; strict HTML/EPUB/LaTeX both modes; PDF; browser checks | Implemented; validated below |

## Documentation Impact

Operator destinations remain the existing REST/WebSocket, Setup/Transmitter,
Maintenance, calibration, CLI/CW, backend/runtime INI, RP1 and Install pages.
No new guide duplicates those workflows. Two pre-existing PDF export blockers
also required bounded repairs: an ASCII minus in About_WSPR and a vector PDF
fallback for the unchanged Internals SVG. Existing builder-specific `only` directives retain the exact SVG URI for
HTML/EPUB and use PDF for LaTeX. No extension,
configuration, dependency or build-code change is introduced. The historical Issue 399 page retains
its original heading anchors, measurements, nosearch/orphan metadata and absence
from normal navigation. `About_Wsprry_Pi/index.md` is byte-identical, SHA-256
`6fccbee61d6af916775e5cf645741ba59de120134a2625dfcc1561e87857e076`.
Its band dispositions and four numbered scope notes remain authoritative.

Only three applicable TODO entries close: Si5351 configuration, Test Tone/direct
CLI behavior, and autosave/validation. All other historical backlog remains open.
Product/design context, CSS, templates, feature gating and image-delivery code
are unchanged. No new management secret, WTP ownership, PPS mechanism, RP1 parent,
provider policy or qualification claim is introduced.

During the task, another writer published application checklist-only commit
`587c7b137e982dca012701c0a5e85422bf720d73` (the application source diff from `a2437d1` is empty outside the
punchlist). Its Beta 1 planning scope was reread: item 12 remains the same;
items 13–14 remain open and this task does none of that work. Concurrent Pico
Phase 15.8 edits also progressed at the same observed HEAD. This task made no
sibling writes and does not claim those concurrent edits were byte-identical.
Provider status/diff remained unchanged at the preservation check.

### Screenshot disposition

`User_Interface/Maintenance/test_tone.png` replaces the materially obsolete
Utility card with the retained actual UI acceptance fixture from application
`fbb80fa2d1f654c10b8fcf695390144e945e0dd1`, also present unchanged at `a2437d1`.
It is 1440 by 1000, 142,818 bytes, SHA-256
`d23f11e942174e68fd750bd95617e14dfc2e851f2da6683698b02d525f88c95c`.
No crop, re-encoding or invented hardware result was used. The caption labels
synthetic transport/runtime feedback; the full-resolution image remains linked.
Current tone markup/CSS are unchanged from the retained capture; subsequent
site.js changes do not replace that tone presentation. Retained desktop/light,
mobile/light active-difference, desktop/dark restored and mobile/dark uncertain
cleanup captures were inspected against current templates/status code.
The accurate disconnected frequency-source image, Setup screenshots and all
other images remain unchanged. No new member screenshot is needed for the
textual resource workflow; no live hardware success is fabricated.

## Review and validation ledger

Generated logs, the disposable source snapshot and captures stay in ignored
`docs/_build/item12-evidence/`; none is committed. Build commands always first
activate `source docs/.venv/bin/activate`, using that Python rather than the
system interpreter. Final local environment: Python 3.14.8, Sphinx 9.1.0,
Docutils 0.22.4, MyST 5.1.0 and RTD theme 3.1.0. No C++ compilation or hardware
test was performed.

Initial implementation tests: all four `python -m unittest discover -s tests`
tests pass. Strict clean HTML, EPUB and LaTeX generation pass in both default
and `WSPRRYPI_DOCS_INCLUDE_PICO=1` modes with zero Sphinx warnings. Full-corpus
cached default -> Pico -> default HTML switching also passes without `-E/-a`.
Every copied source equals the feature-filtered authored source. Default
navigation, search, copied sources and exports exclude the new gated material;
the general Pico incompatibility note is preserved. Historical Issue 399 has
zero search hits.

A temporary checker parses all 14 JSON fences in changed pages. Complete station
and hardware examples plus the bare preview plan validate against the accepted
P15.7 Pico schema, copied read-only from its exact Git object. Independent
closed Pi adapter checks confirm fields, complete target/plan, GP0 eligibility,
Type 1 K1ABC/FN42/20 station, drive-independent metadata and byte budgets.
HTTP headers/methods/revisions/context and uncertainty behavior were separately
checked against browser_http, browser_api, configuration coordinator and runtime
bridge; the four similarly named config paths keep distinct request contracts.
No prose command was executed on a target.

INI values were compared to application stock configuration and parsing/defaults.
All changed values match implemented defaults/units: estimate enabled,
residual/manual/reference PPM zero, Si5351 level 1, boot Never and CW start second
5. The complete example intentionally retains its existing example message 73
(stock HELLO), explicit canonical frequency-profile/preferences and optional
8m/5m blank selectors; these are valid examples, not newly claimed stock bytes.
Canonical CLI flags and retained --ppm/--transmit-pin aliases were checked in
arg_parser and help source. Retired --use-ntp long options are no longer taught
as parsed options. The two installed RP1 commands were verified against the
consumer parser and effects, without executing them.

Both HTML trees contain 52 pages and 51 content-image instances: zero broken
local links/fragments/assets, nonempty image alt and explicit size/loading/async
decoding hints. Item 11 code/CSS hashes are unchanged. New caption/link does not
change its eager/lazy delivery policy. Export verification and hosted identity
are recorded below after actual compilation/publication.

### Impeccable and visual coverage

Impeccable 4.1.1 context loader ran once, with existing PRODUCT/DESIGN Read mode;
the user confirmed to proceed with that context. Clarify, craft-floor, Read,
audit and bounded polish guidance were read. No prior critique snapshot existed.
The detector ran once on five affected rendered HTML surfaces: Maintenance,
calibration, RP1, Pico REST and Pico Transmitter. It returned no regex findings,
but reported **degraded parsing** because htmlparser2/css-select/css-tree/domutils
were unavailable. Custom-property resolution, selector matching and computed
contrast are unavailable; this is not a full-parser or accessibility audit.
There are no detector false positives to dismiss and no new palette advisories.

Chromium in-app review: desktop 1440x900 and mobile 390x844, existing white/slate
documentation theme only. Setup, Maintenance result/recovery, calibration
qualification, RP1 cache commands, member resources and REST bodies were reviewed.
No page-width overflow or broken image was observed in the ten paired samples.
Keyboard Enter opens mobile navigation; Escape closes it and returns focus to
the opener. Breadcrumb layout and previous/next links remain present; default
search returns Si5351 results. Mobile text enlargement measured 32px from 16px
with no whole-page overflow; this is 200% text simulation, not OS/browser zoom
or a screen-reader/real-device certification. EPUB XHTML is also inspected at
768x1024. Bounded confirmation follows the repairs listed below; no redesign.

## Separate adversarial assessment

After implementation, a separate in-thread pass reviewed the complete diff,
coverage matrix, examples, screenshot provenance and completion claims against
source independently of build success. No separate-agent review is claimed.

| Finding | Severity / reproduction | Repair | Validation / reassessment |
| --- | --- | --- | --- |
| Existing GPIO qualification prose contradicted processor/mode distinctions | P2: old Setup claimed blanket 2m rejection and listed only four qualified bands | Point to preserved accepted table/notes and distinguish default Unqualified refusal from Unavailable | Source policy/table review; strict build/link checks |
| Management label drift | P3: draft said Management carrier; current template says Management connection | Use exact label; retain Validate candidate pins and Reported WSPR power (dBm) | Current template comparison and bounded rendered confirmation |
| Historical anchor change | P2: draft renamed Scope and prerequisites | Restore heading/anchor; put historical scope in surrounding prose | Existing anchors and nosearch/navigation checks |
| Config snapshot and explicit RP1 CLI selection | P2: legacy GET wording called saved state active; backend list omitted explicit rp1-gpclk | Distinguish snapshot from committed work and document explicit RP1 selection without fallback | get_public_config_snapshot, tone-deferred jConfig and arg_parser reviewed; affected builds repeated |
| Old AM comparison sign would misdirect GPIO correction | P2: old F/F_ref expression had opposite sign to positive-fast GPIO convention | Use approximate additional F_ref/F adjustment; distinguish Si5351 sign and correction already active | Algebra and actual planner sign/source review; no measurement claim |
| False PDF success risk | P2: actual pdfLaTeX stops on pre-existing U+2212, then direct SVG | ASCII minus repair; same-diagram print fallback; actual compilation required | Previous successful RTD raw log also contains these errors under force mode; final strict results below |
| Print fallback initially lost image geometry | P2: wildcard image URI no longer resolved through item 11 intrinsic sizing | Use builder-specific only blocks with explicit original SVG and print PDF paths | All 51 image instances retain dimensions/loading; HTML SVG URL unchanged |
| Evidence overclaim / cross-repo drift | P2: dirty Pico future work and newer provider maintenance are not accepted wire/release inputs | Pin accepted P15.7 schema, immutable provider/software supplement and application adapter; preserve concurrent work | Source identities and byte-level retained capture checks; no RF/installed-system claims |

All content findings were repaired. Final export, publication and reassessment
dispositions follow; none of the results above closes integrated review or release.

## Final repository acceptance

All actionable in-scope findings are repaired and affected checks pass. The
final reassessment revisited every matrix row, source contract, example,
restoration/correction/qualification boundary, gated output and screenshot
claim. No unresolved actionable item remains in this repository scope.

Actual PDFs compile with latexmk/pdfTeX in a new disposable local Debian build
container based on the existing `wsprrypi-item10:local` image. LaTeX packages
were installed only inside that container; nothing was installed on macOS or
a target. Default PDF has 134 pages; Pico PDF 144. Final logs contain zero
LaTeX errors and zero LaTeX/package warnings, with whole-book typesetting
advisories: default 54 overfull / 82 underfull boxes; Pico 54 / 101.
Inspected changed JSON/table,
Maintenance, calibration and RP1 pages have no clipping or overlapping content.
This is not a claim of full-book print reflow. EPUB XHTML code is readable and
contained at 768x1024; EPUB archive/content and both PDF visibility checks pass.

The pre-existing fatal export errors were reproduced and repaired, rather than
accepting RTD force-mode success alone. Vector print fallback is 22,027 bytes,
produced from the unchanged SVG with `rsvg-convert 2.60.0`, SHA-256
`f7f8b6ef886aa8d0c55a5d7f382a7f9922eccae3d62f5353114b39f96b24344d`.
The diagram is visually inspected; HTML's exact SVG URI, full-resolution link,
1350x750 dimensions, eager loading and async decoding match the item 11 output.
A bounded final confirmation checks the corrected management label, 200% API
text and repaired print value rendering. No general polishing loop follows.

Reproduction (each session first activates the local docs environment):

```bash
source docs/.venv/bin/activate
python -m unittest discover -s tests
python -m sphinx -b html -W --keep-going -E -a docs docs/_build/item12-default
WSPRRYPI_DOCS_INCLUDE_PICO=1 python -m sphinx -b html -W --keep-going -E -a docs docs/_build/item12-pico
python -m sphinx -b epub -W --keep-going -E -a docs docs/_build/item12-epub-default
WSPRRYPI_DOCS_INCLUDE_PICO=1 python -m sphinx -b epub -W --keep-going -E -a docs docs/_build/item12-epub-pico
python -m sphinx -b latex -W --keep-going -E -a docs docs/_build/item12-latex-default
WSPRRYPI_DOCS_INCLUDE_PICO=1 python -m sphinx -b latex -W --keep-going -E -a docs docs/_build/item12-latex-pico
```

In the disposable TeX environment, each generated LaTeX directory passed
`make all-pdf LATEXOPTS=-interaction=nonstopmode`, without force/ignored errors.
Local source/JSON/HTML/EPUB/PDF checks and logs are temporary validation tools;
no new prose-mirroring regression test or runtime dependency is added. All four
existing behavioral tests pass, including incremental gating and image delivery.
No local Mac C++ build, target command, installation/service/GPIO/I2C/RF check,
GitHub issue change, application punchlist edit, integrated item 13 review or
item 14 packaging/publication is performed.

Exact changed paths (this content revision):

- `TODO.md`
- `docs/About_WSPR/index.md` (ASCII minus export repair only)
- `docs/Advanced_Operations/rest_api.md`
- `docs/Advanced_Operations/websocket.md`
- `docs/Advanced_Operations/timing_calibration.md`
- `docs/Advanced_Operations/rp1_gpclk.md`
- `docs/Advanced_Operations/ini_configuration/transmitter_backends.md`
- `docs/Advanced_Operations/ini_configuration/runtime.md`
- `docs/Advanced_Operations/ini_configuration/default_wsprrypi.ini`
- `docs/Command_Line_Operations/transmitter_backends.md`
- `docs/Command_Line_Operations/cw_modes.md`
- `docs/Experimental/rp1_gpio.md`
- `docs/Install/index.md`
- `docs/Internals/index.md` (builder-specific image reference only)
- `docs/Internals/wsprrypi_data_flow.pdf` (same-diagram print fallback)
- `docs/User_Interface/Setup/index.md`
- `docs/User_Interface/Setup/Transmitter/index.md`
- `docs/User_Interface/Maintenance/index.md`
- `docs/User_Interface/Maintenance/test_tone.png`
- `maintainer/item12-operator-docs-review.md`

Remaining gate: commit/push parity and the exact content revision's RTD HTML,
PDF and EPUB build/publication. The canonical HTTPS domain is used without
certificate bypass. The separate custom-domain TLS mismatch and all-host
Impeccable update are not undertaken. Full closure requires the hosted evidence
below; repository success alone is not hardware qualification, integrated UI
acceptance or Beta/stable release readiness.
