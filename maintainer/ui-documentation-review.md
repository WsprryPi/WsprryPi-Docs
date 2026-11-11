# Documentation image and wording review

The published manual describes present behavior. Attribution in `docs/About_Wsprry_Pi/index.md` is preserved verbatim. Literal UI labels, command options, API fields, protocol identifiers, and update-comparison rules remain where operators or developers need them.

The UI reference is the clean WsprryPi source checkout at commit `caf8fd4602f1c5e4f2e2cf293ee6283138f2579c`, under `WsprryPi-UI`. The reference files are copied into an ignored local build directory for rendering; the application repository is unchanged.

## Image coverage

- 17 browser captures show the current templates, production styles, and scripts: Operation, light/dark appearance, navigation, controller status, menus, clock, Setup, CW, transmitter controls, Pi I/O, Maintenance recovery, support-request context, and log controls/options.
- Captures use synthetic local station and runtime responses. They do not represent installation, live journal collection, private uploads, physical device tests, or RF qualification. The Logs controls show a disconnected stream. The API-dependent network-safety, update, and private-upload states are documented in prose without simulated success images.
- The two retained UI crops show the unchanged power buttons and Spots source choices. The system data-flow diagrams and QLG3 wiring diagram are retained after visual/source review.
- Redundant detail crops, superseded full-page screenshots, release-number screenshots, unused variants, and the external Imager screenshot are removed. The installation guide links to the vendor's workflow.
- `ui-image-review.json` records all 55 original referenced assets, the 22 retained/replacement references, page ownership, dispositions, and hashes.

## Wording

Release-specific installation pages point to current channel instructions while retaining their inbound URLs. Historical compatibility narratives and future release promises are removed. Configuration, capability, safety, and measurement limits remain expressed as present operating rules. The browser title is independent of documentation release metadata.

## Validation

Activate the repository environment and build:

```bash
source docs/.venv/bin/activate
python -m sphinx -E -a -n -W -b html docs docs/_build/html
```

The complete strict build passes without warnings. All 22 referenced images exist. Browser inspection of Setup, User Interface, Operation, Maintenance, and Logs confirms loaded visible images and no horizontal overflow at the default desktop viewport. Below-fold images use the existing lazy-loading behavior. Image links expose the originals for full-resolution inspection. Attribution matches the original section byte for byte, and `git diff --check` passes.
