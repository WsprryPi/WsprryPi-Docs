# Installing WsprryPi

## Gather Hardware

You will need the following:

- A Raspberry Pi
- An SD card for the OS image
- A power supply for the Pi.  Pay attention to potentially noisy power supplies here.  You will benefit from a well-regulated supply with sufficient ripple suppression.  You may see supply ripple as mixing products centered around the transmit carrier, typically at 120Hz (60Hz mains frequency) and 100Hz (50Hz mains frequency).

To use a Pico 2 W as an external output, follow [Add a WsprryPico](pico.md).
It covers connection and Fleet setup on an installed Pi and links to the
Pico's firmware and hardware instructions.

If you choose the Si5351 backend, you will additionally need an Si5351 clock
generator. While I have provided a KiCad design for a Pi HAT with a
purpose-built circuit surrounding the Si5351, you may also use one of the
common breakout boards:

- [Adafruit Si5351 Clock Generator Breakout](https://learn.adafruit.com/adafruit-si5351-clock-generator-breakout/overview) - This board uses a 25 MHz crystal. WsprryPi has not qualified a 25 MHz reference for 2 m WSPR.
- [QRP Labs Si5351A Synthesizer](https://www.qrp-labs.com/synth.html) - This kit is supplied with a 27 MHz crystal and supports optional TCXO configurations. WsprryPi's qualified 2 m configuration uses a 27 MHz reference.

The Si5351 is controlled through the Pi's [I2C bus](https://pinout.xyz/pinout/i2c), requiring a connection to GPIO2 and GPIO3 for this communication.

## Prerequisites

This section may be the most challenging part of the whole installation.  *You must have a working Raspberry Pi with Internet access.* It can be hard-wired or on Wi-Fi.  There is no better place to learn how to set up your new Pi than from the people who make it themselves.  [Go here](https://www.raspberrypi.com/documentation/computers/getting-started.html), and learn how to install the operating system with the [Raspberry Pi Imager](https://www.raspberrypi.com/software/).  To enable SSH access, pre-configure your image with your local/time zone, Wi-Fi credentials, and a unique hostname.

![Raspberry Pi Imager](Raspberry_Pi_Imager.png)

I am only testing the current [`stable` versions](https://www.debian.org/releases/stable/).  Testing everything on more than one release, 32 and 64-bit, and now GPIO and Si5153, with WSPR 1, 2 and 3, plus three CW modes, takes more time than I have right now.  In theory it will compile and run on [`oldstable`](https://www.debian.org/releases/oldstable/) but I won't support issues there.

You can use a full-featured desktop version with all the bells and whistles, or WsprryPi will run just fine on the Lite version on an SD card as small as 2 GB (although a minimum of 8 GB seems more comfortable these days).  You can even run it headless without a keyboard, mouse, or monitor.  If you enable SSH, you can use your command line from Windows 10/11, macOS, or another Pi.

Whatever you do, you will need command-line access to your Pi to proceed via SSH or the console.  Once you are up and running and connected to the Internet, you may proceed with WsprryPi installation.  Each time I update this documentation, the Raspberry Pi Imager has changed the workflow.  Use Internet resources to find your best path.  You will only need command line (SSH) access to the Pi, but you are welcome to use any other configuration.

## System Changes

Aside from the obvious, installing WsprryPi, the install script will do the following:

- **Install Apache2**, a popular open-source, cross-platform web server that is the most popular web server by the numbers.  The [Apache Software Foundation](https://www.apache.org/) maintains Apache.  Apache is used to control WsprryPi from an easy-to-use web page.  Additionally, if you have not previously used the Apache installation, a redirect from the root of the web server to `/wsprrypi/` will be created for ease of use.  Finally, the script creates proxy mappings and a managed access policy for communication between the web page and application:
  - `http://127.0.0.1:31415/config` to `/wsprrypi/config` for getting/setting the configuration
  - `http://127.0.0.1:31415/version` to `/wsprrypi/version` to retrieve the running version.
  - `ws://127.0.0.1:31416/socket` to `/wsprrypi/socket` for Web Socket communications.
  - A managed privileged-network-safety policy that restricts protected HTTP
    operations and the entire browser-facing WebSocket endpoint to directly
    connected Ethernet/Wi-Fi networks by default. The installer validates the
    complete Apache configuration before reloading it.
- **Install Chrony**, [a replacement for ntpd](https://chrony-project.org/).
- **Install PHP**, a popular, general-purpose scripting language that is especially suited for web development.  The [PHP Group](https://www.php.net/) maintains PHP.  I wrote the web pages in PHP.
- **Install Raspberry Pi development libraries and other Packages**, `git`, and `libgpiod`.
- **Compile and configure WsprryPi**
- **Install and validate RP1 GPIO support on Raspberry Pi 5-family systems.**
  The installer resolves a compatible RP1-GPCLK-DKMS provider, verifies its
  source and installed artifacts, and first establishes route-neutral
  administration. Fresh setup has no selected route. An explicitly saved RP1
  GPIO4/GPIO20 selection can then be restored, with transmission disabled.
  Package installation, neutral activation and route restoration are separate;
  none grants output authorization.
- **Disable the Raspberry Pi's built-in sound card.** WsprryPi uses the RPi PWM peripheral to time the frequency transitions of the output clock.  The Pi's sound system also utilizes this peripheral; any sound events during a WSPR transmission will interfere with the WSPR transmission.

(install-wspr)=
## Install WsprryPi

You may use this command to install WsprryPi (one line):

```bash
curl -fsSL installwspr.aa0nt.net | sudo bash
```

This shorter URL relies on my hosted DNS for a redirect to GitHub.  If my DNS is broken for some reason, you may see an error like this:

`curl: (22) The requested URL returned error: 404`

If that happens, this longer form should work:

```bash
curl -fsSL https://raw.githubusercontent.com/WsprryPi/WsprryPi/refs/heads/main/scripts/install.sh | sudo bash
```

This install command is idempotent; running it again updates the application
without requiring you to remove an exact installer-owned RP1 provider first.
On Pi 5-family systems, the installer safely returns any exact owned route to a
neutral, inhibited state before replacing provider or application files. It
refuses foreign, modified, mixed, or otherwise unproven provider state instead
of adopting or removing it. If an update is released, re-run the installer to
take advantage of the new release.

The published RP1 provider is v1.0.0 / Debian 1.0.0-1; development source
selection remains separate. Qualification supplement `qualification-v1.0.0-r1`
has its own pinned reference/cache and cannot authorize transmission. If an
application update deliberately skips provider installation, use the
[explicit evidence refresh](../Advanced_Operations/rp1_gpclk.md#qualification-cache-and-installed-commands)
and inspect its result separately from installer success. Do not treat a missing
or invalid evidence cache as a new band-unavailability result.

### Upgrading a customized web interface

Every installed web interface includes an immutable manifest describing the UI files supplied by that installation. Before replacing the web interface, the installer classifies the existing files:

- `packaged`: all covered files match the prior packaged manifest.
- `locally_modified`: a valid prior manifest exists, but covered files were modified, added, or deleted.
- `unknown`: the prior installation cannot be compared safely, for example because its manifest is missing, malformed, unreadable, or unsupported.

For a `locally_modified` installation, the installer creates a unique verified backup under `/var/backups/wsprrypi/ui` before changing the live web files. The backup preserves modified and added files and the prior manifest. A machine-readable `modification-report.json` records modified, added, and missing paths. Missing files have no bytes to copy, so the report is their recovery record.

For an `unknown` installation, the installer backs up the complete covered UI tree before replacement. Runtime and installer-backup directories are excluded from UI identity and are not folded into this covered-tree backup.

The installer verifies the backup before replacing the live UI. If backup creation or verification fails, replacement does not begin. After a successful backup, the installer installs the complete new packaged UI; it does not merge customizations into new files. Recover any desired customization manually by comparing the reported backup with the new installation.

The installer stays quiet when the existing UI matches the packaged files and no backup is needed. If it finds local modifications, the final output shows a short **Customized UI backed up** notice with change counts, the backup directory, and the detailed modification report. An `unknown` installation instead shows **Existing UI backed up**, because the installer preserved the prior files but could not prove whether they were customized. Keep the reported locations until you have reviewed or recovered the files. A UI publication error is always reported, even when no backup was created.

To refuse replacement when the existing UI is `locally_modified` or `unknown`, pass:

```bash
sudo ./scripts/install.sh \
  --fail-on-ui-modifications
```

This option leaves the existing UI in place instead of creating a replacement backup and publishing the new UI. Resolve or preserve the reported installation state, then run the installer again without the option when ready to replace it.

Since the installation script compiles the application on your Pi to avoid any version errors, it will take some time on older Pis with fewer resources.  A Pi 3 with 1 GB of memory takes about 20 minutes.  If the script detects a system with fewer resources, it will intentionally use fewer resources, resulting in a slower installation time.  If that is the case, it will issue a warning:

```text
[WARN ] The compilation step may take from 10m (Pi 3) to up to 50m (Pi 1)
```

The installer reports progress for each operation. The following excerpt shows
executable replacement during an update; other installation steps are omitted:

```text
[  ✔  ] Complete: Stage executable for /usr/local/bin/wsprrypi.
[  ✔  ] Complete: Back up existing executable at /usr/local/bin/wsprrypi.
[  ✔  ] Complete: Stop wsprrypi.service.
[  ✔  ] Complete: Install executable at /usr/local/bin/wsprrypi.
```

The backup message appears only when an executable already exists at the
destination. The service-stop message appears only when the service is running.
Other messages vary with your Pi, installed packages, and installation options.
Each `Complete:` message confirms that operation succeeded; executable
replacement alone does not mean the entire installation has finished. If an
operation fails, the installer reports `Failed:` for that operation.

You may see:

```text
*Important Note:*

WsprryPi uses the same hardware as the sound system to generate
radio frequencies.  This soundcard has been disabled.  You must
reboot the Pi with the following command after install for this
to take effect:

'sudo reboot'

Press any key to continue.
```

The installation will finish with:

```text
Installation successful: WsprryPi.

To configure WsprryPi, open the following URL in your browser:

 http://wspr3.local/wsprrypi/
 http://10.0.0.52/wsprrypi/

If the hostname URL does not work, try using the IP address.
Ensure your device is on the same network and that mDNS is
supported by your system.
```

If the script prompts you to reboot, do that now.  At this point (and if you rebooted if prompted), WsprryPi is installed and running.

Note the URL for the configuration UI, listed as `{name}.local`, and the IP address choice.  You can access your system using the `{name}.local` name without needing to remember the IP address.  The `{name}.local` is convenient for automatically assigned IP addresses in most home networks.  The IP address of your Raspberry Pi may change over time, but its name will remain the same.

Some Windows systems can use this naming standard without additional work, but others may need to install Apple's [Bonjour Print Services](https://support.apple.com/kb/dl999) to enable this helpful tool.  If you encounter a 'host not found' error, try installing Bonjour.

Connect to your new web page from your favorite computer or cell phone using the IP address or the `{name}.local` name, and you can begin setting things up.  See Operations for more information.

## Uninstall WsprryPi

Run the normal installer in uninstall mode:

```bash
curl -fsSL installwspr.aa0nt.net | sudo env ACTION=uninstall bash
```

Uninstall removes the WsprryPi application, service, configuration, and web
files while retaining shared operating-system packages. On Pi 5-family
systems, it also removes the RP1 provider and runtime administration when the
installer can prove that the installed identity is still the one WsprryPi
owns. Foreign, modified, mixed, or unproven provider state is preserved, and
the uninstall reports a failure instead of deleting it.

## Additional Hardware

While the TAPR Hat is optional, an antenna is not. Choosing an antenna is beyond the scope of this documentation. The direct GPIO backend can use GPIO4 (header pin 7) or GPIO20 (header pin 38), but its square-wave output requires the filtering, DC blocking, and protection described in the [RF and Electrical Reference](../Advanced_Operations/rf_electrical.md). Do not connect an antenna directly to an unfiltered GPIO pin.

On Raspberry Pi 5-family systems, the WsprryPi installer installs and validates
the compatible [RP1 GPCLK provider](../Advanced_Operations/rp1_gpclk.md) and
route-management service. Fresh installation leaves both GPIO routes unselected and output disabled;
an update may restore an explicitly saved `rp1-gpclk` route while staying idle.
For a new selection, choose and apply GPIO4 or GPIO20 from **Setup > Transmitter**
after installation. A route change
is complete only after WsprryPi confirms the same requested, persisted,
configured, and active route after startup. You may instead use Si5351 without
selecting an RP1 route.
