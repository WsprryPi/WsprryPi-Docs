# Install 4.0 Beta 7

[WsprryPi 4.0 Beta 7](https://github.com/WsprryPi/WsprryPi/releases/tag/v4.0.0-beta.7) is a testing prerelease. It supports up to **32 independent remote Fleet outputs** alongside the controller's local output and uses the current Pico RC.2 control contract. Review [supported hardware and band limits](../About_Wsprry_Pi/index.md#band-qualification) before operating a transmitter.

## Install or update

Run this command on the Raspberry Pi through SSH or a local console:

```bash
curl -fsSL https://raw.githubusercontent.com/WsprryPi/WsprryPi/refs/heads/devel/scripts/install.sh | sudo REPO_BRANCH=devel bash
```

This selects the current `devel` installer and supporting files. It downloads the newest published executable for `devel` that matches Raspberry Pi OS Bookworm or Trixie and the Pi's 32-bit ARMv6 or 64-bit AArch64 userspace. Published prereleases are eligible. Run the command again to update; later `devel` releases and supporting files can supersede Beta 7.

Automatic downloads verify the supplied checksum, architecture and runtime-library compatibility. A lookup, download or validation failure stops installation. If no compatible release is available, the installer follows its documented source-build policy. Follow its prompts and any requested reboot, then open the printed web address. See [Installing WsprryPi](index.md) for preparation and recovery guidance.

Beta 7's executable reports `4.0.0-beta.7+3db74d7`; the suffix identifies its build source. The [release manifest and checksums](https://github.com/WsprryPi/WsprryPi/releases/tag/v4.0.0-beta.7) identify the four exact executable assets. The normal stable-channel installation commands remain separate.

## Pico USB firmware tools

The installer retains compatible USB-enabled picotool 2.3 or newer within 2.x, or supplies the verified prebuilt picotool 2.3.1 package for the Pi's userspace. Picotool is never compiled on the Pi. The shared Pico maintenance tool is obtained from its independently verified channel when first needed; pending newer Pico CI does not block Pi installation or replace an available compatible verified tool.

In **Setup → Fleet → Pico firmware over USB**, **Specific version** defaults to published Pico `1.0.0-rc.2`. Downloading and checking an image does not program the Pico. Review the reported version and source before explicitly installing it. See [Pico firmware over USB](../User_Interface/Setup/Transmitter/index.md#install-or-update-pico-firmware-over-usb) for saved-settings retention and recovery.

Pi 5-family GPIO installations select published RP1 provider `v1.0.0-rc.2` by default. Driver preparation and kernel compatibility remain separate from the application executable download.

## Testing scope and reports

Software integration and executable checks do not establish installation, physical USB, service lifecycle, GPIO, timing, spectral or RF qualification. A 32-output software capacity is not evidence of a measured 32-transmitter installation. Keep transmission disabled during setup and review the selected hardware's operating limits before enabling it.

Report reproducible problems through [GitHub issues](https://github.com/WsprryPi/WsprryPi/issues/new/choose). Include the installed version, selected backend and relevant device identity. Use [Create and Share a Support Bundle](../User_Interface/Maintenance/support_bundle.md) to send diagnostic information privately.
