# WsprryPi wording follow-up

## Result and scope

**Grammarly-validated for the selected prose below.** The three pages were not
rescored in full. This follow-up tightens the passages identified after the
complete handbook review, preserving message types, frame labels, callsign and
locator distinctions, and planner requirements.

- About WSPR: opening two paragraphs.
- Operations: current-plan descriptions through Type2Type3Paired, including
  neighboring unchanged descriptions for context.
- Configure WSPR: Planning Mode section.

The review started on clean `devel` at `a9825fd`. Exact submitted text is saved
in [original.txt](original.txt) and [final.txt](final.txt). Source-page mappings
and all captured detector passages are in
[detector-passages.json](detector-passages.json). The Grammarly review document
contains separate original and revised pages:
[WsprryPi wording follow-up](https://coda.grammarly.com/d/_dl_YUU_yd--).

## Comparable observations

The same sections and context were reviewed before and after editing. Word
counts use whitespace-delimited words in the saved extracts, including their
section markers. The revised text is 98 words shorter (23.2%).

| Stage | Words | Grammarly writing score | Suggestions remaining | AI resemblance | Flagged parts |
| --- | ---: | ---: | ---: | ---: | ---: |
| Original | 423 | 95 | 5 | 22% | 2: one strong, one moderate |
| First revision | 326 | 98 | 2 | 29% | 2: one strong, one weak |
| Final, after accepting both remaining suggestions | 325 | 100 | 0 | 29% | 2: one strong, one weak |

The prose became shorter and cleared Grammarly's proofreading suggestions, but
the detector percentage increased. This is not reported as an improvement in
AI resemblance. The detector is an advisory pattern assessment, not an authorship
verdict. No additional rewrite was made merely to lower the percentage.

## Changes and editorial decisions

- Replaced the broad efficiency claims with the protocol's purpose and the
  concrete sequence of tones and software decoding.
- Replaced “This may be thought of as an automated means…” in both paired-plan
  descriptions with direct explanations of the frames and receiver association.
- Replaced the vague Planning Mode introduction with its specific selection task.
- Removed the unsupported “best choice” recommendation about remote stations.
  Require paired still requires pairing on every plan; it now explains that the
  callsign and extended locator are supplied in separate frames.
- Accepted Grammarly's final suggestions to use “long-distance propagation” and
  repeat “Type” in “Type 2 and Type 3 messages.”

The four original clarity suggestions were addressed through these focused
rewrites. Its split-infinitive suggestion was superseded by rewriting Require
paired; no awkward adverb movement was introduced. This resolves the relevant
wording portions of prior review items **5**, **89**, and **94** without changing
other decisions grouped under those numbers.

## Captured original AI flags

The following text was actually highlighted by Grammarly. It was captured by
matching the visible highlight rectangles to rendered prose and checking the
highlight boundaries in screenshots. No hidden application state or service API
was accessed. Blank paragraph separators are omitted from the quotations.

### Strong AI patterns — About WSPR

The highlighted region included the heading **About WSPR** and this paragraph:

> WSPR, "Weak Signal Propagation Reporter," is a protocol for low-power, digital communication on amateur radio frequencies. WSPR is designed to transmit and receive information efficiently over long distances, even under challenging radio propagation conditions.

### Moderate AI patterns — About WSPR

> WSPR encodes information in a series of tones and transmits it in short, controlled bursts using a highly efficient modulation scheme. The resulting signal is often too weak to hear but can be decoded by specialized software at a receiving station, which can extract the encoded information from the noise.

Both original paragraphs were rewritten. The second paragraph was no longer
flagged in the final selected scope; the first remained strongly flagged in its
revised form.

## Captured final AI flags

### Item 103: Strong AI patterns — About WSPR

The highlighted region still included the heading **About WSPR** and:

> WSPR (Weak Signal Propagation Reporter) is a protocol for low-power digital communication on amateur radio frequencies. Operators use it to study long-distance propagation, even under poor conditions.

Retained because it gives the protocol's name, purpose, low-power use, and radio
context directly. No concrete grammatical or clarity defect remains to justify
another rewrite of this definition solely for the detector.

### Item 104: Weak AI patterns — Operations

Grammarly highlighted these two consecutive paragraphs as one weak-pattern part:

> Type3Single sends a callsign hash, a six-character Maidenhead locator, and reported power. The hash is not reversible; the receiver needs matching callsign context from another decoded message.
>
> Type2Type3Paired alternates Type 2 (shown as F1/2) and Type 3 (shown as F2/2) messages, pairing a complex or long callsign with a long locator so the receiver can associate both.

The Type3Single explanation was unchanged. Its non-reversible hash and required
receiver context are important limitations. The shortened Type2Type3Paired
explanation retains the actual frame labels and the callsign/locator association.
No more rewriting was warranted by this weak-pattern finding alone.

## Review and validation

- Reviewed the diff for meaning changes, unsupported reception promises, and
  confusion between a message frame and a paired plan. No actionable issue remained.
- Confirmed that headings, destinations, fenced examples, and inline code are
  unchanged on all three edited pages. The F1/2 and F2/2 labels and plan identifiers
  retain their exact spelling and counts. WSPR setup content before Planning Mode
  is unchanged.
- Fresh full HTML build passed with warnings treated as errors:
  `source docs/.venv/bin/activate` followed by
  `python -m sphinx -E -a -b html -n -W --keep-going docs docs/_build/html`.
- The rendered internal-file/fragment audit found zero missing targets.
- `python -m unittest discover -s tests -p 'test_*.py' -v` passed (one test).
- `git diff --check` passed. No code, CSS, hardware, service, or on-air change was made.
- Delivery targets `origin/devel`. Exact commit and observed GitHub and Read the
  Docs build results are reported in the completion message after the report is
  committed.

## Suggestions not applied

Item numbers continue the original review's 1–102 rather than renumbering prior
decisions. The earlier recommendation groups 5, 89, and 94 are partly resolved
as explained above; their other findings remain historical decisions.

| Item | Location | Grammarly recommendation or finding | Reason not applied / disposition |
| --- | --- | --- | --- |
| 103 | About WSPR, opening definition | AI Detector: Strong AI patterns; exact final text quoted above | Retained the clear protocol definition. No concrete editorial defect justified rewriting it solely to lower the detector score. |
| 104 | Operations, Type3Single and Type2Type3Paired | AI Detector: one Weak AI patterns part spanning the two quoted paragraphs | Preserved the hash limitation, receiver context, frame labels, and callsign/locator association. |
| 105 | Final selected proofreading scope | No proofreading suggestions left unapplied | Both final suggestions were accepted and transferred to source; Grammarly showed 100 and no remaining suggestions. This does not mean the AI Detector cleared the text. |
