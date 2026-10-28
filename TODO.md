# TODO: Documentation Updates for Upcoming Release

## High Priority

### Core Transmission & Backend Changes

- [ ] Document Raspberry Pi 5 support and GPIO limitations
- [ ] Update backend selection (GPIO vs Si5351) behavior and constraints
- [ ] Document GPIO resolver changes and multi-chip handling
- [ ] Clarify transmission stop behavior improvements
- [ ] Document CW/QRSS/FSKCW/DFCW execution and timing updates
- [ ] Explain paired WSPR transmission contract and scheduler behavior
- [ ] Add documentation for selector GPIO lifecycle and deterministic handling

### Configuration & CLI

- [ ] Update canonical configuration schema (Operation vs Runtime, etc.)
- [ ] Document new CLI options and planner preference behavior
- [ ] Clarify frequency parsing and accepted formats
- [ ] Document PPM limits and normalization behavior
- [ ] Update CW defaults (shift, base frequency, timing gaps)
- [ ] Document removal of deprecated/legacy config fields
- [ ] Clarify Band GPIO explicit-only behavior

### Si5351 Backend

- [x] Document Si5351 configuration (I2C, reference, outputs) — item 12 reconciles bounded inventory, saved-state, drive and readiness in Setup, CLI and INI references.
- [ ] Explain backend-specific behavior differences vs GPIO
- [ ] Document unused output parking behavior
- [x] Clarify test-tone and direct CLI transmit behavior — item 12 documents acceptance, activity, cleanup/restoration and prior direct-tone restoration.

---

## Medium Priority

### UI / Web Interface

- [ ] Document new Operation landing page and navigation changes
- [ ] Update Setup vs Operation separation
- [x] Document autosave behavior and validation flow — item 12 separates host autosave, Fleet saves and member Load/Validate/scoped saves.
- [ ] Explain offline/online handling and retry logic
- [ ] Document new runtime state model and status indicators
- [ ] Update logs, spots, and maintenance UI behavior
- [ ] Document websocket-based control flow (Stop, status updates)

### API / Backend Services

- [ ] Document fetch_spots API changes and validation requirements
- [ ] Explain caching behavior and TTL handling
- [ ] Document fallback behavior for wspr.live sources
- [ ] Clarify normalized JSON response format

### Logging & Diagnostics

- [ ] Document UDP sender, attached-Pico forwarding, Pi collector, both management UIs, origin/relay provenance, source filters, plaintext trust, local-send semantics, service/installer lifecycle and retention after implementation passes the [canonical coordinated acceptance plan](https://github.com/WsprryPi/WsprryPico/blob/devel/engineering/development/udp-syslog-proposal.md). Proposal reviewed; feature implementation and runtime acceptance pending. Refresh this documentation branch against the intended current operator-docs baseline before writing instructions or screenshots; do not present UDP as available.

- [ ] Document logging changes and debug configuration
- [ ] Explain improved error messaging and diagnostics
- [ ] Document new debug and runtime observability improvements

---

## Lower Priority

### UI Polish & Accessibility

- [ ] Document accessibility improvements (ARIA, semantics)
- [ ] Update theming and layout behavior documentation
- [ ] Document responsive behavior changes

### Testing & Validation

- [ ] Update documentation for new regression tests
- [ ] Document expected behavior for edge cases (reloads, stop, planner errors)

### Miscellaneous

- [ ] Update installer behavior (Pi 5, reboot logic, I2C handling)
- [ ] Document minor behavior changes and cleanup items
- [ ] Update codebase map and developer documentation

---

## Cleanup / Verification

- [ ] Remove references to deprecated features in docs
- [ ] Ensure consistency between CLI, UI, and backend documentation
- [ ] Verify examples match current behavior
- [ ] Update README and quick-start guides
- [ ] Add release notes summary section

---

## Optional Enhancements

- [ ] Add diagrams for scheduler and execution flow
- [ ] Add examples for common configurations (GPIO vs Si5351)
- [ ] Provide troubleshooting section for common failures
- [ ] Add migration guide from previous versions
