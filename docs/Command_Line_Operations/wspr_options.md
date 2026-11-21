# General and WSPR Options

## General Options

- `-h`, `--help`  
  Display help text and exit. This is processed early and does not require root.

- `-v`, `--version`  
  Print version information and exit.

- `--state-directory <directory>` Start the backend using its admitted private application state. The installed Pi service uses `/var/lib/wsprrypi/application-state`. Do not point another process at a live installation's state or delete the directory to bypass recovery. `-i` / `--ini-file` is retired from normal startup; see [one-time migration](../Advanced_Operations/ini_configuration.md).

- `--controller-only --state-directory <directory>` Start the existing controller-only role without local output, local callsign/grid requirements, or transmitter GPIO initialization. Role and listener changes require explicit process restart. This is distinct from a normal Pi's hybrid operation: a transmitter Pi can run its local schedule and manage Fleet devices together without a hybrid flag.

  Pair another Pi through [Maintenance → Controller access](../User_Interface/Maintenance/index.md#controller-access), then select it under Setup's **Device** selector. Each target retains its own schedule and authority. Local transmitter and machine-power controls are unavailable in controller-only mode. A dedicated controller-only distribution and additional native platform service integrations remain separate work; this role does not establish their availability.

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
