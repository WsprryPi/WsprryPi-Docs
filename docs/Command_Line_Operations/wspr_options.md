# General and WSPR Options

## General Options

- `-h`, `--help`  
  Display help text and exit. This is processed early and does not require root.

- `-v`, `--version`  
  Print version information and exit.

- `-i`, `--ini-file <file>`  
  Load configuration from an INI file. When used, CLI transmission options are
  disabled or restricted, and the program runs in daemon-style mode.

- `--controller-only -i <file>`<br /> Start the controller service without a local transmitter. Setup opens Fleet, and Operations identifies the controller as having no local output. The process does not require a local callsign or locator, select an output backend, or initialize transmitter GPIO. Transmitter CLI options are rejected in this role.

  The existing regular INI file locates the controller's adjacent device catalog, Fleet assignments, and recovery journal. Only its `[Operation]` listener ports and `[Security]` network-safety setting are read; local station and output values are left unchanged. Missing listener ports use 31415 and 31416. The controller identity is assigned automatically on Linux and macOS. Startup fails if that identity or its saved controller state cannot be validated.

  `--web-port`, `--socket-port`, `--socket-loopback-only`, `--no-web`, `--no-http`, and the logging options below are supported. Listener ports must be distinct integers from 1024 through 49151 when both listeners are enabled. Port and role changes require an explicit process restart. Stop this process with Ctrl-C or SIGTERM; it does not turn into a transmitter after a reload or failed initialization.

  Pair another Pi through [Maintenance → Controller access](../User_Interface/Maintenance/index.md#controller-access), then choose the verified device under Setup to manage its settings and native schedule. A saved Pico management profile provides access to that Pico’s supported settings.

  `GET /status` reports controller readiness separately from target availability, with `local_output: null`. Existing Fleet and device-catalog interfaces remain available behind the normal network and browser-request checks. Local configuration, output-selection, transmission, and machine-power commands are refused, and their browser controls are unavailable. Choose the verified transmitter under Setup’s **Device** selector to manage it. Its native schedule remains independent of the controller’s output selection.

- `-r`, `--repeat`  
  Repeat transmissions indefinitely in direct CLI mode.

- `-x`, `--terminate <count>`  
  Stop after a specified number of transmissions.

- `-J`, `--journald`  
  Send logs to the systemd journal instead of stdout.

- `-D`, `--date-time-log`  
  Prefix log lines with UTC timestamps.

- `--debug-logging`, `--no-debug-logging`  
  Enable or disable debug-level logging output.

---

## WSPR Behavior

- `--planner-preference <auto\|prefer_paired\|require_paired>`  
  Controls WSPR message planning. The default `auto` mode uses a normal single
  WSPR frame when possible and allows the planner to choose paired handling when
  needed. `prefer_paired` asks the planner to use paired handling when it is
  available. `require_paired` rejects a transmission if the supplied identity
  cannot be represented with the paired-message strategy.

- `-o`, `--offset`<br />Select a uniform placement within ±80 Hz once per prepared WSPR plan. Both frames of a pair retain it. Each independent plan receives a fresh draw, which may repeat the previous value.

- `--no-offset`<br />Use zero random placement. Test Tone never uses random placement.

### WSPR Message Types

The CLI supports WSPR message planning. Direct CLI WSPR input is passed through the same WSPR planning path used by the rest of the application.

- **Type 1** is the normal single-frame WSPR message form for standard callsign, grid, and power combinations.
- **Type 2** supports compound or extended identity cases by transmitting a callsign-hash-oriented frame as part of a paired strategy.
- **Type 3** supports the complementary extended identity information needed for paired decoding.

For ordinary callsigns and four-character grid squares, no special option is usually needed. For identities that require Type 2/Type 3 handling, use `--planner-preference` when you want to prefer or require paired planning.
