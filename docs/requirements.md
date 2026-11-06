# What you need

Start with one Raspberry Pi and one local transmitter output. Add remote Pi or
Pico outputs after learning the local controls. Before installing, choose a
hardware path and prepare its RF connections.

## Choose an output

| Output | What to prepare | Details |
| --- | --- | --- |
| Raspberry Pi GPIO | A compatible Pi and a filtered, DC-blocked, protected GPIO RF path | [Model and band qualification](About_Wsprry_Pi/index.md#raspberry-pi-model-compatibility) and [RF wiring](Advanced_Operations/rf_electrical.md) |
| External Si5351 | A compatible clock-generator board, the correct reference settings, I2C wiring, and a suitable RF path | [Transmitter configuration](User_Interface/Setup/Transmitter/index.md#si5351) |
| WsprryPico | An installed Pi controller, a Pico 2 W running compatible firmware, and USB or a prepared network connection | [Add a WsprryPico](Install/pico.md) |

A model marked **Tested** does not qualify every band or mode. Check the
[band qualification table and its numbered notes](About_Wsprry_Pi/index.md#band-qualification)
for the selected output. Pi qualification does not qualify Pico output.

On Pi 5-family systems, GPIO output requires the installer-managed RP1 GPCLK
provider and an explicitly selected route. A fresh installation leaves output
disabled and neither route selected. See [RP1 GPCLK](Advanced_Operations/rp1_gpclk.md).

## Prepare the Pi and browser

- A Raspberry Pi, an SD card, and a regulated power supply with good ripple suppression.
- A working Raspberry Pi OS installation with internet access and command-line
  access through SSH or a local console. Follow [installation prerequisites](Install/index.md#prerequisites)
  for OS and installer-channel details.
- A computer or phone with a [supported browser](User_Interface/index.md#browser-requirements)
  and access to the Pi's directly connected network.
- Synchronized UTC on the Pi. The installer configures Chrony; check
  [timing and calibration](Advanced_Operations/timing_calibration.md) if clock
  synchronization or RF frequency accuracy needs attention.

The installer supplies the application, web interface, and supporting services.
It changes the Pi's web-server and time-service configuration and disables the
onboard audio path. Review [System Changes](Install/index.md#system-changes)
before installing on a Pi that already runs other services.

## Prepare the station and RF path

Have the station callsign, Maidenhead locator, intended band, and reported WSPR
power ready. Reported power is message content; it does not set or measure
actual RF output. Choose settings appropriate to the station and its operating
authorization.

```{warning}
Do not connect an antenna directly to an unfiltered GPIO RF pin. Prepare suitable
filtering, DC blocking, isolation, and electrical protection before transmission.
Do not connect amplifier keying inputs or a resistive dummy load directly to GPIO.
Read the RF and Electrical Reference before wiring.
```

Use the [RF and Electrical Reference](Advanced_Operations/rf_electrical.md) to
prepare a suitable test path. For on-air use, prepare an appropriate antenna
and filtering for the selected band. Changing bands may require a different
filter; software configuration does not verify the filter or measure emissions.

## Install and continue

Use [Installing WsprryPi](Install/index.md) for a normal Pi installation. That
page distinguishes stable-channel commands from the explicit beta procedure.
Linux and macOS USB Si5351 installations have separate guides under
**Optional Setups**.

After installation, follow [Your first WSPR transmission](first_transmission.md).
