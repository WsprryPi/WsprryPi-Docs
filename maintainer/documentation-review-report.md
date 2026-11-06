# Complete handbook prose and organization review

## Scope and execution

Requested execution prompt: [documentation-review-prompt.md](documentation-review-prompt.md).
Work started on clean `devel` at `59a16d4`. The original Sphinx corpus contained
55 Markdown pages. The review followed the original depth-first toctree order,
then the unlisted historical experimental page. Fenced code blocks and configuration
examples were excluded from proofreading. Inline technical terms were retained
for context and protected when interpreting suggestions. Headings, paragraphs, list prose,
table prose, and admonition prose were included. Git retains exact originals.

**Grammarly-validated: original prose coverage on all 55 pages.** The authenticated
Grammarly web editor was used, with individual editorial decisions applied to
Markdown source. Suggestions were not accepted in bulk. The new requirements
and first-transmission pages, and substantially revised pages, receive a separate
final-pass entry below. A page needing no change still appears in the ledger.
No review of companion-repository files, hardware, or on-air behavior is claimed.

The temporary review document remains in the user's Grammarly account:
[WsprryPi handbook review](https://coda.grammarly.com/d/_dU0MkgfkPWt).
Its numbered batches retain source-page markers. Proofreading scores below are
observed original-batch scores, not final scores or measures of technical accuracy.
Markup fragments and merged inline-code boundaries in the extracts were treated
as extraction artifacts and never copied back to source. Some suggestions changed
as analysis settled. Counts are observations, not a
claimed sum of independent errors.

AI Detector initially ran on the landing-page prose alone (12%, one weak part).
Automatic approval review then blocked further detector processing as outside
explicit proofreading consent. The user subsequently authorized detector checks;
the complete original corpus was then checked in the batches below. Results
are advisory resemblance signals, not authorship findings. Batch scores are not
per-page scores. Source markers, headings, and table prose can affect them.
Passage-level highlights were not reliably readable in the narrow editor view;
no invented highlighted excerpts or authorship conclusion is reported.

## Changes

- Replaced the landing page's version-led introduction with a direct explanation
  of the transmitter, output choices, and a numbered beginner path.
- Added **What you need** and **Your first WSPR transmission**, covering hardware,
  RF preparation, the browser and Pi, configuration, starting, reception reports,
  and deliberate shutdown.
- Put project information, requirements, installation, and first operation in
  Start Here. Protocol background remains linked from the introduction and in
  reference navigation. Optional beta, USB-host, and Pico guides have their own
  navigation group. Troubleshooting and support precede advanced references.
- Put transmitter and signal setup before operation in the UI navigation, followed
  by reception reports, logs, and maintenance. Kept existing source URLs and
  anchors; retained historical experimental material outside normal navigation.
- Moved attribution below compatibility and qualification information without
  removing it. Kept qualification tables and RF warnings.
- Applied Oxford commas, spelling and agreement fixes, a sentence-fragment repair,
  and targeted wording improvements. Preserved identifiers, UI labels, technical
  quantities, requirement strength, and code examples.

## Adversarial assessments

### Round 1: findings and repairs

1. **Pi 5 GPIO contradiction:** Operations still said GPIO was unsupported and
   automatically selected Si5351. Replaced that obsolete path with the existing
   installer-managed RP1 route-selection workflow. Development's dedicated-hardware
   wording and the undefined Compute Module 5 restriction were reconciled with
   the current backend guidance, without changing untested model status.
2. **Protocol error:** About WSPR described Type 3 as inherently two-frame and
   Operations assigned hashing to Type 2 while calling Type 3 reversible. Checked
   the [official WSJT-X protocol reference](https://wsjtx.github.io/wsjtx/guide-full.html)
   and corrected frame formats separately from WsprryPi's paired scheduling.
3. **Band-scope contradiction:** The GPIO FAQ applied legacy PLLD restrictions
   to all GPIO hardware, including qualified Pi 5 12 m output. Scoped those
   findings to the tested legacy profiles and linked the authoritative table.
4. **Beginner navigation gaps:** Optional installation branches interrupted the
   main path; operation preceded setup; no consolidated prerequisites or first
   transmission procedure existed. Added the two guides and reordered toctrees.
5. **Landing-page overload:** The complete nested TOC repeated navigation below
   the introductory prose. Hidden root toctrees now retain the sidebar while
   the page provides a concise guided path.
6. **Editorial defects:** Fixed the four-links/three-pages mismatch, WSPRnet typo,
   `wil`, `frane`, `ay`, `dlownloader`, redundant transmission-control wording,
   and the configuration-repair sentence fragment.

### Round 2: verification

Rechecked the corrected text and the complete rendered handbook. All 57 sources
are discovered by Sphinx; the historical experimental page remains intentionally
outside normal navigation. Root and UI toctrees follow the operator path.
The complete internal file/fragment audit reports zero missing targets.
Protected code examples and qualification tables retain their values; the
removed obsolete inline redirect is accounted for above. `git diff --check`
passes. The fresh warnings-as-errors build and extension test pass.

No actionable issue remains in the changed content, navigation, or local build
within this review's scope. This is documentation verification, not a new
hardware qualification or an exhaustive revalidation of all historical claims.
A rendered-page check also caught an overlong optional-setup sidebar caption;
it was shortened to **Optional Setups** without changing theme behavior.
The final Grammarly pass prompted shorter Operations prose and another detector
check of that revised scope.

## Page coverage in original reading order

| Order | Source | Grammarly batch | Proofreading |
| --- | --- | --- | --- |
| 1 | `docs/index.md` | 01 | Reviewed |
| 2 | `docs/About_WSPR/index.md` | 01 | Reviewed |
| 3 | `docs/About_Wsprry_Pi/index.md` | 01 | Reviewed |
| 4 | `docs/Install/index.md` | 02 | Reviewed |
| 5 | `docs/Install/beta1.md` | 02 | Reviewed |
| 6 | `docs/Install/linux_si5351.md` | 03 | Reviewed |
| 7 | `docs/Install/macos_si5351.md` | 03 | Reviewed |
| 8 | `docs/Install/pico.md` | 04 | Reviewed |
| 9 | `docs/User_Interface/index.md` | 04 | Reviewed |
| 10 | `docs/User_Interface/Operations/index.md` | 05 | Reviewed |
| 11 | `docs/User_Interface/Setup/index.md` | 05 | Reviewed |
| 12 | `docs/User_Interface/Setup/Signal_Setup/index.md` | 05 | Reviewed |
| 13 | `docs/User_Interface/Setup/Signal_Setup/wspr.md` | 05 | Reviewed |
| 14 | `docs/User_Interface/Setup/Signal_Setup/cw.md` | 06 | Reviewed |
| 15 | `docs/User_Interface/Setup/Transmitter/index.md` | 07 | Reviewed |
| 16 | `docs/User_Interface/Setup/Pi_IO/index.md` | 08 | Reviewed |
| 17 | `docs/User_Interface/Logs/index.md` | 08 | Reviewed |
| 18 | `docs/User_Interface/Spots/index.md` | 08 | Reviewed |
| 19 | `docs/User_Interface/Maintenance/index.md` | 09 | Reviewed |
| 20 | `docs/User_Interface/Maintenance/support_bundle.md` | 09 | Reviewed |
| 21 | `docs/User_Interface/Maintenance/network_safety.md` | 10 | Reviewed |
| 22 | `docs/Command_Line_Operations/index.md` | 10 | Reviewed |
| 23 | `docs/Command_Line_Operations/quick_start.md` | 10 | Reviewed |
| 24 | `docs/Command_Line_Operations/wspr_options.md` | 10 | Reviewed |
| 25 | `docs/Command_Line_Operations/transmitter_backends.md` | 10 | Reviewed |
| 26 | `docs/Command_Line_Operations/cw_modes.md` | 10 | Reviewed |
| 27 | `docs/Command_Line_Operations/service_test_controls.md` | 10 | Reviewed |
| 28 | `docs/Advanced_Operations/index.md` | 11 | Reviewed |
| 29 | `docs/Advanced_Operations/timing_calibration.md` | 11 | Reviewed |
| 30 | `docs/Advanced_Operations/canonical_bands.md` | 12 | Reviewed |
| 31 | `docs/Advanced_Operations/ini_configuration.md` | 12 | Reviewed |
| 32 | `docs/Advanced_Operations/ini_configuration/runtime.md` | 12 | Reviewed |
| 33 | `docs/Advanced_Operations/ini_configuration/transmitter_backends.md` | 13 | Reviewed |
| 34 | `docs/Advanced_Operations/ini_configuration/wspr.md` | 13 | Reviewed |
| 35 | `docs/Advanced_Operations/ini_configuration/cw_and_band_gpio.md` | 13 | Reviewed |
| 36 | `docs/Advanced_Operations/ini_configuration/complete_example.md` | 13 | Reviewed |
| 37 | `docs/Advanced_Operations/configuration_troubleshooting.md` | 13 | Reviewed |
| 38 | `docs/Advanced_Operations/rest_api.md` | 14 | Reviewed |
| 39 | `docs/Advanced_Operations/websocket.md` | 14 | Reviewed |
| 40 | `docs/Advanced_Operations/rp1_gpclk.md` | 15 | Reviewed |
| 41 | `docs/Advanced_Operations/rf_electrical.md` | 15 | Reviewed |
| 42 | `docs/Support/index.md` | 15 | Reviewed |
| 43 | `docs/Additional_Reading/validation_platform.md` | 15 | Reviewed |
| 44 | `docs/Internals/index.md` | 15 | Reviewed |
| 45 | `docs/Development/index.md` | 15 | Reviewed |
| 46 | `docs/User_Interface/Maintenance/update_check.md` | 16 | Reviewed |
| 47 | `docs/User_Interface/Maintenance/update_check/ui_build_polling.md` | 16 | Reviewed |
| 48 | `docs/User_Interface/Maintenance/update_check/github_update_polling.md` | 16 | Reviewed |
| 49 | `docs/User_Interface/Maintenance/update_check/prompts_and_state.md` | 16 | Reviewed |
| 50 | `docs/User_Interface/Maintenance/update_check/developer_validation.md` | 16 | Reviewed |
| 51 | `docs/FAQ/index.md` | 16 | Reviewed |
| 52 | `docs/FAQ/why_12m_looks_noisy.md` | 16 | Reviewed |
| 53 | `docs/FAQ/lowpass-filter-justification.md` | 16 | Reviewed |
| 54 | `docs/Additional_Reading/index.md` | 16 | Reviewed |
| 55 | `docs/Experimental/rp1_gpio.md` | 17 | Reviewed |

## Original batch observations

| Batch | Source-page orders | Writing score | Suggestions observed | AI resemblance | Flagged parts |
| --- | --- | --- | --- | --- | --- |
| 01 | 1, 2, 3 | 96 | 23 | 18% | 11 |
| 02 | 4, 5 | 94 | 50 | 46% | 29 |
| 03 | 6, 7 | 97 | 18 | 82% | 38 |
| 04 | 8, 9 | 92 | 57 | 61% | 31 |
| 05 | 10, 11, 12, 13 | 87 | 80 | 21% | 11 |
| 06 | 14 | 90 | 26 | 40% | 7 |
| 07 | 15 | 92 | 96 | 71% | 73 |
| 08 | 16, 17, 18 | 87 | 65 | 53% | 22 |
| 09 | 19, 20 | 96 | 37 | 52% | 40 |
| 10 | 21, 22, 23, 24, 25, 26, 27 | 95 | 43 | 43% | 35 |
| 11 | 28, 29 | 97 | 21 | 71% | 34 |
| 12 | 30, 31, 32 | 96 | 20 | 62% | 36 |
| 13 | 33, 34, 35, 36, 37 | 94 | 44 | 73% | 45 |
| 14 | 38, 39 | 94 | 34 | 77% | 42 |
| 15 | 40, 41, 42, 43, 44, 45 | 95 | 44 | 54% | 41 |
| 16 | 46, 47, 48, 49, 50, 51, 52, 53, 54 | 93 | 60 | 49% | 51 |
| 17 | 55 | 98 | 4 | 79% | 13 |

## Final prose pass

Final batches review the substantially revised pages and the two new pages.
The new `docs/requirements.md` was reviewed in batch 18, and
`docs/first_transmission.md` in batch 19. This brings coverage to all 57 final
Sphinx sources. They have different scopes from the original batches, so the percentages are
not presented as directly comparable before/after improvements. Minor
punctuation corrections after a check do not constitute a whole-document rescore.

| Final batch | Scope | Writing score | Suggestions observed | AI resemblance | Flagged parts |
| --- | --- | --- | --- | --- | --- |
| 18 | Landing page, About WsprryPi, About WSPR, What you need | 98 | 16 | 41% | 23 |
| 19 | Installation and first transmission | 97 | 31 | 53% | 30 |
| 20 | UI overview, operation, CW setup, development | 95 | 47 | 35% | 27 |
| 21 | FAQ, GPIO findings, historical experiment | 98 | 9 | 62% | 26 |
| 22 | Shortened Operations and CW text, checked again | 93 | 30 | 30% | 10 |

## Validation and delivery

- Baseline and revised fresh HTML builds passed with warnings treated as errors.
- Command: `source docs/.venv/bin/activate` followed by
  `python -m sphinx -E -a -b html -n -W --keep-going docs docs/_build/html`.
- Extension tests: `python -m unittest discover -s tests -p 'test_*.py' -v`;
  one test passed.
- Rendered internal file and fragment references were checked across the entire
  HTML output; zero missing targets were found.
- Protected fenced code/configuration examples were compared with Git originals.
  The sole removed inline literal was the obsolete Pi 5 automatic-Si5351 redirect
  URL, replaced with the current transmitter guide.
- Rendered desktop navigation and the beginner entry path were inspected in the
  browser. No theme, CSS, sidebar-search implementation, or mobile-script changes
  were made. Mobile behavior is not claimed as independently qualified.
- Delivery targets `origin/devel`. The existing **Handbook validation** workflow
  builds the documentation on each devel push; Read the Docs publication is a
  separate service. Exact pushed commit and observed remote-build results are
  reported in the completion message, since they are only known after this report
  is committed.

## Suggestions not applied

The following numbered dispositions cover rejected recommendations. Repeated
optional style suggestions are grouped with their count and affected wording;
source-page ranges refer to the coverage ledger. Labels, commands, protocol
fields, cited titles, and fragmentary table entries are not ordinary sentences.
A retained sentence is a deliberate editorial decision, not an unresolved request
for user approval. Detector findings are listed separately from proofreading.

| Item | Location | Grammarly recommendation or finding | Reason not applied / disposition |
| --- | --- | --- | --- |
| 1 | Batch 01, pages 1, 2, 3 | 4 optional wording recommendations: page 2: “Joe estimated that…”; page 3: “As of Version 2.0+…”; page 3: “is specific to…”; page 3: “Harmonic operations are…” | Retained wording where the proposed stylistic rewrite was unnecessary or reduced technical specificity; small independent corrections may still have been made in the same paragraph. |
| 2 | Batch 02, pages 4, 5 | 20 optional wording recommendations: page 4: “is supplied with…”; page 4: “all the bells and whistles…”; page 4: “Each time I update…”; page 4: “Use Internet resources…”; page 4: “is used to…”; page 4: “that is especially…”; page 4: “It installs Python and libusb…”; page 4: “WsprryPi uses the RPi PWM…”; page 4: “The provider reports its version…”; page 4: “Unexpected changes to installed code…”; page 4: “If backup creation or verification fails…”; page 4: “Recover any desired customization…”; page 4: “Keep the reported locations…”; page 4: “The IP address of your Raspberry Pi…”; page 4: “The installer packages…”; page 5: “The installer chooses the matching download…”; page 5: “When installation finishes…”; page 5: “The shared Pico firmware-maintenance installer…”; page 5: “Existing verified tools…”; page 5: “Please send a support bundle…” | Retained wording where the proposed stylistic rewrite was unnecessary or reduced technical specificity; small independent corrections may still have been made in the same paragraph. |
| 3 | Batch 03, pages 6, 7 | 10 optional wording recommendations: page 6: “There is no direct HID transport…”; page 6: “Use the boards' documented STEMMA QT wiring…”; page 6: “Define the exact frequency, mode, bounded duration, stop procedure…”; page 7: “Use the boards' documented STEMMA QT connection…”; page 7: “A universal executable…”; page 7: “is used with…”; page 7: “Do not shorten, decode, or manufacture…”; page 7: “Only the explicitly selected address…”; page 7: “NACK, short or partial transfers…”; page 7: “Define the exact frequency, mode, bounded duration, and output-disable…” | Retained wording where the proposed stylistic rewrite was unnecessary or reduced technical specificity; small independent corrections may still have been made in the same paragraph. |
| 4 | Batch 04, pages 8, 9 | 15 optional wording recommendations: page 8: “The companion…”; page 8: “Check the Pico manual…”; page 8: “Keep output inactive…”; page 8: “Reading a setting…”; page 8: “Fleet WSPR assignments instead take…”; page 8: “These intervals are independent…”; page 8: “Trust local reference for Pico rate…”; page 9: “The page has just opened…”; page 9: “Documentation:…”; page 9: “The icon on the left…”; page 9: “When selected, the transmission LED…”; page 9: “UTC time…”; page 9: “is intended to…”; page 9: “Both accepted choices…”; page 9: “Saved assignments on the controller…” | Retained wording where the proposed stylistic rewrite was unnecessary or reduced technical specificity; small independent corrections may still have been made in the same paragraph. |
| 5 | Batch 05, pages 10, 11, 12, 13 | 14 retained optional wording recommendations: page 10: “is provided to protect…”; page 10: “They do not bypass startup hardware safety…”; page 10: “For the **Si5351** backend…”; page 10: “Correct the hardware or configuration problem…”; page 10: “When enabled, the transmitter…”; page 10: “Type2Type3Paired…”; page 11: “This card is where…”; page 11: “for Raspberry Pi…”; page 11: “Confirm the output, then enter…”; page 13: “the initial alternate profile…”; page 13: “to manually calibrate their rig…”; page 13: “the behavior…”; page 13: “to always use a paired Type 2 and 3…”; page 13: “For those who want the additional data…” | Retained wording where the proposed stylistic rewrite was unnecessary or reduced technical specificity; small independent corrections may still have been made in the same paragraph. |
| 6 | Batch 06, pages 14 | 8 optional wording recommendations: page 14: “CW Mode, using one of…”; page 14: “In contrast, QRSS transmitters…”; page 14: “This mode, when displayed…”; page 14: “QRSS1…”; page 14: “permits editing…”; page 14: “Its spacing uses…”; page 14: “an explicit value of…”; page 14: “as soon as…” | Retained wording where the proposed stylistic rewrite was unnecessary or reduced technical specificity; small independent corrections may still have been made in the same paragraph. |
| 7 | Batch 07, pages 15 | 24 optional wording recommendations: page 15: “The switch…”; page 15: “The selected pin is reserved…”; page 15: “Selecting the Si5351 backend releases…”; page 15: “one assignment is changed or disabled…”; page 15: “Actual output should be measured…”; page 15: “is tied to…”; page 15: “If it does not respond…”; page 15: “Ordinary configuration and status reads…”; page 15: “authority to use it…”; page 15: “are supplied with…”; page 15: “as well as…”; page 15: “selected nearby device…”; page 15: “Plain LAN's reported ID…”; page 15: “On first use…”; page 15: “can be obtained…”; page 15: “Latest verified CI image…”; page 15: “Closing USB or a network connection…”; page 15: “A USB connection uses…”; page 15: “Enter a new password…”; page 15: “Re-enable it using…”; page 15: “The redacted saved password…”; page 15: “A discovery advertisement…”; page 15: “A draft belonging to another Pico…”; page 15: “Amplifier pin and polarity can be set…” | Retained wording where the proposed stylistic rewrite was unnecessary or reduced technical specificity; small independent corrections may still have been made in the same paragraph. |
| 8 | Batch 08, pages 16, 17, 18 | 17 optional wording recommendations: page 16: “You may use the dropdown…”; page 16: “A retained conflict remains visible…”; page 16: “Most amplifiers allocate…”; page 16: “A relay, SSR…”; page 16: “This section allows you…”; page 17: “Each Pico is identified…”; page 17: “The source selector and Pico log prefixes…”; page 17: “When disconnected, this button reads…”; page 17: “An empty view does not mean…”; page 17: “of them…”; page 17: “USB forwarding can be checked…”; page 17: “Restart or journal rotation…”; page 17: “have independent admission…”; page 17: “Keep the recovery firmware bundle…”; page 17: “Discarded history cannot be recovered…”; page 17: “rather than…”; page 18: “It defaults to the…” | Retained wording where the proposed stylistic rewrite was unnecessary or reduced technical specificity; small independent corrections may still have been made in the same paragraph. |
| 9 | Batch 09, pages 19, 20 | 18 optional wording recommendations: page 19: “be presented with…”; page 19: “You will need to reconfigure…”; page 19: “is useful for checking…”; page 19: “as soon as…”; page 19: “The preview adds…”; page 19: “When the accepted target matches…”; page 19: “On the legacy GPIO backend…”; page 19: “rather than…”; page 19: “You must re-enable…”; page 19: “is a preview of…”; page 19: “to quietly show…”; page 19: “to never check again…”; page 19: “If you choose to never check again…”; page 20: “Leave it off when…”; page 20: “UTC time…”; page 20: “Configuration-like text files…”; page 20: “anything should be excluded…”; page 20: “Neither is confirmation that…” | Retained wording where the proposed stylistic rewrite was unnecessary or reduced technical specificity; small independent corrections may still have been made in the same paragraph. |
| 10 | Batch 10, pages 21, 22, 23, 24, 25, 26, 27 | 9 optional wording recommendations: page 21: “VPNs, tunnels, bridges…”; page 22: “when you need…”; page 23: “Scientific notation and fractional-hertz…”; page 24: “no special option is usually needed…”; page 25: “The second command still fails…”; page 25: “After editing a monitored INI file…”; page 25: “Recovery does not resume interrupted work…”; page 25: “prove…”; page 27: “make a direct one-shot command start the managed server…” | Retained wording where the proposed stylistic rewrite was unnecessary or reduced technical specificity; small independent corrections may still have been made in the same paragraph. |
| 11 | Batch 11, pages 28, 29 | 12 optional wording recommendations: page 29: “WsprryPi uses wall-clock time…”; page 29: “UTC time…”; page 29: “A system clock frequency estimate…”; page 29: “Measurements expire after 30 seconds…”; page 29: “Clock-tree access…”; page 29: “direct PPS is selected…”; page 29: “The conducted steady tones…”; page 29: “cannot be used…”; page 29: “An existing canonical value…”; page 29: “Set **Residual PPM**…”; page 29: “Record a separately measured…”; page 29: “Zero-beating a nearby AM carrier…” | Retained wording where the proposed stylistic rewrite was unnecessary or reduced technical specificity; small independent corrections may still have been made in the same paragraph. |
| 12 | Batch 12, pages 30, 31, 32 | 2 optional wording recommendations: page 30: “The numeric dial must correlate…”; page 32: “After interrupted work…” | Retained wording where the proposed stylistic rewrite was unnecessary or reduced technical specificity; small independent corrections may still have been made in the same paragraph. |
| 13 | Batch 13, pages 33, 34, 35, 36, 37 | 14 optional wording recommendations: page 33: “Requests for unqualified combinations…”; page 33: “There is no…”; page 33: “UTC uncertainty is displayed…”; page 33: “It requires transmission to be disabled…”; page 33: “Keep transmission disabled until…”; page 35: “Numeric-looking content…”; page 37: “The invalid draft remains…”; page 37: “This inline state identifies…”; page 37: “At every daemon start…”; page 37: “the safe state cannot be confirmed…”; page 37: “Do not edit provider files…”; page 37: “Eligibility and cleanup must also be accepted…”; page 37: “If the installer reports an ownership…”; page 37: “explains…” | Retained wording where the proposed stylistic rewrite was unnecessary or reduced technical specificity; small independent corrections may still have been made in the same paragraph. |
| 14 | Batch 14, pages 38, 39 | 6 optional wording recommendations: page 38: “perform fresh validation of…”; page 38: “An off-LAN request is rejected…”; page 38: “Evidence not collected…”; page 38: “A temporary disconnect is not proof…”; page 38: “Application includes station…”; page 39: “Apache cannot authorize individual commands…” | Retained wording where the proposed stylistic rewrite was unnecessary or reduced technical specificity; small independent corrections may still have been made in the same paragraph. |
| 15 | Batch 15, pages 40, 41, 42, 43, 44, 45 | 16 optional wording recommendations: page 40: “After that step…”; page 40: “Existing attributable WsprryPi ownership…”; page 40: “Manual edits to installed provider code…”; page 40: “Downgrades require…”; page 40: “that it was removed…”; page 40: “Pre-existing or modified operator data…”; page 40: “Provider recovery evidence…”; page 40: “Runtime readiness, exclusive ownership…”; page 40: “There is no automatic route or backend fallback…”; page 40: “Failure to inspect remains unknown…”; page 41: “The GPIO RF backend uses…”; page 41: “The install script disables…”; page 41: “The GPIO RF backend produces…”; page 41: “The expected RF power output…”; page 42: “The WsprryPi Support GPT can help…”; page 43: “source for Chrony…” | Retained wording where the proposed stylistic rewrite was unnecessary or reduced technical specificity; small independent corrections may still have been made in the same paragraph. |
| 16 | Batch 16, pages 46, 47, 48, 49, 50, 51, 52, 53, 54 | 9 optional wording recommendations: page 46: “outdated…”; page 47: “The endpoint also reports…”; page 50: “The GitHub compare status…”; page 51: “If this happens…”; page 52: “Testing with the 500 MHz…”; page 52: “distribution of energy…”; page 52: “On 6 m, the output…”; page 52: “On 2 m, no usable…”; page 53: “The 12 m and 6 m failures…” | Retained wording where the proposed stylistic rewrite was unnecessary or reduced technical specificity; small independent corrections may still have been made in the same paragraph. |
| 17 | Batch 17, pages 55 | 3 optional wording recommendations: page 55: “It must not be generalized…”; page 55: “Remove the experimental overlay…”; page 55: “Current installation, both-route evidence…” | Retained wording where the proposed stylistic rewrite was unnecessary or reduced technical specificity; small independent corrections may still have been made in the same paragraph. |
| 18 | Initial single-page extraction | Add a period after “Pico” and treat wrapped lines as separate sentences | Soft line breaks were initially imported as paragraph breaks. Re-extracted normalized paragraphs for the full review; these were extraction artifacts. |
| 19 | Pages 4–5, installation | Rewrite `locally_modified`; add spaces or complete a sentence around `.local` | These are literal state values and hostname syntax. |
| 20 | Page 4, Uninstall | Pluralize application, service, and configuration | These words jointly modify “files”; the singular category names are correct. |
| 21 | Page 4, installer messages | Rewrite the period or “local” adjacent to the hostname example | Kept literal `{name}.local` and installer text. |
| 22 | Pages 4, 8, 14–17, 19, 21, 25, 27, 29, 37, 41, 50 | Inclusive-language rewrites of disable, disabled, disables, or Disabling | Technical controls and output states refer to disabling software or RF. Replacements would obscure the instructions. |
| 23 | Page 6, Linux USB I2C | Inclusive-language rewrite of slave | Preserved Linux I2C capability terminology. |
| 24 | Page 6, identity helper | Remove a space at the end of `si5351-adapter-identity` | The command is protected inline code; sentence punctuation is outside its delimiter. |
| 25 | Page 7, macOS examples | Rewrite “. Replacewith” or correct “Replacewith” | Placeholders and inline command boundaries merged in the prose extract; original source syntax remains intact. |
| 26 | Page 8, Pico introduction | Change “owns” | The subject is the singular companion manual. Replacing the verb as suggested is not needed. |
| 27 | Page 8, controls | Change “selects”, “Require”, or add a semicolon after the quoted filter choice | These are quoted UI labels serving as subjects. The full label is one control. |
| 28 | Page 8, firmware | Add an article before “first” | The linked “first firmware installation” is a workflow title. |
| 29 | Page 8, Pico safety | Insert periods after operation, firmware, deliberately, or member | These occur in headings or labels rather than incomplete prose sentences. |
| 30 | Page 9, navbar and clock | Change “at”, remove UTC time, or punctuate “before” and “clock” | Kept spatial navigation wording and the distinction between local and UTC clock displays. |
| 31 | Page 11, Fleet controls | Capitalize “This Pi’s” differently | Preserved the exact UI label. |
| 32 | Pages 10–13, source extraction | Correct “atthe”, “toThis”, or `:legacy`, or insert periods after schedule, Pi, required | These arise from omitted URLs, literal tokens, headings, or table cells; do not transfer them to Markdown. |
| 33 | Page 13, frequency values | Replace integral as a technical adjective throughout | Whole Hz wording was used in one introductory sentence; integral numeric values remain precise elsewhere. |
| 34 | Page 13, calibration | Unsplit “to manually calibrate” and “to always use” | Both are clear English; moving the adverb does not improve the instruction. |
| 35 | Page 15, firmware and management labels | Change System, Download, image, obtains, Time, Save, pin, Disable, or spacing in Device / boot | Protected UI labels and technical nouns. Rewriting them would make the manual disagree with the controls. |
| 36 | Page 15, source extraction | Complete “. Open” or add periods after outputs, settings, page, hostname, Fleet, locator, hash, or application | Headings, labels, and table fragments are intentionally not complete sentences. |
| 37 | Page 15, bracketed callsigns | Remove spaces in “Explicit ,” | The literal `<CALL>` was protected; its omission in the prose extract produced the fragment. |
| 38 | Page 16, I/O | Hyphenate or capitalize the quoted Active High option | Corrected the prose description, but preserved the exact option label. |
| 39 | Pages 16–18, labels and units | Add periods to output, controls, logs, Pi, status, fields, logging, or spacing inside `.service` | Preserved headings, label fragments, and unit names. |
| 40 | Page 17, USB collection | Add a comma before blocks in “remains visible and blocks…” | The predicates share one subject; a comma is unnecessary. |
| 41 | Page 17, UDP identity | Add an article to Local Pi | Local Pi is the source-selector label. |
| 42 | Page 17, collection | Add commas before or in “browser closes or its view is paused” | The two alternatives are clear without changing the sentence structure. |
| 43 | Page 17, settings | Change the preposition near “that” | Kept the distinction between the indicated saved and active settings; no clearer replacement was needed. |
| 44 | Pages 19–20, spelling | Change cancelled or acknowledgement | Retained existing spelling, particularly quoted state names. Neither changes meaning or clarity. |
| 45 | Pages 19–20, headings and controls | Capitalize tone or add periods after confirmation, source, selected, or result | These are labels/headings and technical control names. |
| 46 | Page 20, support-bundle explanation | Split the sentence at “, but it” | The contrast is short and important to the support-bundle privacy explanation. |
| 47 | Pages 22 and 31, topic summaries | Change covers to cover | The linked page title is a singular subject even when its title ends in a plural noun. |
| 48 | Page 25, permission example | Change deny to denies | “To load… but deny…” uses coordinated infinitives; denies would be ungrammatical. |
| 49 | Pages 24–27, literal options | Rewrite offsetSelect, --no-offsetUse, --transmit-pin, --gpio-manual-ppm, --socket-port, gpio, or RF | Protected options or text merged across inline-code boundaries. CLI identifiers are not prose spelling errors. |
| 50 | Page 25, options | Change form, once, or add an article before INI | Kept the exact negative-form and single-application semantics of the examples. |
| 51 | Page 26, numeric validation | Hyphenate nonnegative | The established mathematical spelling is clear and unambiguous. |
| 52 | Pages 29 and 33, correction/accounting | Rewrite key, usb, pins, or `.Transmit` | These refer to literal fields, keys, and transport values. |
| 53 | Page 30, terminology | Change licence to license | Existing regional spelling is acceptable; this is not a grammar defect. |
| 54 | Page 30, configuration prose | Add a comma before blocks after remains visible | Shared-subject compound predicate does not need that comma. |
| 55 | Page 30, band preset syntax | Insert spaces in `:legacy` or change `wrc15` | Preset selectors are protected syntax. |
| 56 | Pages 30–32, layout fragments | Add periods after input, rewrite “. with”, or punctuate or between topic alternatives | Preserved source links, headings, and alternatives that already read correctly in the rendered page. |
| 57 | Page 33, labels and state descriptions | Change saves or uses, or split the sentence at “, while” | Preserved singular control/resource subjects and the distinction between saved and active state. |
| 58 | Page 37, conflict message | Change “GPION is reserved” to “as reserved” or add articles around the label | The string is a literal application diagnostic. |
| 59 | Page 37, layout fragments | Add periods after unconfirmed, connect, destination, or unreachable; rewrite “. Keep” | Table headings and link boundaries are not sentence errors. |
| 60 | Pages 38–39, syntax | Change websocket, `.Transmit`, `:true`, or `:"` | Protected document token, configuration member, or JSON syntax; no source-code rewrite was authorized by proofreading. |
| 61 | Page 38, state descriptions | Add articles before configured or fresh | The phrases describe state categories/status as supplied by the API; retained their parallel form. |
| 62 | Page 38, HTTP methods | Change PUT as if it were a normal English verb | PUT names an HTTP method; station/hardware PUT denotes scoped replacement requests. |
| 63 | Page 38, layout fragments | Add periods after detection, operation, or resources | These are list/table fragments or headings. |
| 64 | Page 39, runtime states | Change cancelled to canceled | The event/state spelling is part of the documented protocol. |
| 65 | Page 40, status terminology | Replace whitelist or capitalize not-evaluated | Kept the existing technical policy term and literal status value. |
| 66 | Pages 40–45, layout fragments | Add periods after route, GPIO, pins, problems, or events; rewrite punctuation near for or a bare period | Headings, code boundaries, and reference fragments were protected. |
| 67 | Pages 46–50, update internals | Add periods to differ, development, invalidation, updates, releases, workflows, branches, notification, main, commit, branch, available, ahead, release, prereleases, example, default, applies, version, lifetime, dismissal, polls, checking, diagnostic, dismissed, or busting | These are headings, table cells, state identifiers, and short list entries, not run-on prose. Repeated title/cell punctuation suggestions were declined. |
| 68 | Pages 46–50, update controls | Change Newer, insert punctuation before also, or add a comma before or in a visibility condition | Preserved the quoted notification name and terse state-transition table entries. |
| 69 | Page 51, error title | Change the quotation punctuation in the Bash diagnostic | The diagnostic is literal code. |
| 70 | Page 54, bibliography | Correct Pleumeur-Bodou or change quotation/date punctuation in cited titles | Proper place names and published titles were preserved; bibliography style was not rewritten. |
| 71 | AI Detector, original batch 01; pages 1, 2, 3 | AI resemblance findings: see the batch percentage and flagged-part count above. | Advisory signal only. Did not paraphrase technical state, recovery, qualification, or citation text merely to lower the score. Concrete clarity/structure problems were addressed in the edits and final pass. No claim that every highlighted span was rewritten. |
| 72 | AI Detector, original batch 02; pages 4, 5 | AI resemblance findings: see the batch percentage and flagged-part count above. | Advisory signal only. Did not paraphrase technical state, recovery, qualification, or citation text merely to lower the score. Concrete clarity/structure problems were addressed in the edits and final pass. No claim that every highlighted span was rewritten. |
| 73 | AI Detector, original batch 03; pages 6, 7 | AI resemblance findings: see the batch percentage and flagged-part count above. | Advisory signal only. Did not paraphrase technical state, recovery, qualification, or citation text merely to lower the score. Concrete clarity/structure problems were addressed in the edits and final pass. No claim that every highlighted span was rewritten. |
| 74 | AI Detector, original batch 04; pages 8, 9 | AI resemblance findings: see the batch percentage and flagged-part count above. | Advisory signal only. Did not paraphrase technical state, recovery, qualification, or citation text merely to lower the score. Concrete clarity/structure problems were addressed in the edits and final pass. No claim that every highlighted span was rewritten. |
| 75 | AI Detector, original batch 05; pages 10, 11, 12, 13 | AI resemblance findings: see the batch percentage and flagged-part count above. | Advisory signal only. Did not paraphrase technical state, recovery, qualification, or citation text merely to lower the score. Concrete clarity/structure problems were addressed in the edits and final pass. No claim that every highlighted span was rewritten. |
| 76 | AI Detector, original batch 06; pages 14 | AI resemblance findings: see the batch percentage and flagged-part count above. | Advisory signal only. Did not paraphrase technical state, recovery, qualification, or citation text merely to lower the score. Concrete clarity/structure problems were addressed in the edits and final pass. No claim that every highlighted span was rewritten. |
| 77 | AI Detector, original batch 07; pages 15 | AI resemblance findings: see the batch percentage and flagged-part count above. | Advisory signal only. Did not paraphrase technical state, recovery, qualification, or citation text merely to lower the score. Concrete clarity/structure problems were addressed in the edits and final pass. No claim that every highlighted span was rewritten. |
| 78 | AI Detector, original batch 08; pages 16, 17, 18 | AI resemblance findings: see the batch percentage and flagged-part count above. | Advisory signal only. Did not paraphrase technical state, recovery, qualification, or citation text merely to lower the score. Concrete clarity/structure problems were addressed in the edits and final pass. No claim that every highlighted span was rewritten. |
| 79 | AI Detector, original batch 09; pages 19, 20 | AI resemblance findings: see the batch percentage and flagged-part count above. | Advisory signal only. Did not paraphrase technical state, recovery, qualification, or citation text merely to lower the score. Concrete clarity/structure problems were addressed in the edits and final pass. No claim that every highlighted span was rewritten. |
| 80 | AI Detector, original batch 10; pages 21, 22, 23, 24, 25, 26, 27 | AI resemblance findings: see the batch percentage and flagged-part count above. | Advisory signal only. Did not paraphrase technical state, recovery, qualification, or citation text merely to lower the score. Concrete clarity/structure problems were addressed in the edits and final pass. No claim that every highlighted span was rewritten. |
| 81 | AI Detector, original batch 11; pages 28, 29 | AI resemblance findings: see the batch percentage and flagged-part count above. | Advisory signal only. Did not paraphrase technical state, recovery, qualification, or citation text merely to lower the score. Concrete clarity/structure problems were addressed in the edits and final pass. No claim that every highlighted span was rewritten. |
| 82 | AI Detector, original batch 12; pages 30, 31, 32 | AI resemblance findings: see the batch percentage and flagged-part count above. | Advisory signal only. Did not paraphrase technical state, recovery, qualification, or citation text merely to lower the score. Concrete clarity/structure problems were addressed in the edits and final pass. No claim that every highlighted span was rewritten. |
| 83 | AI Detector, original batch 13; pages 33, 34, 35, 36, 37 | AI resemblance findings: see the batch percentage and flagged-part count above. | Advisory signal only. Did not paraphrase technical state, recovery, qualification, or citation text merely to lower the score. Concrete clarity/structure problems were addressed in the edits and final pass. No claim that every highlighted span was rewritten. |
| 84 | AI Detector, original batch 14; pages 38, 39 | AI resemblance findings: see the batch percentage and flagged-part count above. | Advisory signal only. Did not paraphrase technical state, recovery, qualification, or citation text merely to lower the score. Concrete clarity/structure problems were addressed in the edits and final pass. No claim that every highlighted span was rewritten. |
| 85 | AI Detector, original batch 15; pages 40, 41, 42, 43, 44, 45 | AI resemblance findings: see the batch percentage and flagged-part count above. | Advisory signal only. Did not paraphrase technical state, recovery, qualification, or citation text merely to lower the score. Concrete clarity/structure problems were addressed in the edits and final pass. No claim that every highlighted span was rewritten. |
| 86 | AI Detector, original batch 16; pages 46, 47, 48, 49, 50, 51, 52, 53, 54 | AI resemblance findings: see the batch percentage and flagged-part count above. | Advisory signal only. Did not paraphrase technical state, recovery, qualification, or citation text merely to lower the score. Concrete clarity/structure problems were addressed in the edits and final pass. No claim that every highlighted span was rewritten. |
| 87 | AI Detector, original batch 17; pages 55 | AI resemblance findings: see the batch percentage and flagged-part count above. | Advisory signal only. Did not paraphrase technical state, recovery, qualification, or citation text merely to lower the score. Concrete clarity/structure problems were addressed in the edits and final pass. No claim that every highlighted span was rewritten. |
| 88 | Final batch 18, overview/requirements | Add periods after station, path, or browser; capitalize What in a linked title | Headings and linked page titles were preserved. |
| 89 | Final batch 18, About pages | Optional rewrites of standalone Pico documentation, “WSPR is designed…”, and “The resulting signal…” (3 recommendations) | Retained concise technical descriptions. Original-batch optional findings retain their earlier numbered dispositions. |
| 90 | Final batch 18, qualification | Change every in “does not qualify every band or mode” | The quantifier is intentional; model compatibility does not establish qualification on all bands. |
| 91 | Final batch 19, installation/first transmission | Optional rewrites of the stable-channel sentence, “This also applies to Pi 5-family…”, “See timing and calibration…”, and runtime application (4 recommendations) | Preserved channel, backend, and saved-versus-applied distinctions. Other repeated installation findings are covered in the original-batch rows. |
| 92 | Final batch 19, walkthrough | Capitalize Your in the linked page title; add periods after disabled or plan; add a serial comma inside reference frequency and source | Preserved titles/headings and the paired reference-frequency/source settings within an already punctuated list. |
| 93 | Final batch 20, UI overview | Change the fragment “Documentation: This documentation…”; recapitalize WSPRnet | A link-description list may use fragments. WSPRnet spelling follows the project and service name. |
| 94 | Final batch 20, operator descriptions | Optional rewrites of the two paired-plan descriptions, CW label explanation, frequency-unit example, and default-value explanation (5 recommendations) | Retained the exact plan/UI labels, units, and validation semantics. The main Operation introduction and stop instruction were shortened independently. |
| 95 | Final batch 20, CW setup | Further optional rewrites of dot/dash duration and the DFCW character-space explanation (2 recommendations) | Kept explicit modulation distinctions and the documented spacing behavior. |
| 96 | Final batch 21, FAQ/experiment | Repeated optional rewrites of the DNS redirect explanation, measured-band findings, and historical qualification scope | Same findings and dispositions as original batches 16–17. Accepted the historical page’s serial comma; retained evidence boundaries. |
| 97 | AI Detector, final batch 18 | Remaining resemblance findings: see final-pass score and part count above. | No stylistic rewrite was made solely to reduce the score. The clearer beginner path and shorter operator prose are substantive editorial changes; technical recovery and qualification wording remains precise. |
| 98 | AI Detector, final batch 19 | Remaining resemblance findings: see final-pass score and part count above. | No stylistic rewrite was made solely to reduce the score. The clearer beginner path and shorter operator prose are substantive editorial changes; technical recovery and qualification wording remains precise. |
| 99 | AI Detector, final batch 20 | Remaining resemblance findings: see final-pass score and part count above. | No stylistic rewrite was made solely to reduce the score. The clearer beginner path and shorter operator prose are substantive editorial changes; technical recovery and qualification wording remains precise. |
| 100 | AI Detector, final batch 21 | Remaining resemblance findings: see final-pass score and part count above. | No stylistic rewrite was made solely to reduce the score. The clearer beginner path and shorter operator prose are substantive editorial changes; technical recovery and qualification wording remains precise. |
| 101 | Final batch 22, Operations introduction | Optional rewrites of the redirect rationale and the condition for adding `/wsprrypi/` (2 recommendations) | Kept the existing redirect behavior and manual-path explanation. The main card introduction and stop instruction were shortened; repeated safety and mode suggestions retain their earlier dispositions. |
| 102 | AI Detector, final batch 22 | 30% resemblance, 10 flagged parts in the revised Operations and CW scope | Reran after the wording changes. Remaining technical descriptions were retained where no concrete clarity defect justified another rewrite. This score is not directly comparable with the larger batch 20. |
