# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.abspath('_ext'))

# -- Project information -----------------------------------------------------

project = u'WsprryPi'
copyright = u'2023 - 2026, Lee C. Bussy (and others)'
author = u'Lee C. Bussy'

def _run_git(args):
    """
    Run a git command and return stripped stdout.
    Returns empty string on failure.
    """
    try:
        out = subprocess.check_output(
            args,
            stderr=subprocess.DEVNULL,
        )
        return out.decode('utf-8', errors='replace').strip()
    except Exception:
        return ""

def _strip_v_prefix(s):
    return re.sub(r'^v', '', s or "")

def _short_sha(s):
    """
    Make a short-ish identifier for display.
    RTD often provides a full sha; trim to 7 if it looks like one.
    """
    if not s:
        return ""
    if re.fullmatch(r"[0-9a-fA-F]{7,40}", s):
        return s[:7]
    return s

# Read the RTD version selection.
# stable / latest / devel per your setup.
_rtd_version = os.environ.get("READTHEDOCS_VERSION", "").strip()

# RTD provides an identifier for the checked-out revision.
# Often a commit sha, sometimes a tag/branch-ish string depending on setup.
_rtd_identifier = os.environ.get("READTHEDOCS_GIT_IDENTIFIER", "").strip()
_rtd_identifier = _short_sha(_rtd_identifier)

# Decide displayed version/release.
#
# - stable: latest local tag (in this repo checkout), fallback to "stable"
# - latest: "main" + sha (or just "main" if no sha)
# - devel: "devel" + sha (or just "devel" if no sha)
# - anything else: show the RTD value
if _rtd_version == "stable":
    _tag = _strip_v_prefix(_run_git(["git", "describe", "--tag", "--abbrev=0"]))
    _desc = _strip_v_prefix(_run_git(["git", "describe", "--tags"]))
    version = _tag or "stable"
    release = _desc or version
elif _rtd_version == "latest":
    version = "main"
    release = ("main-" + _rtd_identifier) if _rtd_identifier else "main"
elif _rtd_version == "devel":
    version = "devel"
    release = ("devel-" + _rtd_identifier) if _rtd_identifier else "devel"
else:
    version = _rtd_version or "devel"
    release = (_rtd_identifier or version)

# -- General configuration ---------------------------------------------------

extensions = [
    'feature_flags',
    'image_delivery',
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
]

# Optional development documentation; also configurable with -D wsprrypico_docs=1.
wsprrypico_docs = os.environ.get('WSPRRYPI_DOCS_INCLUDE_PICO', '0') == '1'

templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.md'

# The master toctree document.
master_doc = 'index'

language = 'en'

exclude_patterns = [u'_build', 'Thumbs.db', '.DS_Store', '.venv/*', 'venv/*']

pygments_style = None

# -- MyST configuration ------------------------------------------------------
# Optional, but avoids surprises if you use common Markdown features.

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "tasklist",
]

myst_heading_anchors = 3

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'logo_only': False,
    'prev_next_buttons_location': 'both',
    'style_external_links': True,
    # 'version_selector': True,  # Removed as requested.

    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 3,
    'includehidden': True,
    'titles_only': True
}

# disable epub mimetype warnings
suppress_warnings = ["epub.unknown_project_files"]

html_logo = '_static/WsprryPi_Logo.png'
html_favicon = '_static/favicon.ico'

# Put the custom.css in the html static path folder (Default is _static folder).
html_css_files = [
    'css/custom.css',
]

html_js_files = [
    'js/accessibility.js',
]

html_static_path = ['_static']

# -- Options for HTMLHelp output ---------------------------------------------

htmlhelp_basename = 'WsprryPidoc'

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {}

latex_documents = [
    (master_doc, 'WsprryPi.tex', u'WsprryPi Documentation',
     u'Lee C. Bussy (and others)', 'manual'),
]

# -- Options for manual page output ------------------------------------------

man_pages = [
    (master_doc, 'wsprrypi', u'WsprryPi Documentation',
     [author], 1)
]

# -- Options for Texinfo output ----------------------------------------------

texinfo_documents = [
    (master_doc, 'WsprryPi', u'WsprryPi Documentation',
     author, 'WsprryPi', 'One line description of project.',
     'Miscellaneous'),
]

# -- Options for Epub output -------------------------------------------------

epub_title = project
epub_exclude_files = ['search.html']

# -- Extension configuration -------------------------------------------------

todo_include_todos = True
