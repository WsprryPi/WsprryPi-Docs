# WsprryPi 4.0 RC.1 installation

This prerelease provides Fleet controls on Operations and supports the published
WsprryPico `1.0.0-rc.3` firmware. The latest stable release remains `v3.2.1`.

## Install or update

Run this command on the Raspberry Pi through SSH or a local console:

```bash
curl -fsSL https://raw.githubusercontent.com/WsprryPi/WsprryPi/refs/heads/devel/scripts/install.sh | sudo env REPO_BRANCH=devel bash -s -- --binary-source release --release-tag v4.0.0-rc.1
```

Rerunning the command reinstalls the same executable version. The installer and
supporting files follow `devel`. Follow the installer prompts and reboot if requested.
The explicit release tag selects RC.1; it does not follow a newer prerelease.
For general development installation, see [Development installation](beta7.md).

The published executables cover ARMv6 and AArch64 userspaces on Raspberry Pi OS
Bookworm and Trixie. Select by operating-system release and userspace architecture,
not kernel architecture alone. The executable source is
`f88c951dcfcb03abf5cf236a02a2d9688ad49b57`; the embedded version is
`4.0.0-rc.1+f88c951d`. Source and checksums are recorded in the release manifest.

## Pico and GPIO companions

Use WsprryPico `1.0.0-rc.3` with this release. In Fleet firmware maintenance,
choose **Specific version** and enter `1.0.0-rc.3`. Choose **Download and check image**
to verify the public image, its provenance, and its settings compatibility before
installation is offered. RC.3 remains a prerelease; **Stable release** does not
select it. See [Add a WsprryPico](pico.md#compatible-software) and
[Pico firmware over USB](../User_Interface/Setup/Transmitter/index.md#install-or-update-pico-firmware-over-usb)
for settings retention and recovery.

Pi 5-family GPIO installations select the published RP1-GPIO-CLK-DKMS `v1.0.0`
provider. Driver installation, route selection, and enabling transmission remain
separate actions. Pi GPIO and Si5351 qualification do not qualify Pico output.

## Before upgrading

Back up station settings and recovery files. Disable transmission, finish or
reconcile owned jobs, and update the Pi and Pico as a compatible pair. After
upgrading, review saved and active hardware settings, complete any required restart,
and confirm the intended device, frequency, filter, and load before enabling output.

On the Operations page, select **This Pi** or an assigned remote output to inspect
status, schedule, pending work, and historical reports. Resuming schedules future
eligible slots; it does not replay missed transmissions. Losing contact does not
confirm that a transmitter has stopped. See [Operations](../User_Interface/Operations/index.md)
for selected-output controls and [Setup](../User_Interface/Setup/index.md) for assignments.

## Qualification limits

Software checks cover production network and USB interoperability, configuration
handling, and browser workflows. They do not establish physical USB, target
installation, service behavior, timing, frequency accuracy, spectral performance,
calibrated power, or RF qualification. The 32-output limit is software capacity,
not a qualified physical fleet. Automatic Si5351 correction remains experimental.
I²C LPF output control is not included in this release.
