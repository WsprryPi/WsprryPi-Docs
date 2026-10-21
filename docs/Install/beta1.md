# Install 4.0 Beta 1

WsprryPi 4.0 Beta 1 is an explicit testing opt-in. The normal installer and
stable update channel continue to select stable software. Use this procedure
after the [Beta release](https://github.com/WsprryPi/WsprryPi/releases/tag/v4.0.0-beta.1)
and its assets are available. A missing download is a reason to stop.

Before upgrading, stop scheduled transmissions and finish interrupted Pico
firmware work. Preserve your configuration, executable, customized web files,
provider recovery inputs and Pico recovery files. An executable-only rollback
does not restore packages, configuration, drivers or firmware.

## Select the complete Beta source and executable

Use a new directory. The tagged checkout supplies the reviewed web interface,
configuration templates, service files and helpers. The
[publication manifest](https://github.com/WsprryPi/WsprryPi/releases/download/v4.0.0-beta.1/publication-manifest.json)
records exact publication/supporting source, executable source and Docs
identities. The executables were built at
`1e047a44a44f07d2eb52dfd3c3537d2d24e60143`; later supporting-source repairs are
included in the publication tag. Do not substitute `main` or moving `devel`.

Select by Debian **userspace architecture** and OS codename, rather than kernel
bitness:

| `dpkg --print-architecture` | OS | Asset |
| --- | --- | --- |
| `armhf` | Bookworm | `wsprrypi-armv6-bookworm` |
| `armhf` | Trixie | `wsprrypi-armv6-trixie` |
| `arm64` | Bookworm | `wsprrypi-aarch64-bookworm` |
| `arm64` | Trixie | `wsprrypi-aarch64-trixie` |

ARMv6 hard-float builds also serve supported newer 32-bit Pis. These are
dynamically linked executables; matching runtime libraries are required.

## Install the checked packet

The procedure requires Git, curl and the standard Debian checksum tools. It
stops on a failed clone/download, an existing checkout directory, dirty or
mismatched source, or a failed checksum. Run the complete block in a shell on
the intended Pi after preparing your recovery set:

```bash
bash <<'BETA_INSTALL'
set -euo pipefail
release_tag=v4.0.0-beta.1
checkout="$HOME/WsprryPi-beta1"
test ! -e "$checkout"
git clone --branch "$release_tag" --single-branch \
  https://github.com/WsprryPi/WsprryPi.git "$checkout"
cd "$checkout"
actual_head=$(git rev-parse HEAD)
tagged_head=$(git rev-parse "refs/tags/$release_tag^{commit}")
source_status=$(git status --porcelain)
[[ "$actual_head" =~ ^[0-9a-f]{40}$ ]]
test "$actual_head" = "$tagged_head"
test -z "$source_status"

case "$(dpkg --print-architecture)" in
  armhf) cpu=armv6 ;;
  arm64) cpu=aarch64 ;;
  *) echo "Unsupported userspace architecture"; exit 1 ;;
esac
. /etc/os-release
case "$VERSION_CODENAME" in
  bookworm|trixie) ;;
  *) echo "Unsupported OS release"; exit 1 ;;
esac
asset="wsprrypi-$cpu-$VERSION_CODENAME"
downloads=$(mktemp -d "$HOME/wsprrypi-beta1-downloads.XXXXXX")
base="https://github.com/WsprryPi/WsprryPi/releases/download/$release_tag"
curl --fail --location "$base/$asset" --output "$downloads/$asset"
curl --fail --location "$base/SHA256SUMS" --output "$downloads/SHA256SUMS"
(cd "$downloads" && grep "  ${asset}$" SHA256SUMS | sha256sum --check --strict)

rm -f ~/finished
sudo ./scripts/install.sh --binary-source local \
  --binary-path "$downloads/$asset" && touch ~/finished
BETA_INSTALL
```

The checksum must report `OK`. It checks agreement with the declared release
packet, rather than authenticating the publisher by itself. Keep the downloads
and recovery copies until installation and idle readiness have been checked.
If an interrupted attempt leaves the checkout directory, inspect it before
retrying; this procedure deliberately refuses to reuse it silently.

The installer installs runtime packages, including Avahi libraries for discovery,
and web dependencies, while skipping application compilation. Pi 5 GPIO support
has separate kernel-header, compiler and DKMS requirements. Pico USB maintenance
requires Python and a separately installed picotool. On failure the installer
attempts executable/service restoration; this is not a complete package or
configuration rollback.

The alternative installer options `--binary-source release --release-tag v4.0.0-beta.1`
select and download an executable for the host. `--release-tag` selects only the
executable; the current checkout selects supporting files. The helper does not
perform the independent checksum comparison in the procedure above.

## Beta acceptance limits

The four builds passed software and build-environment checks. Bounded wspr5
runtime acceptance used the AArch64 Trixie executable, with explicit reuse of
unchanged installer/UI evidence. The later bundled-RP1 helper and Pico installer
distribution changes have isolated installation, status, recovery and CI
coverage; fresh target installation/status of those changed support files was
not performed and is an explicitly accepted Beta limitation.

Fresh clean installation, physical acceptance of the other three exports,
reboot, fresh GPIO4 selection and rollback rehearsal remain unperformed Beta
checks. These results do not establish timing, electrical or RF qualification.
Consult the [band qualification table](../About_Wsprry_Pi/index.md#band-qualification)
and the [RP1 operating limits](../Advanced_Operations/rp1_gpclk.md).
