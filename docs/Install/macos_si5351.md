# macOS USB I2C and Si5351

On macOS, WsprryPi uses the native `mcp2221a-hid` transport to access an MCP2221A
USB-to-I2C adapter. The adapter connects to the existing Si5351 output backend;
mode selection, frequency planning, output gating, cancellation, and cleanup
remain Si5351 operations.

Transport selection is explicit. macOS does not provide Linux `i2c-dev` or a
`/dev/i2c-N` device, and WsprryPi does not switch automatically to another
adapter, bus, transport, or output backend.

Native macOS physical qualification remains incomplete. A successful build,
adapter listing, or register read does not establish output-disable behavior,
timing, frequency accuracy, or RF performance. Use the hardware and recovery
checks below before considering physical operation.

## Reference hardware

- [Adafruit MCP2221A Breakout — product 4471](https://www.adafruit.com/product/4471).
- [Adafruit Si5351A Clock Generator with STEMMA QT — product 5640](https://www.adafruit.com/product/5640), using its 25 MHz crystal and 7-bit address `0x60`.

Use the boards' documented STEMMA QT connection, or verify power, common ground,
SDA, SCL, voltage levels, and pull-ups explicitly. Do not connect competing power
supplies. Confirm the crystal's required load capacitance from the board's
specification. Other boards, references, and adapters require their own
qualification.

## Build from source

The source-build target is macOS 14 or later with Apple Clang and C++20 support.
Build for the Mac's architecture, with a matching OpenSSL installation; Apple
Silicon and Intel builds are separate. Executable deployment requirements also
depend on the selected SDK and OpenSSL build. A universal executable, signed
installer, and macOS service installation are not supplied.

Install Apple's Xcode command-line tools if they are not already present:

```sh
xcode-select --install
```

With [Homebrew](https://brew.sh/) installed, prepare the build dependencies:

```sh
brew install pkg-config openssl@4
export PKG_CONFIG_PATH="$(brew --prefix openssl@4)/lib/pkgconfig${PKG_CONFIG_PATH:+:$PKG_CONFIG_PATH}"
```

From the `src` directory of a WsprryPi source checkout, build the Si5351 profile
without Raspberry Pi GPIO support:

```sh
cd WsprryPi/src
make release \
  BACKENDS=si5351 ANCILLARY_GPIO=0 \
  SI5351_TRANSPORT=mcp2221a-hid SUDO=
```

The executable is `build/bin/wsprrypi`. The native transport uses the IOKit and
CoreFoundation frameworks supplied with macOS. It requires no HIDAPI library,
Linux I2C driver, or USB kernel extension. Linux `linux-i2c` builds and native
macOS builds have separate transport selections and build outputs.

Keep the executable in the build directory while preparing the configuration.
The Raspberry Pi installation script, Apache setup, service commands, GPIO
controls, and Linux device-permission instructions are not macOS setup steps.

## Identify the adapter

From the same `src` directory, these commands report the compiled transport and
read USB registry metadata:

```sh
./build/bin/wsprrypi --si5351-transport
./build/bin/wsprrypi --list-i2c-adapters
```

The first command should report `mcp2221a-hid`. It identifies the compiled
transport, not a working physical output. The adapter listing does not open a
HID session, probe the Si5351, or program output. Review any **Discovery Error**
or **Selection Error** before using an entry.

Copy the exact **Identity** string. A USB serial, when exposed, is used with the
adapter's vendor and product identifiers. Duplicate matches are refused. An
adapter without a serial uses a macOS USB location identity tied to this host,
controller, and physical port. Moving the adapter, changing a dock or
controller, or exposing a serial later can require explicit reselection.
A Linux sysfs topology identity is not a macOS location identity.

Do not shorten, decode, or manufacture an identity, select the first matching
adapter, or rewrite its USB serial to get past an error. Zero or multiple
matches leave the adapter unavailable. A reconnect invalidates the old live
session even when the selected identity can resolve again.

## Prepare the configuration

Native Si5351 setup uses CLI or INI configuration. The web adapter selector and
cached native status workflow are not supported. Do not use browser Reboot or
Shutdown controls on macOS. Machine reboot and power-off are not supported.

Select `si5351` as the **Transmit Backend**, and enter the exact adapter identity.
The retained **I2C Bus** setting is a Linux setting; it does not select a device
on macOS and is not rewritten by native identity selection.

The following is a fragment for an existing INI file, not a complete station
configuration. Replace `<Identity>` with the exact inventory value.
Keep the remaining station, scheduling, and hardware settings under review.

```ini
[Operation]
Transmit = False
Transmit Backend = si5351
Enable on Boot = Never

[Si5351]
Adapter Identity = <Identity>
I2C Address = 0x60
Reference Frequency = 25000000
Reference Source = crystal
```

Set **Crystal Load Capacitance** to the board's specified value: accepted values
are 6, 8, or 10 pF. Choose the intended **TX Output** (`CLK0`, `CLK1`, or `CLK2`)
and **Power Level** (1 through 4). The drive levels correspond to 2, 4, 6, and
8 mA, independently of the WSPR message's reported transmit power. Do not copy
another board's reference, load, drive, or calibration values.

Equivalent CLI options are `--backend si5351`,
`--si5351-adapter-identity`, `--si5351-i2c-address`,
`--si5351-reference-frequency`, `--si5351-reference-source`,
`--si5351-crystal-load-capacitance`, `--si5351-tx-output`, and
`--si5351-power-level`. Use `--no-web` for CLI-only operation. The
`--ini-file` option loads and monitors an INI file.

Loading an operating configuration can open the adapter, probe the configured
address, and attempt startup output disable, even while transmission is off.
Only the explicitly selected address is checked; discovery does not scan other
adapters or substitute another address. Complete the physical setup review
before starting the application with that configuration.

## Access errors and recovery

Run under the intended macOS user account. If HID access is denied or busy,
review the reported macOS permissions, check whether another application owns
the adapter, and confirm the exact identity and connection. Linux I2C groups,
`udev` rules, and world-writable device nodes do not apply. Do not change device
identity or weaken access controls to bypass an error.

The native transport sets the I2C rate to approximately 100 kHz. NACK, short or
partial transfers, timeout, disconnect, and changed identity fail the operation.
A failed configuration write is not replayed. A faulted session does not reopen
or resume automatically; correct the cause and make a deliberate new start.

Do not cancel or reset an idle adapter as a setup step. Cancellation of an
active transfer must establish the resulting engine state; an acknowledgment
alone is not successful recovery. A reported STOP timeout, including `0x62`,
requires investigation rather than repeated cancellation attempts.

## Physical checks and output limits

Before enabling output, verify the conducted output path, instrument input
limits, coupling, attenuation, and a stopping procedure for the actual boards.
Do not assume a generic 50-ohm load is suitable for a CMOS clock output. Initial
qualification uses no antenna or amplifier. Define the exact frequency, mode,
bounded duration, and output-disable measurement before starting.

Startup attempts all-output disable before ordinary programming. Stopping a job
requests output-disable cleanup, but adapter cancellation is not synthesizer
output inhibition. USB removal or an adapter reset cannot prove that a
separately powered Si5351 has stopped generating clocks. A software duration
limit cannot guarantee when inaccessible hardware will cease output.

If cleanup fails or output state is unconfirmed, physically verify the output
and use the setup's established recovery procedure before further operation.
Reconnecting is not authorization to resume. Application deadlines and macOS
scheduling are not hard-real-time output-disable guarantees.

Qualify discovery and identity, configuration writes, startup inhibition,
normal stop, cancellation, denial, NACK, timeout, disconnect, and interruption
on the actual Mac, adapter, and synthesizer. Measure conducted output and
frequency accuracy separately. The [reference calibration guidance](linux_si5351.md#reference-calibration)
describes measurement-reference lock, receiver error, warm-up, uncertainty, and
verification at a second frequency; it does not extend Linux qualification to
macOS. A 25 MHz reference is not qualified for 2 m WSPR. See the
[band qualification table](../About_Wsprry_Pi/index.md#band-qualification) for
host, reference, and band limits.
