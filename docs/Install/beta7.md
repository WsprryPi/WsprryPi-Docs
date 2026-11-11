# Development installation

Use the development channel to install the application and supporting files from `devel`:

```bash
curl -fsSL https://raw.githubusercontent.com/WsprryPi/WsprryPi/refs/heads/devel/scripts/install.sh | sudo env BRANCH=devel bash
```

The installer chooses a published executable matching the selected branch, Raspberry Pi OS, and userspace architecture. Automatic downloads verify supplied checksums, architecture, and runtime-library compatibility. A lookup, download, or validation failure stops installation. If no compatible executable is available, the installer follows its source-build policy. For an explicit asset selection, independently verify the published checksum before installing it. Architecture and runtime checks do not replace checksum verification. Follow any requested reboot and open the printed web address.

Review [hardware and band limits](../About_Wsprry_Pi/index.md#band-qualification) before enabling output.

## Pico USB firmware tools

The installer supplies the Pico USB maintenance tools. Under **Setup → Fleet → Pico firmware over USB**, review the selected image and its source before choosing **Install checked image**. Downloading and checking an image does not program the Pico. See [Pico firmware over USB](../User_Interface/Setup/Transmitter/index.md#install-or-update-pico-firmware-over-usb) for settings retention and recovery.

Pi 5-family GPIO driver preparation and kernel compatibility are separate from the application executable download.

## Testing scope and reports

Software integration and executable checks do not establish physical USB, GPIO, timing, spectral, or RF qualification. Keep transmission disabled during setup and review the selected hardware's operating limits.

Report reproducible problems through [GitHub issues](https://github.com/WsprryPi/WsprryPi/issues/new/choose). Include the installed build identity, selected backend, and relevant device identity. Use [Create and Share a Support Bundle](../User_Interface/Maintenance/support_bundle.md) to share diagnostic information privately.
