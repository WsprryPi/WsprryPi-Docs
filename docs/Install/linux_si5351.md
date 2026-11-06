# Linux USB I2C and Si5351

The Linux Si5351 backend uses `linux-i2c`: the kernel driver registers an I2C
adapter, and WsprryPi accesses its `/dev/i2c-N` node through `i2c-dev`.
For MCP2221A, the path is `MCP2221A → hid-mcp2221 → i2c-dev`.
There is no direct HID transport or automatic backend fallback on Linux.

Physical qualification applies to the tested host, kernel, driver, reference,
and output path. Software tests, enumeration, and register communication alone
do not qualify clock output, frequency accuracy, cancellation, or
disconnected-output safety.
For the native macOS transport, build selection, adapter identity, and setup
limits, use [macOS USB I2C and Si5351](macos_si5351.md).

## Reference hardware

- [Adafruit MCP2221A Breakout — product 4471](https://www.adafruit.com/product/4471).
- [Adafruit Si5351A Clock Generator with STEMMA QT — product 5640](https://www.adafruit.com/product/5640), using its 25 MHz crystal and 7-bit address `0x60`.

Use the boards' documented STEMMA QT wiring or verify power, common ground,
SDA, SCL, voltage levels, and pull-ups explicitly. Do not connect two competing
power supplies. Confirm the fitted crystal and required load setting from the
board's documentation. A different Si5351 board or reference is a different
qualification target.

## Ubuntu prerequisites

Ubuntu 24.04 with GCC 13 is the development target. An Ubuntu VM requires
whole-device USB passthrough, guest driver binding, and verified reconnect
behavior. Containers share their host kernel; a container cannot add a missing
MCP2221 driver to that kernel.

Check `CONFIG_HID_MCP2221`, `hid-mcp2221` binding, `i2c-dev`, device permissions,
and the driver's clock-rate setting on the intended host. WsprryPi does not
configure the MCP2221A clock rate directly. Record the kernel, selected rate,
and verification method when qualifying a setup.

The kernel must enable `CONFIG_HID_MCP2221` as a built-in driver or module.
Some Raspberry Pi OS kernels omit it. Use a kernel with this driver, or a
matching module provided through the host's kernel-maintenance policy, before
expecting the adapter to appear. WsprryPi does not supply a missing kernel
driver.

A strict Si5351 executable can be built without ancillary Pi GPIO:

```sh
sudo apt-get update
sudo apt-get install -y build-essential ca-certificates git libssl-dev \
  libavahi-client-dev libsystemd-dev pkg-config python3
cd WsprryPi/src
make release BACKENDS=si5351 ANCILLARY_GPIO=0 SUDO=
```

The optional `make install-binary BACKENDS=si5351 ANCILLARY_GPIO=0` target
copies only the executable; it does not install the UI, enable services,
configure device permissions, or install kernel drivers. Use an explicitly
chosen installation prefix and privilege policy.

The application user needs read/write permission on the selected I2C node.
Use the host's device-group or narrowly scoped device-rule policy. Avoid
world-writable device nodes. Availability in the selector establishes metadata
presence only; access and `I2C_FUNC_I2C` are checked before slave access.

Physical transmission also requires permission to run the transmitter thread
with `SCHED_FIFO` priority 50. Grant the application user an appropriate
real-time priority limit through the host's service or session policy.
I2C-node access alone does not grant scheduling permission; without it,
transmission fails before waveform generation. The simulated backend does not
require this real-time scheduling permission.

On hosts with the Pico USB updater, use the configured application service
account so its protected maintenance state is readable. An unreadable maintenance
state blocks transmitter controls. Preserve update records and their
permissions.

## Select the adapter

For metadata-only CLI inventory, run `wsprrypi --list-i2c-adapters`; it does not
open an adapter or probe a slave. Copy its exact identity for
`--si5351-adapter-identity <identity>`.

In **Setup → Transmitter hardware**, select **Si5351**, then **I2C adapter**.
A USB entry uses a stable identity and shows its current `/dev/i2c-N` node.
The saved **Adapter Identity** is separate from the legacy **I2C Bus** value;
when identity is set, the numeric value is ignored rather than rewritten.

The identity includes VID/PID and an encoded USB serial when the kernel exposes
one. Duplicate serial matches are rejected. If there is no serial, the identity
uses the full USB sysfs topology path. That identity is tied to this host and
USB port/controller topology; moving the board or changing host topology may
require explicit reselection. A newly exposed serial also requires reselection.
WsprryPi does not rewrite adapter serials or choose the first identical adapter.

Reload after reconnection. A changed bus number can resolve to the same saved
identity. Zero or multiple matches leave the saved selection visible and block
use; select a unique adapter explicitly. Existing generic numeric I2C settings
remain supported, but MCP2221A requires stable identity.

Choose the fitted reference (**25,000,000 Hz**, **Passive crystal** for product
5640), the specified crystal load, the intended transmit clock, and the desired
output drive. Do not substitute defaults for the fitted hardware. The reference
and drive are independent of the WSPR message's reported power.

Choose the board's fitted **I2C Address**. With a stable identity, selecting an
address checks only that address. If a saved address no longer responds, the
control stays editable so you can explicitly select another fitted address.
A failed check does not confirm that the whole address range is empty. Valid
address changes save automatically with the form.

Probing is a
register-pointer write followed by a read, not output programming or definitive
silicon identification. A permission or capability failure is distinct from a
non-responsive slave. Correct the reported condition and explicitly retry.

## Reference calibration

Measure the conducted output against a stable frequency reference before
setting Si5351 calibration. With an SDR, capture a locked reference signal
alongside the Si5351 signal where possible; their separation avoids confusing
receiver tuning error with transmitter error. Record reference lock, receiver
settings, measurement resolution, warm-up, and drift.

The Si5351 calibration value corrects the fitted reference frequency. A positive
PPM value compensates for output below the requested frequency. Verify the
correction at a second frequency before saving it for that board. Keep receiver
correction separate and use the measured value for the actual reference and
setup, rather than copying another board's calibration.

## Conducted measurements and recovery

Before enabling any output, verify the actual wiring and conducted output path,
instrument input limits, coupling, and attenuation for this board. Do not assume
a generic 50-ohm load is suitable for a CMOS clock output. Use no amplifier or
antenna. Define the exact frequency, mode, bounded duration, stop procedure,
and output-disable measurement before starting.

Startup attempts all-output disable before ordinary programming. Cancellation
requests stop and disable cleanup; it does not establish measured RF inactivity.
Removal, NACK, partial transfer, timeout, or identity change fails the operation
without selecting another adapter or bus. Loss of I2C access can leave a powered
Si5351 generating clocks beyond a software duration limit. An adapter reset or
USB disconnect cannot guarantee that a separately powered Si5351 has stopped
generating clocks.
Treat failed cleanup or unknown output state as requiring physical verification
and a known recovery procedure before further operation. Reconnecting does not
authorize automatic resumption.

Kernel I2C calls can block beyond the application's readiness polling intervals.
The isolated address-discovery deadline bounds its reply, not the kernel's
transaction or the time until a detached device ceases output. Qualify latency,
normal stop, interruption, cleanup, and idle cancellation on each actual
host/kernel/reference setup. Keep measurement-reference lock, uncertainty,
frequency, duration, and instrument settings with the resulting evidence.
