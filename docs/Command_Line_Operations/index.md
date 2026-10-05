# Command Line Options

WsprryPi normally runs as a `systemd` service. Use these pages when you need shell-based testing, calibration, direct WSPR or CW transmissions, hardware backend selection, or service controls.

Start with [Command-Line Quick Start](quick_start.md) before running a manual command. It explains how to stop the managed service safely and shows the supported command forms. For ordinary day-to-day configuration, use the [User Interface](../User_Interface/index.md).

```{toctree}
:maxdepth: 1
:hidden:

Command-Line Quick Start <quick_start>
General and WSPR Options <wspr_options>
Transmitter Backend Options <transmitter_backends>
CW Mode Options <cw_modes>
Service, GPIO, and Test Controls <service_test_controls>
```

## Topics

(systemd-service)=
(command-line-overview)=
(usage)=
(common-examples)=
(positional-arguments)=
- [Command-Line Quick Start](quick_start.md) covers the managed service, CLI forms, common examples, and direct WSPR positional arguments.

(general-options)=
(wspr-behavior)=
(wspr-message-types)=
- [General and WSPR Options](wspr_options.md) documents common process controls, repeat behavior, offset selection, and WSPR message planning.

(backend-selection)=
(gpio-backend)=
(si5351-backend)=
- [Transmitter Backend Options](transmitter_backends.md) distinguishes direct GPIO RF output from the Si5351 clock-generator backend.

(cw-qrss-fskcw-dfcw-modes)=
(timing)=
(spacing)=
(envelope-control)=
- [CW Mode Options](cw_modes.md) documents QRSS, FSKCW, and DFCW message, frequency, timing, spacing, and envelope controls.

(service-and-gpio-controls)=
(test-tone)=
(notes)=
- [Service, GPIO, and Test Controls](service_test_controls.md) covers web and socket ports, indicator and shutdown GPIOs, test tones, and operational qualifications.
