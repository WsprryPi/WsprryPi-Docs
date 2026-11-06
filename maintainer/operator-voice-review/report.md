# Approved operator-voice rewrites

## Result and coverage

Applied the user's three approved paragraphs in About WSPR and Operations exactly.
Grammarly-validated for the selected prose in `final.txt`, including the same
neighboring context used in the previous review. This was not a full-page or
handbook rescore. `original.txt` preserves the prior submitted text.

Authenticated Grammarly review: [new Untitled page](https://coda.grammarly.com/d/_dl_YUU_yd--/Untitled-page_suGuOGVg).

| Assessment | Previous selected scope | Approved operator wording |
| --- | --- | --- |
| Proofreading score | 100 | 100 |
| Proofreading suggestions remaining | 0 | 0 |
| AI resemblance | 29% | 10% |
| AI flags | One strong, one weak | One strong |

The original 29% result was visible again on the saved revised page before the
new submission. The new result was captured from the actual AI Detector, not the
proofreading score. Operations no longer appears in the flagged parts. The AI
percentage is an advisory resemblance signal, not proof of authorship.

## Exact remaining highlight

Strong AI patterns: the heading **About WSPR** and the complete opening paragraph:

> WSPR stands for Weak Signal Propagation Reporter. It’s a digital protocol that amateur radio operators use to study how low-power signals travel over long distances, even when propagation conditions are poor.

Captured by matching visible detector-highlight rectangles to rendered text spans;
the screenshot confirmed the complete heading and paragraph boundary. No hidden
state or Grammarly service API was accessed. The saved submitted editor text was
compared with the intended extract after normalizing whitespace and matched.

## Editorial and adversarial review

- Confirmed the source contains the approved wording exactly. No additional
  Grammarly rewrite was applied.
- WSPR's expanded name, digital protocol, amateur radio use, low power, long
  distance, and poor propagation conditions remain explicit.
- Type3Single still carries the hash, six-character Maidenhead locator, and
  reported power. Recovery from the hash alone remains impossible, and another
  decoded message must provide matching callsign information.
- Type2Type3Paired still alternates Type 2/F1/2 and Type 3/F2/2. The complex or long
  callsign and long locator remain associated by the receiver across the frames.
- Headings, link destinations, inline literals, fenced markers, plan identifiers,
  and frame-label counts match the previous committed sources. No navigation,
  configuration, code, or CSS changed.
- Fresh complete Sphinx HTML build passed with warnings treated as errors:
  `source docs/.venv/bin/activate` then
  `python -m sphinx -E -a -b html -n -W --keep-going docs docs/_build/html`.
- Extension unittest passed (one test); `git diff --check` passed.
- No actionable issue remained after reviewing the final diff. Remote build
  results and commit are reported in the completion message.

## Subsequent completion

The remaining Strengthen writing coverage in item 112 was completed in the
[follow-up review](../strengthen-writing-review/report.md). The results and
dispositions below describe the earlier pass.

## Suggestions not applied

Items continue the previous review's numbering. Items 103 and 104 remain historical
results; their approved replacements are assessed here. Proofread showed no more
suggestions. Strengthen writing is a separate optional generated-rewrite surface;
its score and proposals must not be conflated with proofreading.

| Item | Location | Grammarly recommendation or finding | Reason not applied / disposition |
| --- | --- | --- | --- |
| 106 | About WSPR opening | AI Detector: strong AI patterns; exact highlight above | Retained the approved definition and operator voice. No concrete editorial defect warrants changing it solely for the detector. |
| 107 | Selected review scope | Proofread: no suggestions remaining; score 100 | No proofreading suggestions left unapplied. |
| 108 | About WSPR opening | Strengthen writing: replace “It’s” with “It is” and “that amateur radio operators use” with “used by amateur radio operators” | Rejected the more formal, passive phrasing because the user approved a natural operator voice. |
| 109 | About WSPR second paragraph | Strengthen writing: add a comma before “even when” | Optional punctuation in unchanged context; the existing sentence reads clearly. |
| 110 | Operations Current Plan introduction | Strengthen writing: replace future “will display/show” with present “shows” and change pause-mode parentheses to commas | Context outside the approved replacements; retained the existing presentation in this focused pass. |
| 111 | Operations Type3Single | Strengthen writing: “can’t” to “cannot”; “message it has decoded” to “decoded message” | Retained the approved conversational phrasing, which is technically explicit. |
| 112 | Selected review scope | Optional Strengthen writing coverage: displayed groups Tighten terminology (6), Clarify frame logic (4), and Streamline mode labels (5) | Four visible proposals were inspected as items 108–111. Other optional generated rewrites were not exhaustively reviewed or applied. Proofreading and AI Detector coverage were completed for the full saved extract. |
