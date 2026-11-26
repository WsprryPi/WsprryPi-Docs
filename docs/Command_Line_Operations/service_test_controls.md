# Service, GPIO, and Test Controls

## Service and GPIO Controls

- `--no-web`  
  Disable browser listener operation. With the installer’s `--no-web` option, Apache/PHP and the browser service are omitted; the backend and maintenance worker remain available. This does not disable device management transports.

- `-w`, `--web-port <port>`  
  HTTP REST API port (default: 31415).

- `-k`, `--socket-port <port>`  
  WebSocket port (default: 31416).

- `-l`, `--led_pin <gpio>`  
  Set TX LED GPIO.

- `--led-pin <gpio>`  
  Alias for LED pin.

- `--use-led`, `--no-led`  
  Enable or disable LED.

- `-s`, `--shutdown_button <gpio>`  
  Set shutdown button GPIO.

- `--shutdown-button <gpio>`  
  Alias.

- `--use-shutdown`, `--no-shutdown`  
  Enable or disable shutdown monitoring.

---

## Test Tone

- `-t`, `--test-tone <frequency>`  
  Generate a continuous RF tone. Enter a positive whole-number frequency in hertz, or add an `Hz`, `kHz`, `MHz`, or `GHz` suffix to a decimal value that resolves to whole-number hertz. Scientific notation and fractional-hertz results are rejected. A band alias or qualified WSPR preset selects its USB dial plus 1,500 Hz. For example, `--test-tone 20m` targets 14,097,100 Hz with the standard preset. Test Tone omits random placement.

A numeric Test Tone uses the exact requested RF frequency. For example, `--test-tone 14095600` targets 14,095,600 Hz. On the legacy GPIO backend, an unsafe clock-divider boundary causes the request to fail. A successful start reports the synthesis target. Use an independent measurement to verify the actual RF frequency.

An admitted numeric tone outside the amateur-band catalog leaves the band selector inactive unless the frequency includes an explicit GPIO suffix. To drive a selector, append `@<gpio>H` for active-high or `@<gpio>L` for active-low. A suffix such as `@17` defaults to active-low. The selector uses a BCM GPIO number from 0 through 27 on builds with ancillary GPIO support. Choose a pin free of conflicts with RF output, the TX LED, the shutdown button, and amplifier control. The existing [frequency overrides](transmitter_backends.md#experimental-frequency-policy) and backend checks still apply.

For clock-error measurements, see [Interpreting Test Tone Measurements](../Advanced_Operations/timing_calibration.md#interpreting-test-tone-measurements).

---

## Notes

- Direct CLI options are transient. Saved service settings use SQLite; listener edits require backend restart. See [Saved Settings and Local Maintenance](saved_settings.md).
- Some advanced features are CLI-only.
- Root privileges (`sudo`) are required for RF output.
