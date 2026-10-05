# WsprryPi System Internals

The system consists of the following:

- `wsprrypi` (executable): Installed to `/usr/local/bin/wsprrypi`
- `wsprrypi.ini` (configuration): Installed to `/usr/local/etc/wsprrypi.ini`
- `wsprrypi.service` (service control file): Installed to `/lib/systemd/system/wsprrypi.service`
- WsprryPi Web UI: Installed to `/var/www/html/wsprrypi`

The primary data flow is as follows:

![Data Flow Diagram](wsprrypi_data_flow.svg)

## Log Files

As of 2.2.x, the `wsprrypi` service will log messages to the Debian `systemd-journald` facility.

See the section on the [Log Panel](../User_Interface/Logs/index.md) for more information.
