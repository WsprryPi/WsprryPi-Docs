# About WsprryPi

WsprryPi creates a simple WSPR beacon on your Raspberry Pi by generating a Pulse-Width Modulation (PWM) square-wave signal through a General-Purpose Input/Output (GPIO) pin. As of version 3.0.0, support for the inexpensive Si5351 clock generator was added, allowing use of the more capable Raspberry Pi 5.

You connect the generated output through a [Low-Pass Filter to remove harmonics](https://www.nutsvolts.com/magazine/article/making\_waves\_) and then to an appropriate antenna.

:::{warning}
Do not use WsprryPi without an appropriate low-pass filter. Unfiltered output can create harmonic interference on other bands.
:::

## Attribution

This idea likely originated with Oliver Mattos and Oskar Weigl at the PiFM project. While the website is no longer online, the Wayback Machine has [the last known good version]( http://web.archive.org/web/20131016184311/http://www.icrobotics.co.uk/wiki/index.php/Turning_the_Raspberry_Pi_Into_an_FM_Transmitter).

The icrobotics.co.uk website still hosts the original PiFM code. However, I suspect the domain has fallen into disrepair and may be unsafe, and I will not provide direct links here. Use the URL above to see the site; should the code disappear, I have [saved it here](https://github.com/WsprryPi/WsprryPi/raw/refs/heads/main/historical/pifm.tar.gz).

After a conversation with Bruce Raymond of TAPR, I forked @threeme3's repo and added rudimentary installation capabilities and orchestration. Version 1.x of this project was a fork of threeme3/WsprryPi (no longer on GitHub), licensed under the GNU General Public License v3 (GPLv3). The original project is no longer maintained.

In late 2024, George [K9TRV] of TAPR contacted me with questions about using WsprryPi on the Pi 5. The conversation led me to discard the original code in favor of a more modern, extensible, and maintainable base.

As of Version 2.0+, all of the original code has been replaced with my own; it is no longer derivative work, and I have released it under the MIT license.

My goal, and where you will validate my success, is to let you execute one command on your Pi to install and run the WsprryPi software. If you are lucky and have been living right, a radio wave will hit the cosmos and be received [somewhere else](https://wsprnet.org).

## Raspberry Pi model compatibility

Compatibility depends on both the Raspberry Pi model and transmitter type.

| Model | GPIO | Si5351 |
| --- | --- | --- |
| Raspberry Pi 1 Model B | <span class="compatibility-status compatibility-status--tested">Tested</span> | <span class="compatibility-status compatibility-status--tested">Tested</span> |
| Raspberry Pi 1 Model A | <span class="compatibility-status compatibility-status--tested">Tested</span> | <span class="compatibility-status compatibility-status--tested">Tested</span> |
| Raspberry Pi 1 Model B+ | <span class="compatibility-status compatibility-status--tested">Tested</span> | <span class="compatibility-status compatibility-status--tested">Tested</span> |
| Raspberry Pi 1 Model A+ | <span class="compatibility-status compatibility-status--tested">Tested</span> | <span class="compatibility-status compatibility-status--tested">Tested</span> |
| Raspberry Pi 2 Model B | <span class="compatibility-status compatibility-status--tested">Tested</span> | <span class="compatibility-status compatibility-status--tested">Tested</span> |
| Raspberry Pi 3 Model B | <span class="compatibility-status compatibility-status--tested">Tested</span> | <span class="compatibility-status compatibility-status--tested">Tested</span> |
| Raspberry Pi 3 Model B+ | <span class="compatibility-status compatibility-status--tested">Tested</span> | <span class="compatibility-status compatibility-status--tested">Tested</span> |
| Raspberry Pi 3 Model A+ | <span class="compatibility-status compatibility-status--tested">Tested</span> | <span class="compatibility-status compatibility-status--tested">Tested</span> |
| Raspberry Pi 4 Model B | <span class="compatibility-status compatibility-status--tested">Tested</span> | <span class="compatibility-status compatibility-status--tested">Tested</span> |
| Raspberry Pi 5 | <span class="compatibility-status compatibility-status--tested">Tested</span> | <span class="compatibility-status compatibility-status--tested">Tested</span> |
| Raspberry Pi Zero | <span class="compatibility-status compatibility-status--tested">Tested</span> | <span class="compatibility-status compatibility-status--tested">Tested</span> |
| Raspberry Pi Zero W | <span class="compatibility-status compatibility-status--tested">Tested</span> | <span class="compatibility-status compatibility-status--tested">Tested</span> |
| Raspberry Pi Zero 2 W | <span class="compatibility-status compatibility-status--tested">Tested</span> | <span class="compatibility-status compatibility-status--tested">Tested</span> |
| Raspberry Pi 400 | <span class="compatibility-status compatibility-status--untested">Untested</span> | <span class="compatibility-status compatibility-status--untested">Untested</span> |
| Raspberry Pi 500 | <span class="compatibility-status compatibility-status--untested">Untested</span> | <span class="compatibility-status compatibility-status--untested">Untested</span> |
| Raspberry Pi 500+ | <span class="compatibility-status compatibility-status--untested">Untested</span> | <span class="compatibility-status compatibility-status--untested">Untested</span> |

- <span class="compatibility-status compatibility-status--tested">Tested</span>: WsprryPi operation has been recorded on this model and transmitter type.
- <span class="compatibility-status compatibility-status--untested">Untested</span>: The hardware is expected to support this transmitter type, but model-specific operation has not been recorded.
- <span class="compatibility-status compatibility-status--unsupported">Not supported</span>: WsprryPi cannot use this transmitter type on the model.

## Compute Module compatibility

Compute Modules retain the GPIO and I2C capabilities of their corresponding Raspberry Pi generation, but they do not include GPIO headers. Their carrier board must route the connections required by the selected transmitter. Although these configurations are untested, they are expected to work; generation-specific restrictions, including the Compute Module 5 GPIO limitation, still apply.

## Raspberry Pi Pico incompatibility

Raspberry Pi Pico boards are microcontrollers and cannot run the Linux
WsprryPi application or its GPIO and Si5351 backends. A Pico 2 W running
WsprryPico firmware can instead serve as an external output controlled by
WsprryPi over USB or a network connection. The Pi remains the controller and
can manage several outputs through Fleet. See
[Add a WsprryPico](../Install/pico.md) for preparation and Pi setup. Standalone
Pico use, hardware limits and firmware details are in the companion
[WsprryPico manual](https://wsprrypico.readthedocs.io/en/devel/).

## Transmitter qualification

Qualification is specific to the transmitter type, band, and GPIO clock profile.

### GPIO clock profiles

The GPIO hardware falls into three groups: the original Pi 1 family, Pi 2–4, and Pi 5. The SoC or package determines the oscillator frequency and GPIO clock source; Pi 2–4 do not all use the same PLLD frequency.

In the table, **SoC** means system on chip and **CM** means Compute Module. Clock frequencies are nominal.

| Pi models | SoC or package | GPIO clock source | Oscillator |
| --- | --- | --- | --- |
| Pi 1 A/A+/B/B+; Zero/Zero W; CM1 | <a href="https://www.raspberrypi.com/documentation/computers/processors.html#bcm2835">BCM2835</a> | 500 MHz PLLD | 19.2 MHz |
| Pi 2 B (original revisions) | <a href="https://www.raspberrypi.com/documentation/computers/processors.html#bcm2836">BCM2836</a> | 500 MHz PLLD | 19.2 MHz |
| Pi 2 B (revision 1.2); Pi 3 B; CM3 | <a href="https://www.raspberrypi.com/documentation/computers/processors.html#bcm2837">BCM2837</a> | 500 MHz PLLD | 19.2 MHz |
| Pi 3 A+/B+; CM3+ | <a href="https://www.raspberrypi.com/documentation/computers/processors.html#bcm2837b0">BCM2837B0</a> | 500 MHz PLLD | 19.2 MHz |
| Zero 2 W | <a href="https://www.raspberrypi.com/documentation/computers/processors.html#rp3a0">RP3A0</a> (BCM2710A1 die) | 500 MHz PLLD | 19.2 MHz |
| Pi 4 B; Pi 400; CM4/CM4S | <a href="https://www.raspberrypi.com/documentation/computers/processors.html#bcm2711">BCM2711</a> | 750 MHz PLLD | 54 MHz |
| Pi 5 | <a href="https://www.raspberrypi.com/documentation/computers/processors.html#bcm2712">BCM2712</a> / RP1 GPIO | 200 MHz PLL_SYS | 50 MHz |

### Band qualification

| Band | GPIO: Pi 1–3<br>500 MHz PLLD | GPIO: Pi 4<br>750 MHz PLLD | GPIO: Pi 5<br>200 MHz PLL_SYS | Si5351 |
| --- | --- | --- | --- | --- |
| 2200 m | <span class="qualification-status qualification-status--partial">Partial</span><sup>1</sup> | <span class="qualification-status qualification-status--qualified">Qualified</span><sup>2</sup> | <span class="qualification-status qualification-status--qualified">Qualified</span> | <span class="qualification-status qualification-status--qualified">Qualified</span> |
| 630 m | <span class="qualification-status qualification-status--qualified">Qualified</span> | <span class="qualification-status qualification-status--qualified">Qualified</span> | <span class="qualification-status qualification-status--qualified">Qualified</span> | <span class="qualification-status qualification-status--qualified">Qualified</span> |
| 160 m | <span class="qualification-status qualification-status--qualified">Qualified</span> | <span class="qualification-status qualification-status--qualified">Qualified</span> | <span class="qualification-status qualification-status--qualified">Qualified</span> | <span class="qualification-status qualification-status--qualified">Qualified</span> |
| 80 m | <span class="qualification-status qualification-status--qualified">Qualified</span> | <span class="qualification-status qualification-status--qualified">Qualified</span> | <span class="qualification-status qualification-status--qualified">Qualified</span> | <span class="qualification-status qualification-status--qualified">Qualified</span> |
| 60 m | <span class="qualification-status qualification-status--qualified">Qualified</span> | <span class="qualification-status qualification-status--qualified">Qualified</span> | <span class="qualification-status qualification-status--qualified">Qualified</span> | <span class="qualification-status qualification-status--qualified">Qualified</span> |
| 40 m | <span class="qualification-status qualification-status--qualified">Qualified</span> | <span class="qualification-status qualification-status--qualified">Qualified</span> | <span class="qualification-status qualification-status--qualified">Qualified</span> | <span class="qualification-status qualification-status--qualified">Qualified</span> |
| 30 m | <span class="qualification-status qualification-status--qualified">Qualified</span> | <span class="qualification-status qualification-status--qualified">Qualified</span> | <span class="qualification-status qualification-status--qualified">Qualified</span> | <span class="qualification-status qualification-status--qualified">Qualified</span> |
| 22 m | <span class="qualification-status qualification-status--qualified">Qualified</span> | <span class="qualification-status qualification-status--qualified">Qualified</span> | <span class="qualification-status qualification-status--qualified">Qualified</span> | <span class="qualification-status qualification-status--qualified">Qualified</span> |
| 20 m | <span class="qualification-status qualification-status--qualified">Qualified</span> | <span class="qualification-status qualification-status--qualified">Qualified</span> | <span class="qualification-status qualification-status--qualified">Qualified</span> | <span class="qualification-status qualification-status--qualified">Qualified</span> |
| 17 m | <span class="qualification-status qualification-status--qualified">Qualified</span> | <span class="qualification-status qualification-status--qualified">Qualified</span> | <span class="qualification-status qualification-status--qualified">Qualified</span> | <span class="qualification-status qualification-status--qualified">Qualified</span> |
| 15 m | <span class="qualification-status qualification-status--qualified">Qualified</span> | <span class="qualification-status qualification-status--qualified">Qualified</span> | <span class="qualification-status qualification-status--qualified">Qualified</span> | <span class="qualification-status qualification-status--qualified">Qualified</span> |
| 12 m | <span class="qualification-status qualification-status--unqualified">Unqualified</span> | <span class="qualification-status qualification-status--unqualified">Unqualified</span> | <span class="qualification-status qualification-status--qualified">Qualified</span> | <span class="qualification-status qualification-status--qualified">Qualified</span> |
| 10 m | <span class="qualification-status qualification-status--qualified">Qualified</span> | <span class="qualification-status qualification-status--qualified">Qualified</span> | <span class="qualification-status qualification-status--qualified">Qualified</span> | <span class="qualification-status qualification-status--qualified">Qualified</span> |
| 6 m | <span class="qualification-status qualification-status--unqualified">Unqualified</span> | <span class="qualification-status qualification-status--unqualified">Unqualified</span> | <span class="qualification-status qualification-status--unqualified">Unqualified</span> | <span class="qualification-status qualification-status--qualified">Qualified</span> |
| 4 m | <span class="qualification-status qualification-status--unqualified">Unqualified</span> | <span class="qualification-status qualification-status--unqualified">Unqualified</span> | <span class="qualification-status qualification-status--unqualified">Unqualified</span> | <span class="qualification-status qualification-status--qualified">Qualified</span> |
| 2 m | <span class="qualification-status qualification-status--unavailable">Unavailable</span><sup>4</sup> | <span class="qualification-status qualification-status--unqualified">Unqualified</span> | <span class="qualification-status qualification-status--unavailable">Unavailable</span><sup>4</sup> | <span class="qualification-status qualification-status--qualified">Qualified</span><sup>3</sup> |
| 1.25 m | <span class="qualification-status qualification-status--unavailable">Unavailable</span><sup>4</sup> | <span class="qualification-status qualification-status--unavailable">Unavailable</span><sup>4</sup> | <span class="qualification-status qualification-status--unavailable">Unavailable</span><sup>4</sup> | <span class="qualification-status qualification-status--unavailable">Unavailable</span><sup>4</sup> |
| 70 cm | <span class="qualification-status qualification-status--unavailable">Unavailable</span><sup>4</sup> | <span class="qualification-status qualification-status--unavailable">Unavailable</span><sup>4</sup> | <span class="qualification-status qualification-status--unavailable">Unavailable</span><sup>4</sup> | <span class="qualification-status qualification-status--unavailable">Unavailable</span><sup>4</sup> |

1. On 2200 m, the 500 MHz PLLD profile is qualified for TONE, QRSS, FSKCW, and DFCW; WSPR did not meet the decode requirement.
2. On 2200 m the Pi 4 uses the 54 MHz oscillator, instead of the usual 750 MHz PLLD.
3. Si5351 qualification on 2 m requires the tested 27 MHz reference configuration. A 25 MHz reference did not pass 2 m qualification testing and is unqualified.
4. Today we have direct-output planning, not implemented or qualified harmonic operation. Harmonic operations are a feasible development direction; usable power, spectral cleanliness, and modulation quality remain to be measured.

- <span class="qualification-status qualification-status--qualified">Qualified</span>: The transmitter type produced usable output on that band during qualification testing.
- <span class="qualification-status qualification-status--partial">Partial</span>: At least one supported mode is qualified on that band and at least one other mode is not. Check the numbered note before transmitting.
- <span class="qualification-status qualification-status--unqualified">Unqualified</span>: The backend and mode combination did not meet the applicable carrier or decode gate. WsprryPi blocks the combination by default. An operator with appropriate authorization may enable it with the explicit experimental override and remains responsible for RF-path safety, filtering, and compliance with applicable rules.
- <span class="qualification-status qualification-status--unavailable">Unavailable</span>: The backend cannot safely construct this output. Experimental overrides do not enable it.

For local qualification testing, use a conducted, suitably attenuated and filtered path into a receiver or SDR. Begin and end with a known-qualified control, verify the requested carrier and mode behavior, and confirm that RF output is disabled afterward. Use [`--allow-unqualified-frequency`](../Command_Line_Operations/transmitter_backends.md) only for a controlled test of an Untested or Unqualified combination; it cannot enable an Unavailable combination.

See [GPIO Band Capabilities and Signal Quality](../FAQ/why_12m_looks_noisy.md) for the GPIO qualification findings.
