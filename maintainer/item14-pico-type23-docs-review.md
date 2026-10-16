# Item 14: Pico Type 2/3 operator guidance

October 16, 2026. Bounded operator-documentation candidate prepared on
`codex/step14-pico-type23-docs` from clean `b377bc48bafe7310a5e5e6ef04db7a7e8ace9427`.
Application integration baseline is `af4ce3138177ac488421e7d45808e5c31a54ec4f`,
full accepted companion `6d5e73430bfbacdb8cfc29c3fe41089aa8ae5fcb`, and tested
Pico implementation `804e8a06585ec5a0e650e69fcd71ada398b6cc9f`.
Later Pico roadmap/ongoing development is not substituted for that immutable pin.

## Documentation Impact

Updated four operator paths: Transmitter setup/member resources, REST API,
Signal Setup WSPR and WSPR INI reference. The member table distinguishes
ordinary-six Type 1, compound/four Type 2 without locator, compound/six Type 2/3,
and explicit bracket/six Type 3. Bounds, W1A, suffix ambiguity, requested-call
hashing, receiver context, pair reservation/STOP/reboot and complete atomic saves
remain distinct from readiness, enablement, output inactivity and transmission.
Versioned native routing is separate from stable Pi browser paths; profile
identity remains transactional setup authority. Pi planner preferences remain
host preferences and do not control Pico's automatic station planning.

Considered unchanged: existing recovery/troubleshooting instructions already
require explicit readback/review and prohibit replay; no save or login proves an
interrupted write committed. Existing setup screenshots still identify the same
controls; none depicts the corrected station hint as an instruction. No image
replacement or visibility-gating change is required. P15.9 is not implemented
or documented as available. No schema, protocol or application code is changed
in this repository.

The operator subsequently authorized promotion to Docs devel and its automatic
Read the Docs publication. Final promotion/parity and exact-content hosted build
verification are required after this record commit; their actual results belong
in the Pi item 14 acceptance record and final handoff. No manual publication,
release, tag or announcement is introduced by this record.

## Validation

Used the repository's existing `docs/.venv` (linked only for local tooling
in the isolated worktree). Commands from repository root:

```sh
source docs/.venv/bin/activate
python -m unittest discover -s tests
python -m sphinx -b html -W --keep-going -E -a docs docs/_build/step14-default
WSPRRYPI_DOCS_INCLUDE_PICO=1 python -m sphinx -b html -W --keep-going -E -a docs docs/_build/step14-pico
python -m sphinx -b epub -W --keep-going -E -a docs docs/_build/step14-epub-default
WSPRRYPI_DOCS_INCLUDE_PICO=1 python -m sphinx -b epub -W --keep-going -E -a docs docs/_build/step14-epub-pico
python -m sphinx -b latex -W --keep-going -E -a docs docs/_build/step14-latex-default
WSPRRYPI_DOCS_INCLUDE_PICO=1 python -m sphinx -b latex -W --keep-going -E -a docs docs/_build/step14-latex-pico
git diff --check
```

All four behavioral tests and all six strict builds pass with zero Sphinx
warnings. Both EPUB archives were inspected: the new Pico section is present
only in the enabled build. Existing tests also verify source/search/navigation
visibility. Links resolve in strict builds; the old station/1 example is
explicitly legacy and requires the exact loaded /2 schema for current firmware.
A fresh independent reviewer corrected two P2 documentation findings: a
universal unsupported-format HTTP status and an ambiguously applicable legacy
JSON example. Both were repaired and reassessed against native/API tests.

Actual default/Pico PDFs compile with `latexmk -pdf -interaction=nonstopmode
-halt-on-error WsprryPi.tex` in disposable Debian container
`wsprrypi-step14-pdf` based on `wsprrypi-item10:local`; tools are installed only
inside that container. Default is 134 pages; Pico is 146 pages. No TeX error or
LaTeX/package warning occurs. Whole-book advisories are default 54 overfull / 68 underfull hboxes and Pico
54 / 90, plus incumbent vertical-box advisories; this
is affected-page review rather than full-book print reflow. Affected table,
planning prose, versioned API and JSON pages (PDF indices 40, 41, 112, 113) were
rendered with Poppler and visually inspected for clipping/overlap.

Impeccable 4.1.1 preserves PRODUCT/DESIGN's Read the Docs shell and reading
hierarchy. The actual built Transmitter table and API guidance were reviewed in
the in-app browser at desktop 1280x900 and mobile 390x844; API 200% text has
390-pixel document width without horizontal overflow. Source and rendered
paragraph scope links were reviewed. The detector reports no mechanical findings
but rendered HTML explicitly degrades to regex because optional parser modules
are absent; selector/computed-contrast coverage is not claimed. No stylesheet
or screenshot changes are introduced.

Runtime artifacts remain outside Git under `/private/tmp/wsprrypi-step14`:
`docs-*.log`, `pdf-*-final.log`, `docs-visual/`, `pdf-visual/`, and detector output.
The isolated Python server is loopback-only. Browser overrides are reset and
temporary tabs closed. No Pi, transmitter, target service or installed runtime
is operated. Original Docs devel and unrelated worktrees remain preserved.
