# WsprryPi

WsprryPi is a Raspberry Pi-based transmitter for amateur radio operators who want to explore propagation with WSPR. The project focuses on making a low-cost, low-complexity beacon practical to install, configure, and operate on common Raspberry Pi hardware.

WsprryPi can use local transmitter hardware or control external Pi and Pico
outputs. To add a Pico 2 W running WsprryPico and manage output schedules, see
[Add a WsprryPico](Install/pico.md). The companion
[WsprryPico manual](https://wsprrypico.readthedocs.io/en/devel/) covers standalone
use, device-side setup and deeper Pico details.
Qualification depends on
the backend, Raspberry Pi clock profile, band, and transmission mode. Check the
[Band qualification](About_Wsprry_Pi/index.md#band-qualification) table before
choosing hardware or a mode for a band. See
[GPIO Band Capabilities and Signal Quality](FAQ/why_12m_looks_noisy.md) for the
measured GPIO signal-quality findings.

As of version 3.0.0, several CW capabilities were added to the suite:

- QRSS: The name “QRSS” is a derivation of the Q code “QRS”, a phrase Morse code operators send to indicate the transmitter needs to slow down. The extra “S” means slow way, way down.
- FSKCW: Frequency Shift Keying CW is a variant of QRSS. Instead of switching the carrier on and off, FSKCW keeps it active for the transmission and shifts the frequency downward during gaps between elements and characters.
- DFCW: Dual Frequency CW is a combination of QRSS and FSKCW. In DFCW, the element duration is replaced by the element frequency, speeding transmissions considerably.

To configure these modes, see [Configure WSPR and CW](User_Interface/Setup/Signal_Setup/index.md). For their direct command-line controls, see [CW Mode Options](Command_Line_Operations/cw_modes.md). [Scott Harden's AJ4VD website](https://swharden.com/blog/tags/#qrss) provides additional QRSS background and experiments.

This documentation is organized to help you move through the project in a practical order:

- Learn what WSPR is and how WsprryPi works.
- Install the software and required supporting services.
- Configure and operate the system through the web UI or command line.
- Use the reference and FAQ material when you need detail or troubleshooting.

```{toctree}
:maxdepth: 2
:caption: Start Here

About_WSPR/index
About_Wsprry_Pi/index
Install/index
Install/pico
```

```{toctree}
:maxdepth: 2
:caption: Operate WsprryPi

User_Interface/index
Command_Line_Operations/index
Advanced_Operations/index
Support/index
```

```{toctree}
:maxdepth: 2
:caption: Reference

Internals/index
Development/index
FAQ/index
Additional_Reading/index
```
