# Item 11: documentation performance and Impeccable housekeeping

Date: 2026-10-16. Outcome: item 11 is complete, including the verified devel
build and publication of `dad196e` recorded below. The checklist owner can close
item 11. Items 12–14, integrated application review #423 and 4.0 release
readiness remain open. This file is outside Sphinx's source tree.

## Identity and scope

- Started on clean `devel`, tracking `origin/devel`, at
  `e212ef7a5572cb32cf8e1a38075dd81ec26169bc`. An explicit fetch confirmed 0 ahead,
  0 behind. No reset, stash, rebase, feature branch or fast-forward was needed.
- Final source identities are the SHA-256 values in
  [measurements](item11-measurements.json) and the complete
  [image inventory](item11-image-inventory.json). The integration identity is
  the commit containing this record: `git log -1 --format=%H -- maintainer/item11-docs-performance-review.md`.
  The final report records its pushed SHA and independently read remote SHA.
- Read `AGENTS.md`, README, TODO, PRODUCT, tracked DESIGN, configuration,
  requirements, RTD configuration, both extensions, layout, CSS, accessibility
  JavaScript, existing tests, representative pages and images before editing.
  Reviewed `b2aefee`, `76e3ae9`, `4672d9a`, `a8b2fdc`, `71ea945`, `19c9008`
  and subsequent navigation/Pico changes. In particular, `71ea945` replaced
  two previously compressed screenshots; their current bytes warranted review.
- Application reference: `WsprryPi` devel `a2437d1bf026e91ea95ac7e2a7a0101e3c4f11a1`.
  RP1 reference: devel `80c43dc5dceb10b52e85358d30ae16e4d7b58c4a`, already one
  commit ahead of its upstream. This task made **no writes** to either repository.
  Later checks exposed concurrent item-11-in-progress edits to the application's
  `release_tools/Release Punchlist.md` and RP1's `ROADMAP.md`; these were preserved.
  No transmitter, Pi service, installed application, issue or release was operated.

## Saved reminder dispositions

| Reminder | Current implementation/evidence | Remaining gap | Disposition |
| --- | --- | --- | --- |
| Build-time image loading | `b2aefee`; 51 current content images, 12 eager and 39 lazy in initial HTML; all 51 decode asynchronously and reserve intrinsic dimensions | Single authored dimension and explicit loading were overwritten | Repair required, now repaired with generated-HTML regression coverage |
| Oversized screenshots | Earlier optimization was real; current source corpus is 65 assets / 8,694,460 bytes, including refreshed Setup images | Three referenced PNGs retain worthwhile deflate savings | Repair required, now losslessly recompressed; no derivative or format migration needed |
| Old 1080×1080 / 1.1 MiB logo | Current shared logo is 600×600 / 289,854 bytes, already changed by `b2aefee` | None demonstrated; browser requests it eagerly by default | Completed/already addressed; preserve its pixels, URL and theme markup |
| PRODUCT schema migration | `76e3ae9`; current PRODUCT has `impeccable:product-schema 1`; doctor reports no findings | None | Completed/already addressed |
| Design collateral / sidecar housekeeping | Tracked DESIGN describes the Operator's Bench Manual; current context resolves it and doctor finds no drift | No artifact requiring repair was identified | Completed/already addressed; preserve tracked tooling and documents |
| Host-update reminder | The saved 2026-08-20 #414 reminder explicitly says to update **Impeccable on all hosts**, alongside product/design collateral | Other hosts were not inventoried or updated | Explicitly deferred outside this repository task; installed local skill is 4.1.1, with no `UPDATE_AVAILABLE` notice. This was not an RTD or operating-system upgrade request |
| Deployed waterfall / Core Web Vitals follow-up | Reproducible cold-cache browser lab measurements now retained below | No real-device, field CWV, INP or production-network evidence | Explicitly deferred until such a campaign is separately requested; no field-performance claim |
| Dense sidebar / differing task and tab labels | Existing task hierarchy, exact UI labels and navigation behavior remain usable in the sampled views | No demonstrated navigation defect requiring restructuring | Explicitly deferred; restructure only with concrete clipping/disorientation evidence, outside this bounded performance repair |

## Changes and image integrity

- `docs/_ext/image_delivery.py`: respect any explicit width/height and loading
  choice; leave explicit size/scale interpretation to Sphinx; exclude external
  URI authorities from local-image policy; avoid duplicate decoding/loading
  attributes; keep HTML hints out of non-HTML writers. An environment version
  invalidates builds cached under the old policy.
- `docs/_static/css/custom.css`: reserve a 1em home-icon slot in breadcrumbs.
  Late Font Awesome loading otherwise widened the first crumb just enough to
  wrap a long mobile breadcrumb and move the document. No navigation markup,
  color, font choice, procedure, URL, anchor or application CSS was changed.
- `tests/test_image_delivery.py`: actual strict Sphinx HTML builds cover first
  and subsequent images, explicit width, height, percentages, both dimensions,
  scale, explicit first-image lazy loading, explicit link loading, nested paths,
  linked originals, external/data/SVG images, decoding and incremental reordering.
  LaTeX output verifies that unsized images do not acquire forced pixel sizes.

| PNG | Dimensions | Before bytes | After bytes | Saved |
| --- | --- | ---: | ---: | ---: |
| `docs/User_Interface/Setup/Setup.png` | 3026×1854 | 812,254 | 517,239 | 295,015 |
| `docs/User_Interface/Setup/invalid_callsign.png` | 1322×1172 | 170,030 | 133,472 | 36,558 |
| `docs/User_Interface/Logs/logs.png` | 2454×1860 | 767,751 | 731,525 | 36,226 |
| Total | Unchanged | 1,750,035 | 1,382,236 | 367,799 |

Only concatenated PNG IDAT data was recompressed with zlib level 9. Decompressed
scanlines and all non-IDAT chunks are identical. Independent Pillow comparisons
also confirmed dimensions, mode, decoded pixels and metadata; original/final file
hashes and decoded RGBA hashes are in the inventory. There was no resampling,
crop, palette reduction, metadata stripping, transparency or color conversion.
All three URLs and full-resolution links remain intact. At the nine image-pass
viewports, baseline and image-candidate screenshots were pixel-identical.

The complete authored corpus falls from 8,694,460 to 8,326,661 bytes (4.23%).
The built `_images` directory falls from 6,753,459 to 6,385,660 bytes; the shared
logo is delivered separately from `_static`. Twelve authored assets have no
current page references. Two large unused candidates, `Health_Check.png` and
`Si5351.png`, were deliberately left unchanged after reference inspection.
Existing JPEG files with `.png` names (`rpi_imager.png`, `maintenance.png`) are
also preserved: renaming or re-encoding them is unnecessary for this task.
The inventory uses Git's canonical `Mode_Switch.png` spelling; the existing Mac
working-tree entry is `Mode_switch.png`. Its source reference already uses the
correct Git spelling, so no rename or source repair was needed.

## Browser measurements and visual review

Lab: Chromium 155 through the in-app browser on macOS; desktop 1440×900 and
mobile emulation 390×844; disabled cache; 80 ms latency, 200,000 B/s download,
100,000 B/s upload; 4× CPU throttle. Python serves static files only on
`127.0.0.1:8765`, with no HTTP compression. Sample after the eager load event
plus 1,200 ms. ResourceTiming counts below include the document and completed
resources, excluding favicon; image body bytes exclude response overhead.
Buffered CDP request-event counts were inconsistent and were discarded.

| Page / sampled viewport | Initial requests before → after | Image body bytes before → after |
| --- | ---: | ---: |
| Landing, desktop/mobile | 16 → 16 | 289,854 → 289,854 |
| Setup, desktop/mobile | 18 → 18 | 1,298,380 → 966,807 |
| Logs, desktop/mobile | 16 → 16 | 1,057,605 → 1,021,379 |
| Runtime table/code reference, desktop | 15 → 15 | 289,854 → 289,854 |
| Maintenance, desktop | 19 → 19 | 586,472 → 586,472 |
| Pico-visible Transmitter, mobile | 15 → 15 | 289,854 → 289,854 |

Favicon requests appeared inconsistently in ResourceTiming and are explicitly
excluded from these counts. These are individual samples, not medians.
Setup image transfers including browser-reported response overhead fall from
1,299,580 to 968,007 bytes (25.51%); Logs from 1,058,205 to 1,021,979 (3.42%).
Setup's lab LCP was 10,360 ms before and 8,720/8,700 ms in the final desktop/mobile
confirmation. This is a local throttled observation, not a deployed CWV claim.
The breadcrumb reservation adds 152 bytes to the stylesheet (15,981 → 16,133)
per cold download; it adds no requests.

Chromium fetched Setup's two nearby lazy images even though they were below the
first viewport. Maintenance initially fetched its logo, first image and three
nearby lazy images; nine later content images remained unloaded. Scrolling then
loaded Reset Confirmation, Reset Complete, Test Tone and its frequency-source
image, while the final five remained deferred. The shared logo stays eager;
the first content image stays eager and all content image geometry is unchanged.

The mobile Pico page initially measured lab CLS 0.111683. Buffered layout-shift
attribution identified breadcrumb wrapping as the principal source, not image
dimensions. The icon-slot repair's targeted confirmation measured CLS 0 on that
page and on desktop/mobile Setup. Single-run timing and font arrival can vary.

Batched review covered landing, Setup, Logs, Runtime reference, Maintenance and
the Pico-visible Transmitter page. Observed working: current-page expansion,
breadcrumbs, previous/next, mobile open/close state, Escape returning visible
focus to the opener, default-build search for Si5351, linked 3026×1854 Setup
original, readable labels/alt text, scrollable code and mobile tables without
whole-page overflow. Temporary text-enlargement CSS produced measured 32px
copy from 16px without page overflow; this was a simulation, not browser zoom
or a real-device accessibility certification. OS dark preference retained the
supported white/slate documentation theme; no dark mode was added.

Screenshots, raw samples, shift attribution and build logs remain locally in
ignored `docs/_build/item11-evidence/`; screenshot hashes, representative rendered
sizes, sampling limits and compact results are committed in measurements JSON.
No generated HTML, large logs or screenshots are staged. One `_ready` error from
generated `sphinx_highlight.js` was seen during the session; fresh baseline and
final navigations both had `_ready` defined and no new console errors. Its cause
was not established, and no dependency or third-party file was patched.

## Validation, Impeccable and adversarial reassessment

Local environment: repository `docs/.venv`, Python 3.14.8, Sphinx 9.1.0,
Docutils 0.22.4, MyST 5.1.0, RTD theme 3.1.0. `pip check` passed. Image verification
used bundled Python 3.12.14 / Pillow 12.3.0, without altering the docs environment.
RTD declares Ubuntu 22.04 / Python 3.11; its successful baseline build
[35195553](https://app.readthedocs.org/projects/wsprry-pi/builds/35195553/)
at `e212ef7` actually used Python 3.11 and Sphinx 9.0.4. A Linux/Python 3.11
requirements dry-run resolved successfully; changed Python also parses as 3.11.
No requirements, interpreter, global package or skill files were changed.

All Sphinx commands first activated `source docs/.venv/bin/activate`:

```bash
python -m sphinx -b html -E -a docs docs/_build/item11-baseline-default
WSPRRYPI_DOCS_INCLUDE_PICO=1 python -m sphinx -b html -E -a docs docs/_build/item11-baseline-pico
python -m sphinx -b html -E -a -W --keep-going docs docs/_build/item11-default
WSPRRYPI_DOCS_INCLUDE_PICO=1 python -m sphinx -b html -E -a -W --keep-going docs docs/_build/item11-pico
python -m unittest discover -s tests
python -m sphinx -b latex -E -a -W --keep-going docs docs/_build/item11-latex
python -m sphinx -b epub -E -a -W --keep-going docs docs/_build/item11-epub
```

- Baseline builds: zero warnings; original three tests passed. Final builds:
  zero warnings; all four tests passed. EPUB and LaTeX-source generation passed;
  no local PDF toolchain was installed or PDF compilation claimed.
- Complete local HTML link/fragment/image checks: 52 HTML files per build,
  zero broken targets in baseline/default/Pico outputs. All 51 content-image
  instances have nonempty alt, both dimensions and async decoding; 12 eager,
  39 lazy in both flag states. No new source pages or external-link crawl.
- Actual-corpus default → Pico → default incremental builds passed strict mode:
  all ten gated published sources match the selected source text (decoding
  Sphinx's UTF-8 BOM), WTP search terms and Pico anchors appear only when enabled.
  A copied baseline cache rebuilt without `-E`/`-a` when extension metadata
  changed: `build environment version not current`; old output was refreshed.
- Impeccable 4.1.1: context loader once, optimize, craft-floor, Read guidance,
  doctor (zero findings) and bounded polish/confirmation. HTML detector returned
  no regex findings but explicitly reported degraded parsing; computed contrast
  was unavailable. After the CSS repair, the affected CSS scan returned seven
  pre-existing advisories: three fluid heading endpoints, three admonition border
  colors and the 30px mobile opener. The new rule adds no font/color values;
  these incumbent patterns are retained under DESIGN and the refinement scope.

| Adversarial finding | Severity / reproduction | Repair | Reassessment |
| --- | --- | --- | --- |
| Author sizing/loading erased | P2: strict fixture generated intrinsic 400×200 instead of authored `width:120px`; old transform unconditionally assigned loading | Preserve explicit dimensions/loading; real HTML tests cover clean/incremental cases | Pass; existing pages retain geometry and all loading counts |
| Icon-font breadcrumb movement | P2: mobile Pico long breadcrumb wraps on icon-font arrival; lab CLS ≈0.112 | Fixed-width icon slot using existing font metrics | Pass; targeted final CLS 0, no page overflow |
| Old cached pages could survive extension changes | P2: Sphinx does not track extension source edits as page dependencies | Add environment version | Pass; real baseline environment invalidated automatically |
| Corpus savings confused with reader savings / unused binaries | P2 completion-claim risk: unused candidates do not affect delivered pages; lazy attributes alone do not prove deferred requests | Keep unused assets unchanged; separate corpus, delivered and requested bytes | Pass; measured payloads and actual scroll behavior recorded |
| Detector / platform / hosted overclaim | P2 completion-claim risk: regex fallback, emulated mobile and local Sphinx differ from RTD | Explicit limitations; inspect public RTD evidence and final push checks separately | No unsupported field, device, full-parser or release claim |

A separate in-thread adversarial pass reviewed the whole source/binary diff,
generated behavior, measurements and claims after implementation. Actionable
findings were repaired and affected validation repeated. Final reassessment:
no actionable in-scope finding remains. No separate-agent review is claimed.

## Documentation Impact and handback

Operator procedures, support/band/mode dispositions, hardware qualification,
navigation hierarchy, anchors and URLs are unchanged. Readers receive smaller
identical screenshots, stable breadcrumb layout and correct authored image
sizing/loading. PRODUCT and tracked DESIGN remain unchanged after inspection.

Item 12 still owns API/Phase 15.4 shared resources, Test Tone lifecycle/status,
calibration boundaries, accepted Si5351 readiness/drive/fade, inventory timeout,
RP1 supplement cache/refresh/evidence-status/diagnostic/migration/recovery content,
and materially inaccurate screenshot replacements. No application UI defect or
new hardware-support claim was introduced here. Items 13–14 remain open.

Hosting follow-up: `https://wsprdocs.aa0nt.net/` failed certificate-name validation;
do not bypass it or change hosting administration under this task. Canonical
Read the Docs build/API access works. The repository has no GitHub Actions
workflows or check runs, and no commit statuses on the starting SHA. The final
report must distinguish push parity, the triggered RTD build and publication
verification. This issue does not undo the locally validated repository work.

## Initial post-push verification

At 2026-10-16 11:39 CDT, implementation commit
`bb42bc93129b9673a176fa72fcf85a03c9687475` was successfully pushed to
`origin/devel`. Independent `git ls-remote`, a fresh fetch, HEAD, `origin/devel`
and upstream all agreed on that full SHA, with 0 ahead/behind and a clean tree.
The source hashes in the evidence describe that implementation; this subsequent
record update changes no Sphinx source or test behavior.

GitHub reported zero workflows, check runs and commit statuses; its combined
`pending` value with an empty status list is not a queued check. The repository
webhook listing was empty. Fresh, uncached public RTD queries showed **no build
for the pushed commit**: latest devel build remained successful 35195553 at
`e212ef7`. RTD's public project metadata points at the correct documentation
repository. No automatic build or new publication is verified, and no cause
beyond those observations is asserted. No hosting configuration was changed.

## Hosted build and publication verification

On the owner's explicit follow-up request, **Rebuild version** was invoked for
`devel` through the existing authenticated Firefox RTD session. No hosting,
integration, version, alias or build settings were changed.

[Build 35197280](https://app.readthedocs.org/projects/wsprry-pi/builds/35197280/)
checked out exactly `dad196e706968d48b045c84a550ec4342130196b` and succeeded.
It started on 2026-10-16 at 12:06:36 CDT and finished at 12:07:34 CDT (58 seconds).
The public build API reports `finished`, `success: true`, and no error. The
[raw build log](https://app.readthedocs.org/api/v2/build/35197280.txt) records
Python 3.11.15 / Sphinx 9.0.4, all 16 commands exiting zero, and no Sphinx
`WARNING:` diagnostics. HTML, single-page HTML, PDF compilation and EPUB all
completed successfully. This closes the hosted-environment verification gap.

Publication was independently checked after success at the canonical
[devel documentation](https://wsprry-pi.readthedocs.io/en/devel/): the landing,
[Setup](https://wsprry-pi.readthedocs.io/en/devel/User_Interface/Setup/index.html)
and [Logs](https://wsprry-pi.readthedocs.io/en/devel/User_Interface/Logs/index.html)
pages returned HTTP 200. The served Setup HTML contains its eager first image
and two lazy subsequent images; Logs contains its eager first image. All four
content-image instances retain async decoding, dimensions and nonempty alt text.

Independent HTTPS downloads with cache revalidation also returned HTTP 200
and matched the repository's SHA-256 values byte-for-byte:

| Published asset, relative to `/en/devel/` | Delivered bytes | Identity |
| --- | ---: | --- |
| `_images/Setup.png` | 517,239 | Exact match to `dad196e` and image inventory |
| `_images/invalid_callsign.png` | 133,472 | Exact match to `dad196e` and image inventory |
| `_images/logs.png` | 731,525 | Exact match to `dad196e` and image inventory |
| `_static/css/custom.css` | 16,133 | Exact match to `dad196e` and source hash in measurements |

The successful build's revision and the independently served page/asset results
verify publication of the requested `dad196e` candidate. This subsequent
completion-record commit changes no Sphinx source, asset, test, dependency or
configuration; no publication of that newer record-only commit is claimed.
No local implementation tests were repeated for this maintainer-only update.
Validation used the actual hosted build, served HTML/asset checks, local record
links and staged whitespace/diff review. API results, the raw log, verification
JSON and screenshots are retained locally under ignored
`docs/_build/item11-publication/`; none of those runtime artifacts is committed.

Checklist handback: item 11's implementation, dispositions, review, local
validation and hosted publication verification are complete; item 11 can close.
The separately dispositioned all-host Impeccable update and custom-domain
certificate follow-ups remain outside this task. Items 12–14 remain open and
were not started. Only this documentation-repository completion record is
updated; the WsprryPi checklist and RP1 roadmap are not edited here.
