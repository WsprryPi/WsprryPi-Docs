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
  Generate a continuous RF tone. Enter a positive whole-number frequency in
  hertz, or add an `Hz`, `kHz`, `MHz`, or `GHz` suffix to a decimal value that
  resolves to whole-number hertz. Scientific notation and fractional-hertz
  results are rejected. A band alias selects the effective WSPR RF center: its USB dial plus
  1,500 Hz, without random placement. For example, `--test-tone 20m` targets
  14,097,100 Hz with the standard preset.

An explicit numeric Test Tone frequency is the requested RF carrier; no WSPR audio offset is added. For example, `--test-tone 14097100` targets 14,097,100 Hz. On the legacy GPIO backend, an unsafe clock-divider boundary causes the request to fail instead of moving the carrier. Choose a nearby valid frequency and review the new request before trying again. A successful start reports the synthesis target, not a measured RF frequency.

For clock-error measurements, see [Interpreting Test Tone Measurements](../Advanced_Operations/timing_calibration.md#interpreting-test-tone-measurements).

---

## Notes

- Direct CLI options are transient. Saved service settings use SQLite; listener edits require backend restart. See [Saved Settings and Local Maintenance](saved_settings.md).
- Some advanced features are CLI-only.
- Root privileges (`sudo`) are required for RF output.
