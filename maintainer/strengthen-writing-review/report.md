# Completed Strengthen writing review

## Scope and result

Completed the previously unfinished Strengthen writing review for the selected
extract: About WSPR's opening two paragraphs, Operations' Current Plan and plan
descriptions, and Configure WSPR's Planning Mode section. This does not rescore
whole pages or the handbook. The exact prior and final submissions are saved as
[original.txt](original.txt) and [final.txt](final.txt).

Baseline: clean `devel` at `2cdb762`. The existing authenticated Grammarly page
showed proofreading 100 and AI Detector 10% before changes. The expected account
was confirmed before editing.

The original three groups displayed counts of 6, 4, and 5. Every available card
was inspected individually: 13 cards, including overlapping category entries.
After changes, Update suggestions produced another set with counts 4, 4, and 1;
all seven available cards were inspected. Each queue ended with all three groups
checked and disabled. Category totals are not asserted to be unique card counts.
No Accept all, Humanizer, or automatic wholesale rewrite was used. Selected useful
parts were transferred to source while protected markup and identifiers remained
intact.

An in-place Grammarly editor replacement later duplicated content. That result
was discarded. A clean new page was populated with the intended final extract;
its rendered editor text matched the saved extract after whitespace normalization.
Final results below come only from that clean page:
[final Grammarly review](https://coda.grammarly.com/d/_dl_YUU_yd--/Untitled-page_sueKvWRp).
The prior working page is an intermediate review surface, not the final evidence.

| Check | Original selected scope | Final clean selected scope |
| --- | --- | --- |
| Grammarly proofreading score | 100 | 100 |
| Proofreading suggestions | 0 | 0 |
| AI Detector resemblance | 10% | 10% |
| AI flags | One strong | One strong |

**Grammarly-validated** for the saved selected prose. The detector is an advisory
pattern assessment, not an authorship verdict. No text was changed solely to
reduce its percentage.

## Applied improvements

- Current Plan uses present-tense “shows,” moves the pause-mode condition after
  the current plan, and uses “WSPR frame type being transmitted.” It still
  distinguishes a plan to be transmitted from an active frame. Callsign, locator,
  CW message, and character-cursor details remain.
- Planning Mode capitalization matches the control name.
- Prefer paired when available now says “If the planner can generate…” and
  “it does so in alternating windows.” Both message types and the condition
  remain explicit.

About WSPR, all exact plan identifiers, the previously approved hash explanation,
paired-plan descriptions, and Require paired's requirements remain unchanged.

## Complete card dispositions

Prior item numbers are retained; new findings start at 113. Item 112's incomplete
coverage is now closed by this review. Earlier reports remain historical.

| Item | Card / location | Proposal and final disposition |
| --- | --- | --- |
| 108 | Use consistent terminology / WSPR definition | Rejected “It is” and passive “used by” in place of the approved conversational wording. |
| 109 | Tighten signal wording / WSPR decoding paragraph | Rejected optional comma before “even when”; uninterrupted condition reads clearly. |
| 110 | Tighten plan terminology / Current Plan | Applied present tense. Its comma-bracketed pause phrase was superseded by the clearer sentence in item 115. |
| 111 | Trim hash explanation / Type3Single | Rejected “cannot” and “decoded message” substitutions; retained approved conversational wording. |
| 113 | Planning Mode introduction | Applied capitalization matching the control name. |
| 114 | Prefer paired / terminology | Applied removal of “finds it.” |
| 115 | Current Plan / frame logic | Applied clearer pause condition and “along with.” Rejected changing “being transmitted” to “will be transmitted.” |
| 116 | Type3Single / frame logic | Rejected joining the hash limitation and dependency with a semicolon and shortening “message it has decoded.” Short sentences remain clear. |
| 117 | Prefer paired / frame logic | Applied direct conditional and present-tense “does so”; alternating windows unchanged. |
| 118 | Current Plan / streamline labels | Applied overlapping present-tense and pause improvements; retained explicit “being transmitted.” |
| 119 | Type1Single / streamline labels | Rejected renaming exact identifier to “Type 1 Single.” |
| 120 | Type2Single / streamline labels | Rejected renaming exact identifier to “Type 2 Single.” |
| 121 | Type3Single / streamline labels | Rejected renaming exact identifier to “Type 3 Single.” |
| 122 | Intermediate proofreading / Current Plan | Rejected “currently being transmitted” for “to be transmitted”: a displayed plan does not necessarily mean active transmission. Final clean check did not repeat it. |
| 123 | Refreshed WSPR definition | Rejected formal/passive rewrite and inconsequential removal of “over”; approved voice retained. |
| 124 | Refreshed Current Plan terminology | Applied “WSPR frame type” for “type of WSPR frame.” |
| 125 | Refreshed Current Plan frame logic | Rejected replacing the frame-type phrase with a Type 1/2/3 enumeration. Types are explained immediately below. |
| 126 | Refreshed Planning Mode introduction | Rejected adding “and how paired frames are used”; option descriptions already supply that detail. |
| 127 | Refreshed Prefer paired | Rejected adding “so the paired frames are used together”; alternating windows is more precise and avoids implying simultaneity. |
| 128 | Refreshed Require paired | Rejected adding “and always using the paired format”; “every transmission plan” already expresses the requirement. |
| 129 | Refreshed Current Plan labels | Applied the shorter “frame type” through item 124, but retained “being transmitted” as temporal context. |

## Exact final detector highlight

Strong AI patterns: heading **About WSPR** and this entire paragraph:

> WSPR stands for Weak Signal Propagation Reporter. It’s a digital protocol that amateur radio operators use to study how low-power signals travel over long distances, even when propagation conditions are poor.

Captured by matching visible highlight rectangles to rendered text spans, then
checking the boundary in a screenshot. The complete final submission was verified
again after capture. No hidden application state or service API was used.

## Adversarial review and validation

Reviewed the final source diff for changed planner conditions, requirement strength,
message types, temporal meaning, hash recovery promises, and identifier spelling.
No actionable issue remains. The review caught an initial source replacement
that missed Current Plan's Markdown emphasis; the final source and submitted
extract were compared after correcting it.

- Headings, exact emphasized labels, plan identifiers, message-type counts,
  F1/2 and F2/2 counts, link/image destinations, inline literals, and fenced
  markers match the prior committed sources.
- Fresh complete warnings-as-errors HTML build passed:
  `source docs/.venv/bin/activate` then
  `python -m sphinx -E -a -b html -n -W --keep-going docs docs/_build/html`.
- Extension unittest passed (one test).
- Generated HTML contains all three changed paragraphs intact.
- `git diff --check` passed. No code, CSS, navigation, or hardware change.
- Commit, push, and exact-commit remote build results are reported in the final
  completion message after this report is committed.

## Suggestions not applied

| Item | Location | Grammarly recommendation or finding | Reason not applied / disposition |
| --- | --- | --- | --- |
| 106 | About WSPR definition | AI Detector: strong patterns; final highlight above | Retained accurate approved operator wording; resemblance remains 10%. |
| 108 | About WSPR definition | “It is” and passive “used by” | Preserve operator voice. |
| 109 | About WSPR decoding | Optional comma before “even when” | No clarity improvement. |
| 110 | Current Plan | Commas around pause condition | Present tense applied; clearer pause sentence from item 115 used instead. |
| 111 | Type3Single | “cannot” and “decoded message” | Preserve approved conversational phrasing. |
| 115 | Current Plan | “will be transmitted” for active-frame description | Preserve “being transmitted”; other parts applied. |
| 116 | Type3Single | Semicolon and shorter decoded-message wording | Short sentences make limitation and dependency clear. |
| 118 | Current Plan | Remove explicit “being transmitted” | Retain active-frame context; other improvements applied. |
| 119 | Type1Single | Rename to “Type 1 Single” | Exact application identifier. |
| 120 | Type2Single | Rename to “Type 2 Single” | Exact application identifier. |
| 121 | Type3Single | Rename to “Type 3 Single” | Exact application identifier. |
| 122 | Intermediate Current Plan proofreading | “currently being transmitted” | Could imply active transmission; absent from final clean check. |
| 123 | About WSPR definition | Formal/passive wording; remove “over” | Preserve approved voice; no concrete benefit. |
| 125 | Current Plan | Enumerate Type 1, 2, or 3 here | Types already described below. |
| 126 | Planning Mode introduction | Add pairing-behavior clause | Redundant with options immediately below. |
| 127 | Prefer paired | Add “used together” | Less precise than alternating windows. |
| 128 | Require paired | Add “always using the paired format” | Redundant with every transmission plan. |
| 129 | Current Plan | Remove “being transmitted” while shortening label | Keep temporal context; shorter frame-type phrase applied. |
| 130 | Final clean proofreading | No suggestions remaining; score 100 | No final proofreading suggestions left unapplied. |
