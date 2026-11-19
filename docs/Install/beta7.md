# Development installation

Use the development channel to install the application and supporting files from `devel`:

```bash
curl -fsSL https://raw.githubusercontent.com/WsprryPi/WsprryPi/refs/heads/devel/scripts/install.sh | sudo env BRANCH=devel bash
```

The installer chooses a published executable matching the selected branch, Raspberry Pi OS, and userspace architecture. Automatic downloads verify supplied checksums, architecture, and runtime-library compatibility. A lookup, download, or validation failure stops installation. If no compatible executable is available, the installer follows its source-build policy. For an explicit asset selection, independently verify the published checksum before installing it. Architecture and runtime checks do not replace checksum verification. Follow any requested reboot and open the printed web address.

Review [hardware and band limits](../About_Wsprry_Pi/index.md#band-qualification) before enabling output.

Development source uses one coordinated Pi/Pico control schema. A previously
published Pico release is not automatically compatible with a later development
schema. Use the [compatibility and upgrade guidance](pico.md#compatible-software)
for the selected source pair. Complete legacy retirement with matching
WTP-capable software before replacement. This development command follows
`devel` supporting files and its available executable. A published executable
can predate the current control schema; confirm the matched sources before use.
For the matched RC.1 executable, use the [pinned RC.1 installation command](rc1.md).
A source build remains an explicit choice through `--binary-source build`; it
builds current `devel` under the documented build-resource policy. Installation
and firmware programming are separate operator actions.

## Pico USB firmware tools

The installer supplies the independent Pico USB maintenance tools. The former
selected-output browser firmware panel is unavailable in retirement software.
Use the [standalone Pico installation workflow](https://wsprrypico.readthedocs.io/en/devel/install.html)
with its exclusive-access and recovery procedure. Firmware programming remains
a separate deliberate action. See [Pico firmware over USB](../User_Interface/Setup/Transmitter/index.md#install-or-update-pico-firmware-over-usb).


Pi 5-family GPIO driver preparation and kernel compatibility are separate from the application executable download.

## Testing scope and reports

Software integration and executable checks do not establish physical USB, GPIO, timing, spectral, or RF qualification. Keep transmission disabled during setup and review the selected hardware's operating limits.

Report reproducible problems through [GitHub issues](https://github.com/WsprryPi/WsprryPi/issues/new/choose). Include the installed build identity, selected backend, and relevant device identity. Use [Create and Share a Support Bundle](../User_Interface/Maintenance/support_bundle.md) to share diagnostic information privately.
