# RF and Electrical Reference

## PWM Peripheral

The GPIO RF backend uses the Raspberry Pi PWM peripheral to time the frequency transitions of the output clock.

The Raspberry Pi sound subsystem also uses this peripheral, so sound activity during a WSPR transmission can interfere with transmission quality.

The install script disables the onboard audio path automatically, so most users do not need to make manual changes.

This restriction applies only to the direct GPIO RF backend. External hardware backends such as Si5351 are not affected.

## RF and Electrical Considerations

The GPIO RF backend produces a square-wave RF clock, so a low-pass filter is required.

For the reasoning behind that requirement, see {doc}`../FAQ/lowpass-filter-justification`.

Connect a low-pass filter through a DC-blocking capacitor to the configured GPIO4 or GPIO20 `GPCLK0` RF output and a ground pin on the Raspberry Pi before connecting an antenna.

GPIO4 is on header pin 7, and GPIO20 is on header pin 38. Header pin 9 is a nearby ground connection.

See:

- http://elinux.org/RPi_Low-level_peripherals

for Raspberry Pi pin layout details.

Examples of low-pass filters can be found here:

- http://www.gqrp.com/harmonic_filters.pdf

TAPR also offers a Raspberry Pi shield with filtering and amplification:

- https://www.tapr.org/kits_20M-wsprrypi-pi.html

The expected RF power output from the GPIO backend is configurable from the command line, INI file, or Web UI.

Even at low power levels, WSPR transmissions are commonly received over very long distances.

Because the Raspberry Pi does not strongly attenuate ripple and noise from the 5 V supply, use a regulated power supply with good ripple suppression.

Supply ripple can appear as mixing products centered around the transmit carrier, typically at 100 Hz or 120 Hz.

Do not expose GPIO pins to voltages or currents above the Raspberry Pi absolute maximum ratings.

The selected GPIO RF pin outputs a 3.3 V digital clock with a maximum current of approximately 16 mA.

Do not:

- Short the selected GPIO RF output directly to ground
- Connect a resistive dummy load directly to the GPIO
- Connect external amplifier keying circuitry directly to GPIO pins

Use appropriate isolation when controlling external amplifiers.

Most amplifiers expect their control line to be switched relative to chassis ground, which usually requires:

- A relay
- An SSR
- A MOSFET driver
- Or another isolated switching stage

Do not connect amplifier keying inputs directly to Raspberry Pi GPIO pins.

A DC-blocking capacitor should always be used when connecting transformers, filters, or antennas to the GPIO RF output.

Antennas can also expose GPIO pins to:

- Static discharge
- Induced RF energy
- Lightning transients

Some form of isolation and protection is strongly recommended.
