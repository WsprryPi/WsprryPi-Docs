# WsprryPi Documentation

The documents are written in Markdown with Sphinx and hosted on Read the Docs (RTD) and accessible via [wsprdocs.aa0nt.net](http://wsprdocs.aa0nt.net/).

## RTD Documentation Labels

Three labels are maintained and automatically built by RTD:

- `stable`: Built from the latest released version
- `latest`: Built from the default branch (`main`), but not guaranteed to be a release and can be ahead of `stable`.
- `devel`: Build from the devel branch, and generally considered in development along side it's corresponding code.

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

## Optional WsprryPico Documentation

WsprryPico development documentation is **hidden by default** in all builds,
including Read the Docs. The build flag controls the Pico backend entries,
setup and recovery instructions, CLI reference, and WTP INI reference. Hidden
content is omitted from rendered pages, navigation, search, and the published
page sources. The general Raspberry Pi Pico incompatibility note remains visible.
This flag changes documentation visibility only.

From the repository root, build the default documentation with:

```bash
source docs/.venv/bin/activate
python -m sphinx -b html docs docs/_build/html
```

To include the Pico documentation for a development build:

```bash
source docs/.venv/bin/activate
WSPRRYPI_DOCS_INCLUDE_PICO=1 python -m sphinx -b html docs docs/_build/html
```

Alternatively, pass `-D wsprrypico_docs=1` to Sphinx. For Read the Docs, set
`WSPRRYPI_DOCS_INCLUDE_PICO=1` in the build environment to opt in; leave it unset
or set it to `0` to hide the content. Rebuild and republish after changing the
flag. Changing its value also refreshes an existing Sphinx build environment.

When adding Pico content, enclose complete sections, labels, and their links in
the following source markers. Blocks cannot be nested. An optional
`<!-- else-wsprrypico -->` marker supplies text for the default build.

```markdown
<!-- if-wsprrypico -->
## Pico development topic

Pico-specific documentation goes here.
<!-- endif-wsprrypico -->
```
