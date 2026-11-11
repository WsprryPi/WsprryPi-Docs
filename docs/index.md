# WsprryPi

WsprryPi turns a Raspberry Pi into a low-power amateur radio transmitter for
WSPR propagation experiments and slow Morse-code modes. Configure a station
and transmission schedule in its web interface, then use reception reports to
see where the signal was heard.

The Pi can generate RF through a GPIO clock output or use an external Si5351
clock generator. It can also control remote Pi and WsprryPico outputs through
Fleet. Each output needs suitable RF filtering and a band and mode supported
by that hardware.

## Start with one station

1. Read [About WsprryPi](About_Wsprry_Pi/index.md) for the project overview and
   hardware compatibility. [About WSPR](About_WSPR/index.md) explains the protocol.
2. Check [What you need](requirements.md) before choosing hardware or installing.
3. [Install WsprryPi](Install/index.md) on the Pi.
4. Follow [Your first WSPR transmission](first_transmission.md) to configure,
   start, monitor, and stop one local station.
5. Use the [User Interface guide](User_Interface/index.md) for everyday settings
   and controls. Turn to [FAQ and Known Errors](FAQ/index.md) or
   [Support](Support/index.md) when something needs attention.

## Other operating paths

For shell-based operation, use [Command-Line Quick Start](Command_Line_Operations/quick_start.md).
To add an external Pico 2 W after installing the Pi, use
[Add a WsprryPico](Install/pico.md). We strongly recommend
{ref}`starting with standalone operation <start-with-standalone-operation>`
to learn the Pico's local capabilities before using Fleet. Its companion
[manual](https://wsprrypico.readthedocs.io/en/devel/) covers device setup and recovery.

Qualification depends on the backend, Raspberry Pi clock profile, band, and
transmission mode. Check the
[Band qualification](About_Wsprry_Pi/index.md#band-qualification) table before
choosing hardware or a mode for a band. See
[GPIO Band Capabilities and Signal Quality](FAQ/why_12m_looks_noisy.md) for the
measured GPIO findings.

## Slow Morse-code modes

WsprryPi also supports these slow Morse-code modes:

- QRSS: The name “QRSS” derives from the Q code “QRS”, a phrase Morse code operators send to indicate the transmitter needs to slow down. The extra “S” means slow way, way down.
- FSKCW: Frequency Shift Keying CW is a variant of QRSS. Instead of switching the carrier on and off, FSKCW keeps it active for the transmission and shifts the frequency downward during gaps between elements and characters.
- DFCW: Dual Frequency CW combines QRSS and FSKCW. In DFCW, the element duration is replaced by the element frequency, speeding transmissions considerably.

To configure these modes, see [Configure WSPR and CW](User_Interface/Setup/Signal_Setup/index.md). For their direct command-line controls, see [CW Mode Options](Command_Line_Operations/cw_modes.md). [Scott Harden's AJ4VD website](https://swharden.com/blog/tags/#qrss) provides additional QRSS background and experiments.

```{toctree}
:maxdepth: 2
:caption: Start Here
:hidden:

About_Wsprry_Pi/index
requirements
Install/index
first_transmission
```

```{toctree}
:maxdepth: 2
:caption: Configure and Operate
:hidden:

User_Interface/index
Command_Line_Operations/index
```

```{toctree}
:maxdepth: 2
:caption: Troubleshooting and Support
:hidden:

FAQ/index
Support/index
```

```{toctree}
:maxdepth: 1
:caption: Optional Setups
:hidden:

Install/pico
Install/beta7
Install/linux_si5351
Install/macos_si5351
```

```{toctree}
:maxdepth: 2
:caption: Advanced and Reference
:hidden:

About_WSPR/index
Advanced_Operations/index
Additional_Reading/validation_platform
Internals/index
Development/index
Additional_Reading/index
```
