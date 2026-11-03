# Repository instructions

- This repo uses the local Python virtual environment at `docs/.venv`.
- Before running Sphinx commands, use `source docs/.venv/bin/activate`.
- Prefer `python -m sphinx -b html docs docs/_build/html`.
- Do not use `/usr/bin/python3` for docs builds.

## Cross-repo UI CSS reference

- The WsprryPi application UI is not part of this repository.
- If available at `../WsprryPi/WsprryPi-UI`, it may be used as visual reference only.
- Never modify files outside this docs repository.
- Do not copy application CSS wholesale into the docs.
- Translate only compatible typography, spacing, color, border, and card patterns into `docs/_static/css/custom.css`.
- Preserve Read the Docs sidebar, search, and mobile behavior.
