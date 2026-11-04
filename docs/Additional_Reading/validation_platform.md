# Validation platform

This example GPS/PPS operator platform pairs a **Raspberry Pi 4 Model B**
with a **QRP Labs QLG3 GPS receiver**. The receiver supplies serial UTC data
and a precise PPS input for the operating system's time service. WsprryPi
uses Chrony's clock-frequency estimate for GPIO RF calibration.

The connections use BCM GPIO numbering and physical numbers on the Pi's
40-pin header. Match the selected software GPIO roles to the wiring, and
remove power before changing connections. Each GPIO has one exclusive role.

## Parts and connections

| Part | Platform use |
| --- | --- |
| [Raspberry Pi 4 Model B](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#gpio) | Serial receive, PPS input, and GPIO RF output |
| [QRP Labs QLG3](https://qrp-labs.com/qlg3.html) ([kit](https://shop.qrp-labs.com/qlg3)) | GPS serial data and PPS, powered from 3.3 V |
| Connecting leads | Jumper wiring, with a joined VDD/VBAT supply lead |

## GPS/PPS wiring

![QLG3 VDD and VBAT joined to Raspberry Pi physical pin 1 at 3.3 V; GND to pin 6; GPS TX to pin 10, GPIO15 RXD; PPS to pin 12, GPIO18](../_static/images/wiring/qlg3-pi4.svg)

| <span class="no-break">QLG3</span> | Raspberry Pi connection |
| --- | --- |
| <span class="no-break">VDD</span> | Physical pin 1: 3.3 V GPS supply |
| <span class="no-break">VBAT</span> | Physical pin 1: same 3.3 V supply as VDD, powering the backup input |
| <span class="no-break">GND</span> | Physical pin 6: shared ground |
| <span class="no-break">TX</span> | Physical pin 10: GPIO15 / RXD, GPS serial output to Pi receive input |
| <span class="no-break">PPS</span> | Physical pin 12: GPIO18 PPS input |

**VDD and VBAT join to the same 3.3 V supply.** The QLG3 specifies a regulated
3.3 V supply; this platform powers VBAT alongside VDD rather than using a
separate backup battery. The QLG3 five-pin connection does not require a Pi TX
connection. See the [QLG3 documentation](https://qrp-labs.com/qlg3.html) and the
[QMX+ assembly manual, pages 62–63](https://www.qrp-labs.com/images/qmxp/manuals/assembly_2_00.pdf)
for its supply arrangement.

The serial line supplies UTC information; PPS supplies the precise second
boundary. **GPIO18 is physical pin 12**, not physical pin 18. GPIO15/RXD is
physical pin 10. Verify the board orientation and physical numbers rather than
relying on wire colors or left/right position.

## Software assignments

Configure Linux's existing GPS serial and GPIO PPS support for the connections
above. The serial input is connected to GPIO15/RXD; the system's `serial0`
alias identifies its UART. Linux's PPS GPIO assignment must match **GPIO18**.
WsprryPi does not configure the UART, PPS overlay, GPIO mux, or Chrony.

In **Setup > Transmitter > GPIO Output > Frequency calibration**, enable
**System clock estimate**. The corresponding INI setting is:

```ini
[GPIO]
Use System Clock Frequency Estimate = True
```

The GPS/PPS receiver is an optional source for Chrony. Linux/GPS services
and Chrony handle the serial and PPS inputs; WsprryPi does not directly
capture PPS on Pi 1–4 and has no PPS-input GPIO setting for this platform.
Chrony can also use network time sources without a GPS/PPS receiver.

Keep the OS-configured GPIO18 PPS input separate from RF output, LEDs,
amplifier controls, shutdown buttons, and band selectors. GPIO18 is physical
pin 12. The Linux `ppsN` device number is separate from the GPIO number.

Verify Chrony's synchronization before transmission. See
{ref}`Pi 1–4 host-frequency calibration <pi1-4-host-frequency-calibration>`
for the relationship between OS clock discipline and WsprryPi's RF model.
