# Development installation

Use the development channel to install the application and supporting files from `devel`:

```bash
curl -fsSL https://raw.githubusercontent.com/WsprryPi/WsprryPi/refs/heads/devel/scripts/install.sh | sudo env REPO_BRANCH=devel bash
```

`REPO_BRANCH=devel` explicitly selects the source branch for supporting files.
The installer script URL alone does not select that branch.

The installer chooses a published executable matching the selected branch, Raspberry Pi OS, and userspace architecture. Automatic downloads verify supplied checksums, architecture, and runtime-library compatibility. A lookup, download, or validation failure stops installation. If no compatible executable is available, the installer follows its source-build policy. For an explicit asset selection, independently verify the published checksum before installing it. Architecture and runtime checks do not replace checksum verification. Follow any requested reboot and open the printed web address.

Review [hardware and band limits](../About_Wsprry_Pi/index.md#band-qualification) before enabling output.

Current development builds support the **WsprryPico 1.0.0-rc.3** prerelease.
Use the [compatibility and upgrade guidance](pico.md#compatible-software) before
selecting firmware. This development command follows current `devel` supporting
files and its available executable; an older published executable may predate
RC.3 support.
For the matched RC.1 executable, use the [pinned RC.1 installation command](rc1.md).
A source build remains an explicit choice through `--binary-source build`; it
builds current `devel` under the documented build-resource policy. Installation
and firmware programming are separate operator actions.

## Pico USB firmware tools

The installer supplies the Pico USB maintenance tools. Under **Setup → Fleet → Pico firmware over USB**, review the selected image and its source before choosing **Install checked image**. Downloading and checking an image does not program the Pico. See [Pico firmware over USB](../User_Interface/Setup/Transmitter/index.md#install-or-update-pico-firmware-over-usb) for settings retention and recovery.

Pi 5-family GPIO driver preparation and kernel compatibility are separate from the application executable download.

## Startup and recovery after a failed update

On supported Pi 5/CM5 systems, automatic RP1 provider installation is independent
of the selected transmit backend. Selecting Si5351 or WTP keeps RP1 available
for later use; `INSTALL_RP1_GPCLK_DKMS=false` explicitly omits its installation.

RP1 startup recovery applies only when the saved transmit backend is `rp1-gpclk`.
Other backends start without requiring RP1 restoration support in the executable
or consulting RP1 recovery records. RP1 recovery does not change their saved
transmit or boot settings. When RP1 is selected, its recovery safeguards still
apply. See [RP1 installation and ownership](../Advanced_Operations/rp1_gpclk.md#installation-and-ownership).

If an installation step fails after executable replacement, the installer
attempts to restore the previous executable and restart the service if it was
previously running. Supporting files, including the startup hook, remain at the
installed version. The hook accepts a restored non-RP1 executable without RP1
restoration support. An executable used for RP1 still requires that support.

Executable recovery does not reverse package or configuration changes. An older
executable may be unable to read configuration changed during the attempted
update. The installer reports failure even if recovery succeeds. Preserve the
original error, subsequent recovery messages, installer log, and recovery files
when reporting a failed update.

## Testing scope and reports

Software integration and executable checks do not establish physical USB, GPIO, timing, spectral, or RF qualification. Keep transmission disabled during setup and review the selected hardware's operating limits.

Report reproducible problems through [GitHub issues](https://github.com/WsprryPi/WsprryPi/issues/new/choose). Include the installed build identity, selected backend, and relevant device identity. Use [Create and Share a Support Bundle](../User_Interface/Maintenance/support_bundle.md) to share diagnostic information privately.
