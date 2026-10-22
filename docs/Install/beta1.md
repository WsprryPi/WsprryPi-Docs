# Install 4.0 Beta 1

To install the current WsprryPi beta, run this command on your Raspberry Pi through SSH or a local console:

```bash
curl -fsSL https://raw.githubusercontent.com/WsprryPi/WsprryPi/refs/heads/devel/scripts/install.sh | sudo REPO_BRANCH=devel bash
```

This selects the `devel` branch. Run the same command again to update to the current beta.

Follow the installer's prompts, including a reboot if requested. When installation finishes, open the web address printed by the installer to configure WsprryPi.

For Raspberry Pi setup and general installation guidance, see [Installing WsprryPi](index.md). For supported hardware and band limits, see the [band qualification table](../About_Wsprry_Pi/index.md#band-qualification) and [RP1 operating limits](../Advanced_Operations/rp1_gpclk.md).

## Report beta problems

If a problem relates to one of the issues listed below, please add your report as a comment on that issue so testing feedback stays together. For any other problem, [open a separate issue](https://github.com/WsprryPi/WsprryPi/issues/new/choose). Describe what you expected, what happened, and how to reproduce it.

Please send a support bundle (debug packet) with every problem report, whether you are commenting on an existing issue or opening a new one. Use the [private support-bundle reporting facility](https://github.com/WsprryPi/WsprryPi/issues/414) described below to send the diagnostic information to the maintainer.

### Send a support bundle

Open **Maintenance → Support Bundle** in the WsprryPi web interface and select **Start support bundle**. Enter the relevant issue number or choose to create a new issue. Follow the steps to review the collected information, encrypt it, and upload it privately. Post the prepared public comment with its case ID in the GitHub issue so the maintainer can connect your report to the packet. See [Create and Share a Support Bundle](../User_Interface/Maintenance/support_bundle.md) for the complete procedure.

### Issues marked Ready for Release

These issues are currently marked **Ready for Release**:

- [#332: Define canonical band correlation and regional WSPR frequency presets](https://github.com/WsprryPi/WsprryPi/issues/332)
- [#346: Add GPIO 26 and GPIO 27 to the UI safe-pin list](https://github.com/WsprryPi/WsprryPi/issues/346)
- [#347: Actively reset/disable Si5351 on startup ?](https://github.com/WsprryPi/WsprryPi/issues/347)
- [#348: Can we allow multiple bands to share a GPIO?](https://github.com/WsprryPi/WsprryPi/issues/348)
- [#349: WebSocket client threads are not reaped after browser disconnects](https://github.com/WsprryPi/WsprryPi/issues/349)
- [#352: Feature: Add UI workflow to create and download a support bundle](https://github.com/WsprryPi/WsprryPi/issues/352)
- [#354: Feature Request: Expand "Spot" Menu Item](https://github.com/WsprryPi/WsprryPi/issues/354)
- [#355: Web log viewer leaves journalctl processes running after navigation](https://github.com/WsprryPi/WsprryPi/issues/355)
- [#361: Add band selector and custom frequency to Test Tone](https://github.com/WsprryPi/WsprryPi/issues/361)
- [#364: Harden update detection contract for non-main branch builds](https://github.com/WsprryPi/WsprryPi/issues/364)
- [#365: Make GPIO4 and GPIO20 conditionally available outside GPIO RF output](https://github.com/WsprryPi/WsprryPi/issues/365)
- [#367: Frequencies and Offsets Not Legible on Mobile](https://github.com/WsprryPi/WsprryPi/issues/367)
- [#368: Crash with Si5351 and 2m band](https://github.com/WsprryPi/WsprryPi/issues/368)
- [#379: Qualify 2m WSPR on GPIO and Si5351 backends](https://github.com/WsprryPi/WsprryPi/issues/379)
- [#382: Si5351 should set (and expose) XTAL loading capacitor](https://github.com/WsprryPi/WsprryPi/issues/382)
- [#383: Apply Calibration.PPM to Si5351 synthesis planning](https://github.com/WsprryPi/WsprryPi/issues/383)
- [#387: Combine system clock frequency estimate and manual residual for GPIO accuracy](https://github.com/WsprryPi/WsprryPi/issues/387)
- [#390: Qualify remaining GPIO and Si5351 band combinations, excluding 70 cm](https://github.com/WsprryPi/WsprryPi/issues/390)
- [#400: Add a hardware-free simulated backend for Debian development and CI](https://github.com/WsprryPi/WsprryPi/issues/400)
- [#401: Add mode-aware band qualification and experimental frequency overrides](https://github.com/WsprryPi/WsprryPi/issues/401)
- [#412: Integrate and release RP1 GPCLK DKMS support](https://github.com/WsprryPi/WsprryPi/issues/412)
- [#414: Add encrypted private support-bundle intake](https://github.com/WsprryPi/WsprryPi/issues/414)
- [#415: Absorb Git submodules into WsprryPi as ordinary tracked components](https://github.com/WsprryPi/WsprryPi/issues/415)
- [#416: Protect privileged controls with directly connected LAN safety](https://github.com/WsprryPi/WsprryPi/issues/416)
- [#422: Add immutable UI manifest, local-modification support, and refresh-safe upgrades](https://github.com/WsprryPi/WsprryPi/issues/422)
- [#426: Research isolated-LAN / offline field operation with Web UI](https://github.com/WsprryPi/WsprryPi/issues/426)
