# CW Mode Options

These options configure direct command-line transmissions using QRSS, FSKCW, or DFCW.

## Mode Selection

- `--mode <WSPR\|QRSS\|FSKCW\|DFCW>` Select transmission mode.

- `--cw-message <text>` Message to transmit in CW-based modes.

- `--cw-base-frequency <freq>` Numeric RF reference: carrier for QRSS, space for FSKCW, dot for DFCW. Supports Hz, kHz, MHz and GHz suffixes; WSPR band aliases are rejected.

- `--cw-shift-hz <hz>` Positive shift in Hz: FSKCW mark = space + shift; DFCW dash = dot + shift. QRSS ignores it. Band correlation still applies to filters, frequency policy and output limits; it does not convert CW frequencies into WSPR presets.

- `--cw-dot-seconds <seconds>` Length of a Morse "dot".

## Timing

- `--cw-start-minute <0-59>` Start minute for scheduled transmissions.

- `--cw-repeat-minutes <minutes>` Interval between transmissions.

## Spacing

The `--cw-*` gap options are shared by QRSS and FSKCW. DFCW uses its own gap options.

- `--cw-intra-element-gap <multiple>` QRSS/FSKCW gap between elements of a character.

- `--cw-inter-character-gap <multiple>` QRSS/FSKCW gap between characters.

- `--cw-inter-word-gap <multiple>` QRSS/FSKCW gap between words.

- `--dfcw-intra-element-gap <multiple>`

  DFCW gap between equal-duration dot and dash symbols (default: `0.333333` dot lengths).

- `--dfcw-inter-character-gap <multiple>`

  DFCW gap between characters (default: `1.0` dot lengths).

- `--dfcw-inter-word-gap <multiple>`

  DFCW gap between words (default: `3.0` dot lengths).

## Envelope Control

For Si5351, fades chop the output on/off at the retained full drive; duty cycle approximates the requested envelope. This is neither a measured analog amplitude envelope nor a spectral guarantee. I2C and scheduling time count against each event's absolute monotonic deadlines; expired slices are skipped rather than replayed. Slow transfers can consume a slice and shorten or omit pulses.

Fade durations must be nonnegative and the slice duration positive. The last slice is limited to the remaining event time; overlapping fades use the lower envelope level. Smaller slices increase switching cost and do not prove smoother RF or extend the event. Measure the actual waveform and spectrum independently.

- `--cw-fade-shape <none\|linear\|raised_cosine>` Requested envelope shape (`none` disables fading).

- `--cw-fade-in-ms <ms>` Fade-in duration.

- `--cw-fade-out-ms <ms>` Fade-out duration.

- `--cw-fade-slice-ms <ms>` Maximum requested duty-cycle slice duration in milliseconds.