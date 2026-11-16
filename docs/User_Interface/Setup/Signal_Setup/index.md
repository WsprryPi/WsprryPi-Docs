# Signal Setup Tab

Choose **Device** beside the tabs first. With **This Pi**, Signal Setup configures
the local signal type and message content and keeps validated autosave.

![Signal Setup Panel](../setup.jpg)

With a saved Pico, this tab shows station progress, complete station saves, and
its existing standalone combined-settings editor. Read saved values before an
explicit save. Applying saved station progress is a separate action; saving a
draft does not make an incomplete station ready or enable output. Existing
standalone schedules retain their own explicit save and enable semantics.
Pi CW profiles are not mapped onto Pico settings. Unsupported controls are
unavailable rather than sent to the local Pi. See
[Pico station resources](../Transmitter/index.md#shared-pico-member-resources).

The local Pi view has two main modes, WSPR and CW.

Select your preferred mode to show its settings.

Choose the mode you want to configure:

```{toctree}
:maxdepth: 1
:hidden:

Configure WSPR <wspr>
Configure CW Modes <cw>
```

## Signal Configuration Guides

<span id="wspr-mode"></span>
<span id="station-identity"></span>
<span id="wspr-transmission-type-selection-examples"></span>
<span id="rule-summary"></span>
<span id="wspr-transmission-plan"></span>
<span id="frequencies"></span>
<span id="random-offset"></span>
<span id="reported-power"></span>
<span id="frequency-calibration-ppm-ntp-calibration"></span>
<span id="planning-mode"></span>

- [Configure WSPR](wspr.md) for station identity, WSPR message planning, frequencies, reported power, and calibration.

<span id="cw-mode"></span>
<span id="mode"></span>
<span id="available-modes"></span>
<span id="cw-timing"></span>
<span id="speed"></span>
<span id="spacing"></span>
<span id="modulation-construction"></span>
<span id="frequency-offset"></span>
<span id="base-frequency"></span>
<span id="frequency-calibration"></span>
<span id="schedule"></span>
<span id="start-minute-start-second-repeat-interval"></span>
<span id="cw-message"></span>
<span id="message-validation"></span>
<span id="when-a-cw-message-is-too-long"></span>
<span id="cw-message-too-long"></span>

- [Configure CW Modes](cw.md) for QRSS, FSKCW, and DFCW modulation, timing, spacing, scheduling, frequency, and message validation.

If your task concerns the RF output path or Raspberry Pi pins rather than signal content, use [Configure Transmitter](../Transmitter/index.md) or [Configure Device I/O](../Pi_IO/index.md).
