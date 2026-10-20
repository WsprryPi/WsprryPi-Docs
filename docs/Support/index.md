(support-gpt)=
# Getting Help with the WsprryPi Support GPT

The WsprryPi Support GPT can help you troubleshoot WsprryPi by reviewing your description of the problem. A WsprryPi support bundle can also help a project developer investigate an issue.

Start here: [Open the WsprryPi Support GPT](https://chatgpt.com/g/g-6a43dc71d1988191b16ead50e3bb707b-wsprrypi-support-assistant).

## Quick Start

1. Open the WsprryPi Support GPT.
2. Briefly describe what is going wrong.
3. If you need developer help, [create and review a support bundle](../User_Interface/Maintenance/support_bundle.md).
4. Keep the downloaded `.tar.gz` available in case the project developer requests it.

You can still start with the GPT even if you do not already have a bundle.

## What the GPT Can Help With

Use the WsprryPi Support GPT for help with issues such as:

- Configuration problems
- Runtime errors
- Audio or signal-generation behavior
- WSPR decoding or spotting questions
- Upload or reporting problems
- Raspberry Pi environment issues

The GPT is meant to help with troubleshooting. It is not a substitute for checking hardware safety, licensing rules, antenna setup, or local operating requirements.

## What to Tell the GPT

Include a short description of the problem. The most useful details are:

- What you expected to happen
- What actually happened
- What you were doing when the issue occurred
- Whether the issue happens every time or only sometimes
- Any recent changes, such as updates, configuration edits, hardware changes, or network changes

A short, specific description usually helps more than a long transcript with no context.

## Problems involving a Pico output

For WsprryPi connection, Fleet scheduling or host job recovery, start with
[Add a WsprryPico](../Install/pico.md) and
[Pico status and recovery](../User_Interface/Setup/Transmitter/index.md#pico-status-and-recovery).
Include the Pi version, Pico firmware/source identity, full stable device ID,
transport and the exact error. Say whether output is confirmed inactive or
unknown; a disconnected member is not proof of RF shutdown.

For the Pico's own browser, firmware, standalone scheduler or device reset,
use [Pico troubleshooting](https://wsprrypico.readthedocs.io/en/devel/troubleshoot.html)
and [Pico support information](https://wsprrypico.readthedocs.io/en/devel/maintain.html#support-information).
Keep full-flash backups, credentials and unsanitized installer transactions
private; they are not support attachments.

## Using a Support Bundle

A support bundle gives a developer useful diagnostic context. It can help identify configuration, runtime, audio, WSPR decoding, upload, and Raspberry Pi environment issues.

Create and download the readable candidate from the Maintenance page. Review it for information you do not want to share, approve the exact candidate, then upload only its encrypted `.age` file through the private Dropbox handoff. The [support-bundle guide](../User_Interface/Maintenance/support_bundle.md) explains support context, active I²C consent, review, encryption, receipts, Dropbox metadata, truthful upload reporting, GitHub correlation, and cleanup.

## Example Questions

You can ask questions such as:

- "I expected WsprryPi to transmit on 20m, but I do not see any spots. Can you review this support bundle and suggest what to check?"
- "The application starts, but transmissions do not appear to run. What does this support bundle show?"
- "Can you look for configuration problems that might prevent WSPR uploads?"
- "Does this bundle show any runtime errors or environment problems?"
- "I do not have a support bundle yet. Can you walk me through collecting one?"

## What Not to Upload

Do not paste or upload:

- Passwords or private account credentials
- API keys, tokens, or other secrets
- Unrelated personal files
- Private documents that are not part of the support request

The support bundle is intended for diagnostics, but automatic redaction is best-effort. Always review it before attaching it to a public issue or sending it to another service.

## If the GPT Cannot Solve the Issue

If the WsprryPi Support GPT cannot identify the problem, keep the support bundle and the GPT's summary. That information can make it easier to ask for help from the WsprryPi project or community.
