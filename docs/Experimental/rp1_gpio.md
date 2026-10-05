---
orphan: true
nosearch: true
---

# Experimental Raspberry Pi 5 RP1 GPIO transmission

This is a historical record of the Issue 399 custom-kernel provider. Its device
names, installation steps, and qualification table do not describe the current
installer-managed integration. For current operation, see
[Raspberry Pi 5 RP1 GPCLK](../Advanced_Operations/rp1_gpclk.md).

This page records an engineering workflow that is deliberately absent from the
normal WsprryPi navigation and installation process. Raspberry Pi 5 RP1 GPIO
transmission is implemented for continued development, but ordinary operators
are not offered this transmitter path. Use the supported Si5351 path unless you
are maintaining the matching kernel, provider, and recovery procedure yourself.

## Scope and prerequisites

The engineering path is limited to the Raspberry Pi OS 64-bit BCM2712-optimized
kernel used by Raspberry Pi 5, Pi 500, and CM5 systems. The kernel image,
provider modules, overlay, userspace UAPI, and running kernel release must be an
exact matching set. A module that merely loads is not proof of compatibility.

The normal WsprryPi installer does not install or select any of these
historical Issue 399 artifacts. Kernel, module, overlay, boot-file, service,
GPIO, and reboot changes require a separately controlled maintenance window
and a known-good boot selection retained for recovery.

## Drive selection

RP1 accepts 2, 4, 8, and 12 mA pad-drive settings. Use 2 mA unless a specific
engineering test requires another value. These values describe the RP1 output
pad configuration; they are not calibrated RF power readings and must not be
reported as transmitter output power.

## Qualification boundary

Implementation, clock-disabled hardware execution, live RF observation, decode
evidence, and general product qualification are separate claims.

| Cell | Current evidence |
|---|---|
| Raspberry Pi 5, GPIO4, 20 m WSPR, 2 mA | Live output and independent decodes on the recorded Issue 399 kernel/provider build |
| Raspberry Pi 5, GPIO4, QRSS, FSKCW, and DFCW, 2 mA | Live keyed intervals and relative SDR behavior on the recorded Issue 399 build |
| 2, 4, 8, and 12 mA selection | Configuration, provider-contract, and clock-disabled runtime evidence |
| GPIO20 | Not qualified |
| Other Raspberry Pi 5-family models | Not qualified |
| Higher-drive live RF behavior | Not qualified |
| Absolute output power or spectral compliance | Not qualified |
| Normal installer deployment | Unavailable |

Evidence applies only to the exact recorded hardware, kernel, provider,
userspace revisions, mode, pin, band, and procedure. It must not be generalized
to another cell without its own evidence.

## Clock-disabled identity check

Before opening the provider, confirm the running and installed identities and
require `live_output=N`:

```sh
uname -r
/sbin/modinfo -F filename rp1_gpclk_provider
/sbin/modinfo -F srcversion rp1_gpclk_provider
/sbin/modinfo -F filename rp1_gpclk_provider_kunit
/sbin/modinfo -F srcversion rp1_gpclk_provider_kunit
cat /sys/module/rp1_gpclk_provider/parameters/live_output
stat /dev/rp1-gpclk0
grep -E '^(auto_initramfs|kernel|dtoverlay=rp1-gpclk-provider)=' \
  /boot/firmware/config.txt
```

Stop if `/dev/rp1-gpclk0` is absent, the provider returns `ENOTTY` or `EPROTO`,
artifact identities differ, or `live_output` is not `N`. Do not silently fall
back to a different transmitter.

## Recovery

### Provider or UAPI failure

Keep transmission disabled. Compare the running kernel release, loaded module
location and source version, installed module hashes, overlay, and userspace
UAPI. Restore the backed-up matching modules or select the retained packaged
kernel, run `depmod` for that exact release, reboot, and repeat the identity
check before further testing.

### Failed module or overlay load

Remove the experimental overlay from the next boot selection or restore the
backed-up boot configuration. Select the known-good packaged kernel rather than
overwriting it. Reboot and verify that the expected kernel and normal WsprryPi
services are active.

### Clock-disabled state

`live_output` is a read-only module-load parameter and defaults to false. Do not
persist `live_output=1` in module configuration. Restore the provider to
`live_output=N` before diagnostic or clock-disabled testing.

### GPIO and service recovery

After any controlled test, verify that the transmit GPIO is an input, GPCLK0
prepare and enable counts are zero, and the WsprryPi service is active. If the
service does not start, keep transmission disabled and review its status and
journal before changing the provider or boot selection again.

Use the Maintenance page to create a support bundle after restoring a safe
state. Include the bundle with the exact kernel release, provider source
version, artifact hashes, selected boot entry, and the failed operation.

## Promotion boundary

This page must remain unlinked while RP1 GPIO is hidden from ordinary
operators. Public promotion requires a supported installation and rollback
workflow, documentation updates, and qualification sufficient for every claim
made on the public compatibility, installation, configuration, and operation
pages.
