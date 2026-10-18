# Service, GPIO, and Test Controls

## Service and GPIO Controls

- `--no-web`  
  Disable Web UI and WebSocket server.

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
  results are rejected. A band alias selects that band's WSPR dial frequency,
  not its WSPR carrier frequency; use an explicit value for another carrier.

An explicit numeric Test Tone frequency is the requested RF carrier; no WSPR
audio offset is added. For example, `--test-tone 14097100` targets 14,097,100 Hz.
On the legacy GPIO backend, an unsafe clock-divider boundary causes the request
to fail instead of moving the carrier. Choose a nearby valid frequency and
review the new request before trying again. A successful start reports the
synthesis target, not a measured RF frequency.

For clock-error measurements and older GPIO tone records, see
[Interpreting Test Tone Measurements](../Advanced_Operations/timing_calibration.md#interpreting-test-tone-measurements).

---

## Notes

- CLI options override INI values unless restricted.
- Some advanced features are CLI-only.
- Root privileges (`sudo`) are required for RF output.

## Managed WTP listener port

- `--wtp-server-port <port>` overrides the managed Pi WTP listener's port for
  this process. Valid values are `1` through `65535`; the saved default is
  `31417` in `[WTP Server]`.

The override does not rewrite the INI. DNS-SD advertises the actual listening
port, including an override. This option does not enable local RF, create a
remote assignment, or make a direct one-shot command start the managed server.
See [WTP Server configuration](../Advanced_Operations/ini_configuration/runtime.md#wtp-server)
for admission and interface selection. The Pi endpoint's finite remote TONE
job is separate from the continuous local `--test-tone` control above.
