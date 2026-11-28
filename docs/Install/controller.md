# Install a Controller-Only Host

A controller-only host runs the WsprryPi dashboard and manages other transmitters. Each managed Pi or Pico owns its settings, schedules, and output. The controller needs no station settings or connected RF hardware.

## Select a bundle

The native installer and service lifecycle were tested on these host profiles:

- **Ubuntu 26.04 arm64.** Install Apache 2 with `libapache2-mod-php8.5`, Python 3, systemd, udev, binutils, and the runtime libraries reported by the installer dry run. Apache must run as `www-data` with `proxy`, `proxy_http`, `proxy_wstunnel`, `headers`, `alias`, `dir`, and `php8.5` enabled.
- **macOS 27 on Apple silicon.** Install the Apple Command Line Tools for `/usr/bin/python3`. The bundle supplies the Apache, PHP, and Python runtime used by the installed services.
- **Windows 11 x64 build 26300.** Use 64-bit Windows PowerShell 5.1, an absolute path to a trusted Python 3.12 or later executable for bundle verification, and the x64 Microsoft Visual C++ Redistributable 14.52.37029 or later. The bundle supplies Apache, PHP, and the installed Python runtime. Run the trusted local installer under your organization’s PowerShell execution policy.

Use the controller archive for your platform, its expected SHA-256 from the bundle provider, and the matching WsprryPi source checkout. Run the commands from that checkout. The regular [Raspberry Pi installer](index.md) and its release executables are for the transmitter role. The controller installer refuses to adopt an existing transmitter installation.

The native tests cover controller services and management software. Network and USB software peers exercise the supported Pi and Pico management workflows. Physical USB devices, host drivers, and RF paths require separate qualification.

## Verify and install

### Ubuntu and macOS

Replace the example bundle path and `SHA256` with the actual archive path and its expected digest. Verify without elevation, then run the install command with administrator privileges.

```bash
bundle='/path/controller.tar'
digest=SHA256

bash scripts/install.sh \
  --controller-only install \
  --dry-run --bundle "$bundle" \
  --sha256 "$digest"

sudo ./scripts/install.sh \
  --controller-only install \
  --bundle "$bundle" \
  --sha256 "$digest"
```

### Windows

In 64-bit Windows PowerShell, enter the checkout’s `scripts` directory and set the actual local archive, digest, and absolute Python path. Run the dry run without elevation. Run the install from the same directory in an administrator session with the same values.

```powershell
Set-Location scripts
$options = @{
  Bundle = 'C:\controller.tar'
  Sha256 = 'SHA256'
  Python = 'C:\path\python.exe'
}

.\controller_windows.ps1 `
  install @options -DryRun

.\controller_windows.ps1 `
  install @options
```

## Open the dashboard and connect a device

Open `http://HOST/wsprrypi/` on Ubuntu with Apache’s default HTTP port. On macOS and Windows, use `http://HOST:8080/wsprrypi/`. Replace `HOST` with the controller’s hostname or IP address. Use the same dashboard URL for management and keep the service on its intended local network.

**Operation** identifies the host as **Controller (no local output)**. An empty device list is normal on first start. For a Pi, use [Maintenance → Controller access](../User_Interface/Maintenance/index.md#controller-access). Supported Picos attached to a paired Pi appear through that connection. Use [Setup → Fleet](../User_Interface/Setup/index.md#pi-and-pico-fleet-setup) for directly managed Pico profiles. Confirm the device identity in **Device** before reading or changing its settings. Closing the controller’s browser or restarting the controller leaves device-owned schedules under the target’s authority.

## Local command and service paths

Keep the installer-managed ownership and permissions on private settings, credentials, and recovery data. Use [Saved Settings and Local Maintenance](../Command_Line_Operations/saved_settings.md) with the installed executable below. Quote executable paths that contain spaces. Run local administrative commands with `sudo` on Ubuntu or macOS, or use PowerShell’s `&` operator in an administrator session on Windows.

### Ubuntu

- Executable: `/usr/local/bin/wsprrypi`.
- Private state: `/var/lib/wsprrypi/application-state` and `/var/lib/wsprrypi-maintenance`.
- Check the backend, browser, maintenance, and Apache services with `systemctl status` and `journalctl -u`.

```bash
systemctl status \
  wsprrypi.service \
  wsprrypi-web.service \
  wsprrypi-maintenance.service \
  apache2.service
```

### macOS

- Executable: `/Library/Application Support/WsprryPi/Program/bin/wsprrypi`.
- Private state: `Controller/application-state` and `Maintenance` under `/Library/Application Support/WsprryPi`.
- Inspect `system/org.wsprrypi.controller` with `sudo launchctl print`. Append `.web`, `.maintenance`, or `.http` to inspect the other jobs. Read service logs under `/Library/Logs/WsprryPi`.

### Windows

- Executable: `%ProgramFiles%\WsprryPi\bin\wsprrypi.exe`.
- Private state: `Controller\application-state` and `Maintenance` under `%ProgramData%\WsprryPi`.
- Run `Get-Service WsprryPi*` to inspect the four services. Apache’s startup log is `Http\startup.log` under `%ProgramData%\WsprryPi`.

## Update, roll back, or uninstall

Before updating, use [Backup and restore](../User_Interface/Maintenance/backup_restore.md) to download an encrypted controller backup. Retain the current archive and its SHA-256 separately. Repeat the install procedure with the replacement archive and digest. Verify that the dashboard opens and that the expected controller and device identities appear.

If activation fails, preserve the installer output and state. Reapply the retained archive and its own digest for an explicit rollback. The installer checks the existing role and saved state before starting the retained executable. If it refuses admission, preserve the state and resolve the reported problem before trying again.

Run the uninstall from the matching checkout as an administrator. On Windows, run it from the checkout’s `scripts` directory. Retained private state, the service identities, and protected release files remain available for reinstall or recovery.

```bash
sudo ./scripts/install.sh \
  --controller-only uninstall
```

```powershell
.\controller_windows.ps1 `
  uninstall
```
