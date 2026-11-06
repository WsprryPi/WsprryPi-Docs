---
orphan: true
---
(why_12m_looks_noisy)=
# GPIO Band Capabilities and Signal Quality

Direct GPIO RF is not equally usable on every band. Testing with the 500 MHz
and 750 MHz PLLD clock profiles showed that qualification is specific to the
band and clock profile, rather than determined by a simple upper-frequency
limit.

:::{important}
Qualification requires usable modulation and repeatable WSPR decoding. A
steady carrier alone does not prove that a GPIO signal is usable for WSPR.
:::

For the legacy 500 MHz and 750 MHz PLLD GPIO paths described here,
WsprryPi blocks unqualified direct GPIO requests by default in the 12 m,
6 m, 4 m, 2 m, 1.25 m, and 70 cm band ranges. The check uses the final
requested RF frequency and applies to named bands and arbitrary frequencies,
WSPR and CW modes, scheduled operation, command-line operation, and Test Tone.
The request is rejected before the transmitter is activated, with guidance to
select a GPIO-qualified band or a transmitter backend separately qualified for
the requested band. The Si5351 backend is not subject to this GPIO policy, but
its qualification status still varies by band. Pi 5 uses a different RP1 clock
profile and is qualified on 12 m; use the current table below for its limits.

## Current Qualification Status

See [Transmitter qualification](../About_Wsprry_Pi/index.md#transmitter-qualification)
for the authoritative qualification status of each band, transmitter backend,
and GPIO clock profile. This page provides background for selected GPIO
signal-quality findings; it does not replace the qualification table.

Testing on bands above and below 12 m showed that the limitation is not a
monotonic frequency ceiling. Divider selection and fractional scheduling
interact differently at different requested frequencies.

These are backend qualification results, not guaranteed RF specifications for
every Raspberry Pi or station. Oscillator accuracy, drift, phase noise,
harmonics, spurs, output power, and the attached RF chain remain
hardware-specific.

## Original-Generation Software Comparison

The `Legacy_1.2.3` software, which is close to the original WsprryPi
implementation, was also tested on the same Raspberry Pi 4 and Debian Trixie
platform. Its 12 m tone did not form a usable requested-frequency carrier, and
its 6 m tone formed a broad comb rather than a usable carrier. WSPR frame tests
were therefore not attempted. These results do not show that the original
WsprryPi code produced usable 12 m or 6 m signals on this platform. They
therefore do not establish that the current behavior is a regression.

## What Testing Showed on Unqualified Bands

The GPIO backend synthesizes frequencies by switching between integer divider
states so their time average produces the requested WSPR tones. At some
frequencies, the measured output showed an unfavorable distribution of energy.

- On 12 m, neither clock profile met the requirement for three consecutive
  decoded frames.
- On 6 m, the output was spread across a comb instead of being concentrated in
  one narrow channel. In the conducted measurement, the most useful 20 Hz
  region contained only about 1.7% of the resolved close-in transmitted power.
- On 2 m, no usable requested-frequency signal was found.

Visible comb teeth do not automatically mean the same failure on every band.
At 10 m, more than 99.5% of the resolved close-in power remained within one
20 Hz channel in the tested WSPR captures, and the frames decoded. The band
disposition is therefore based on usable modulation and decoding, not merely
on whether a spectrum display shows side products.

## Filtering and Calibration

An appropriate band filter is required for any GPIO transmission. Filtering
suppresses harmonics and out-of-band switching products, but it cannot turn a
dispersed or absent requested-frequency carrier into a qualified WSPR signal.
See [Low-Pass Filter Requirements](lowpass-filter-justification.md).

Frequency calibration moves the output toward the intended frequency; it does
not cure band-specific synthesis artifacts. Calibration values are specific to
the Raspberry Pi and reference used to measure it. Do not copy another
station's PPM value as a project default.

Qualification does not authorize unlicensed or unfiltered on-air operation.
Use a shielded load and suitable attenuation for bench testing, and comply
with the rules that apply to your station.
