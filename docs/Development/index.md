# WsprryPi Development

WsprryPi is developed as a modular Raspberry Pi application with a native C++ backend and a separate Bootstrap-based web UI.

```{toctree}
:maxdepth: 1
:hidden:

Automatic Update Polling Internals <../User_Interface/Maintenance/update_check>
```

The project officially supports Raspberry Pi 5. GPIO RF transmission on Raspberry Pi 5 requires dedicated supported hardware rather than the older direct GPIO clock path used on earlier Raspberry Pi models.

## Build Environment

Current development builds are compiled directly on the target Raspberry Pi. This avoids distributing binaries that may depend on newer `GLIBC` versions than the user's installed operating system provides.

The project is currently built with `g++` from GCC 14:

```text
gcc (Debian 14.2.0-19) 14.2.0
```

The backend is developed in modern C++.

## Repository Layout

The top-level `WsprryPi` repository contains the main application source,
configuration defaults, install scripts, documentation support, web UI, and
reusable supporting components. A normal clone contains the complete source
tree; no submodule initialization is required.

The web UI is kept as a top-level component:

```text
WsprryPi-UI/
```

The native C++ support libraries are kept under:

```text
src/
```

## Components

The component directories are ordinary files tracked by the central WsprryPi
repository. Their named roots, public interfaces, standalone build or test
entry points, and reuse boundaries remain intact. The former component
repositories are retained as historical references rather than active
synchronization targets.

### Web UI

- [WsprryPi-UI](https://github.com/WsprryPi/WsprryPi-UI): The Bootstrap-based WsprryPi web UI.

### Core Support Libraries

- [INI-Handler](https://github.com/WsprryPi/INI-Handler): A class for reading and writing formatted INI files.
- [LCBLog](https://github.com/WsprryPi/LCBLog): A logging class for formatting, writing, levels, and timestamps.
- [Mailbox](https://github.com/WsprryPi/Mailbox): The current Linux mailbox-property interface. Broadcom mailbox software is historical design lineage; the absorbed component does not contain Broadcom source.
- [MonitorFile](https://github.com/WsprryPi/MonitorFile): A class for watching a file for changes.
- [PPM-Manager](https://github.com/WsprryPi/PPM-Manager): A class for tracking and applying system clock PPM correction.
- [Signal-Handler](https://github.com/WsprryPi/Signal-Handler): A class for intercepting process signals such as `SIGINT` and allowing clean shutdown.
- [Singleton](https://github.com/WsprryPi/Singleton): A class for enforcing a single running instance.

### WSPR and Transmission Libraries

- [WSPR-Reference](https://github.com/WsprryPi/WSPR-Reference): Reference WSPR encoding and decoding support used for validation and compatibility.
- [WSPR-Transmitter](https://github.com/WsprryPi/WSPR-Transmitter): The transmission backend library that manages RF backend execution, timing, DMA-backed GPIO transmission where supported, and hardware-backed transmission paths.

## Current Component Layout

The project tracks these component paths in the main repository:

```text
WsprryPi-UI
src/INI-Handler
src/LCBLog
src/Mailbox
src/MonitorFile
src/PPM-Manager
src/Signal-Handler
src/Singleton
src/WSPR-Reference
src/WSPR-Transmitter
```

## Development Notes

This organization keeps the main application focused on configuration, scheduling, runtime orchestration, command-line handling, REST/WebSocket service behavior, and web UI integration.

The component boundaries isolate reusable pieces such as:

- INI parsing
- logging
- mailbox communication
- file monitoring
- PPM correction
- signal handling
- single-instance locking
- WSPR reference behavior
- RF transmission backends

This modular layout keeps lower-level components independently diagnosable and
allows components such as LCBLog and WSPR-Reference to be extracted for reuse
through a separately reviewed process. Original repository URLs, imported
revisions, licensing disposition, and extraction guidance are recorded in
`docs/components/provenance.md` in the WsprryPi source repository.

## Raspberry Pi 5 Support

Raspberry Pi 5 support is now official.

Because Raspberry Pi 5 hardware differs significantly from earlier Raspberry Pi models, supported transmission paths may require dedicated external hardware or backend-specific support. The older direct GPIO RF approach remains associated with earlier Raspberry Pi generations where that clocking path is supported.

## Web UI Development

The web UI lives in the `WsprryPi-UI` component. It provides the browser-based
setup, operation, logging, and maintenance interface. Its source, tests, and
deployment data are versioned with the parent application.

The main backend exposes REST and WebSocket interfaces used by the UI for:

- Reading and writing configuration
- Starting and stopping runtime actions
- Receiving transmission state updates
- Receiving configuration reload events
- Displaying version and update status
- Coordinating multi-tab browser behavior

## Backend Development

The native backend is responsible for:

- Command-line parsing
- INI and JSON configuration translation
- Runtime validation
- Scheduling
- RF backend selection
- GPIO control orchestration
- REST API service
- WebSocket service
- Update/version metadata exposure
- Integration with the web UI

## Build and Test Workflow

The project should be built from the `src` directory when using the existing make targets:

```bash
cd src
make -j$(nproc)
make -j$(nproc) release
```

Source development requires the C++ build toolchain, CMake, Python 3, Node.js,
npm, and PHP CLI. Chromium is also required for the hardware-free UI browser
integration suite. On Debian or Raspberry Pi OS, install the development
packages with:

```bash
sudo apt update
sudo apt install -y \
    git build-essential cmake pkg-config python3 \
    libgpiod-dev libsystemd-dev libssl-dev \
    nodejs npm php-cli chromium
```

Node.js is required for the complete runtime semantics validation target. Run
it from the Raspberry Pi checkout:

```bash
cd ~/WsprryPi/src
make semantics-test
```

The UI has tracked private npm manifests. Install their exact development
dependency set and run the UI suites with:

```bash
cd ~/WsprryPi/WsprryPi-UI
npm ci --ignore-scripts
npm test
npm run test:browser
```

The pinned `ws` package is used only by mocked WebSocket tests. It is not a
production or browser-runtime dependency. Chromium is used only by the
hardware-free browser integration tests. Do not commit the generated
`node_modules/` directory.

Targeted regression tests are also built and run from `src`.

Examples:

```bash
make -j$(nproc) build/bin/ui_source_regression_test
./build/bin/ui_source_regression_test

make -j$(nproc) build/bin/dial_frequency_semantics_test
./build/bin/dial_frequency_semantics_test
```

Additional tests may be available depending on the current branch and enabled build targets.
