# WsprryPi Documentation

The documents are written in Markdown with Sphinx and hosted on Read the Docs (RTD) and accessible via [wsprdocs.aa0nt.net](http://wsprdocs.aa0nt.net/).

## RTD Documentation Labels

Three labels are maintained and automatically built by RTD:

- `stable`: Built from the latest released version
- `latest`: Built from the default branch (`main`), but not guaranteed to be a release and can be ahead of `stable`.
- `devel`: Build from the devel branch, and generally considered in development along side it's corresponding code.

## Legacy `/en/` URL compatibility

Read the Docs serves this project at `/<version>/<page>`. Preserve the following project-level rules in [Settings → Redirects](https://app.readthedocs.org/dashboard/wsprry-pi/redirects/) so existing English documentation links continue to work:

| Type | From URL | To URL |
| --- | --- | --- |
| Exact Redirect | `/en` | `https://wsprry-pi.readthedocs.io/` |
| Exact Redirect | `/en/*` | `https://wsprry-pi.readthedocs.io/:splat` |

Both rules must be enabled, use **302 — Temporary Redirect**, and have **Force redirect** disabled. Read the Docs stores these rules in the project settings independently of Sphinx output and the build configuration in `readthedocs.yaml`; normal documentation builds preserve them. Retain or restore these settings when recreating the hosting project or changing its URL scheme.

The wildcard preserves the requested version, page path, query parameters, and section anchor, including links to stylesheets, scripts, images, and page sources. The `/en` shorthand follows the project's current default version. After changing hosting settings, check `/en`, `/en/stable/`, `/en/latest/`, `/en/devel/`, and `/en/v4.0.0-beta.1/Install/beta1.html`, plus a search query and static assets. See the [Read the Docs redirect reference](https://docs.readthedocs.com/platform/stable/user-defined-redirects.html) for wildcard behavior.

## Working with the Docs

First, create a virtual environment:

``` bash
cd docs
sudo apt install python3-venv -y
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Or you can use the `create_venv.sh` script provided by sourcing it:

```bash
. ./create_venv.sh
```

Now you have the requirements:

- `sphinx`
- `sphinx_rtd_theme`
- `myst-parser`
- `esbonio`
- `requests`

From here you can `make html` to create the docs in `./build/html`.

You can also use the release script `copy_docs.sh` to copy the documentation to your local webserver at `wsprrypi/docs`.

## Pico and Fleet operator documentation

The normal build includes Pico connections, USB firmware updates, fleet
scheduling, recovery, command-line options and configuration references. No
Pico-specific build flag is required, including on Read the Docs.

These topics are written for a WsprryPi operator adding Pico outputs and
managing a fleet. Start with [Add a WsprryPico](docs/Install/pico.md).
The [WsprryPico operator manual](https://wsprrypico.readthedocs.io/en/devel/)
covers standalone use, initial firmware installation, Pico browser controls,
hardware limits and device recovery. Its
[engineering guide](https://github.com/WsprryPi/WsprryPico/blob/devel/engineering/development/README.md)
owns Pico architecture, protocols and implementation details.

Keep Pi connection, Fleet, host scheduling, CLI/INI and Pi-managed update
instructions here. Link to the Pico manual for device-side procedures instead
of duplicating them. Both manuals link back to the relevant task in the other.

Build from the repository root:

```bash
source docs/.venv/bin/activate
python -m sphinx -b html docs docs/_build/html
```
