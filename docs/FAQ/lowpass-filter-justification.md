---
orphan: true
---
(lowpass-filter-justification)=
# Low-Pass Filter Requirements

Direct GPIO RF is a square-wave output, not a spectrally clean sine wave. An appropriate low-pass or band-pass filter is required between the Raspberry Pi and the antenna system to suppress harmonics and out-of-band switching products.

:::{warning}
Never treat a clean-looking carrier or a successful WSPR decode as proof that
the complete RF output is suitable for an antenna. Verify the output with
appropriate RF test equipment and use filtering for the selected band.
:::

## What a Filter Can Do

A suitable filter can attenuate:

- harmonics of the square-wave carrier;
- divider-switching products outside the intended channel; and
- other wideband energy outside the filter passband.

The filter must be designed for the operating band and the power level of the complete transmitter chain. A filter for one band is not a general-purpose filter for every configured frequency.

## What a Filter Cannot Do

A filter cannot correct an unusable synthesized signal within its passband. It does not:

- create the requested carrier when the GPIO divider does not produce one;
- restore WSPR tone timing that cannot be decoded;
- remove close-in products that fall inside the same narrow passband; or
- correct oscillator frequency error or drift.

This distinction matters on the higher GPIO bands. Conducted testing qualified GPIO on 80 m, 20 m, 15 m, and 10 m, but disqualified 12 m, 6 m, and 2 m. The 12 m and 6 m failures cannot be repaired by adding an LPF or increasing `PWM_CLOCKS_PER_ITER_NOMINAL`. See [GPIO Band Capabilities and Signal Quality](why_12m_looks_noisy.md).

## Bench and On-Air Use

For bench tests, use a shielded 50-ohm load, attenuation appropriate to the measurement instrument, and a filter when evaluating spectral cleanliness. For on-air operation, use a filter appropriate to the selected band and comply with applicable licensing and emission requirements.

Hardware-specific output power, harmonics, spurs, oscillator behavior, and RF chain losses are not project-wide guarantees. Measure the assembled station.
