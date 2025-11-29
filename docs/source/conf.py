import os
import sys

# -----------------------------------------------------------------------------
# Path setup
# -----------------------------------------------------------------------------
HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

# Put the project root on sys.path so `import scripts`, `import utils`, etc. work
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# -----------------------------------------------------------------------------
# Project information
# -----------------------------------------------------------------------------
project = "Playground"
author = "Ankit Shrivastava"
copyright = f"2025, {author}"


# -----------------------------------------------------------------------------
# General configuration
# -----------------------------------------------------------------------------
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
master_doc = "index"

# Disable "module.function" prefixes in documentation
add_module_names = False

# Member ordering in autodoc
autodoc_member_order = "groupwise"


# -----------------------------------------------------------------------------
# Sphinx extensions
# -----------------------------------------------------------------------------
extensions = [
    "nbsphinx",                   # Jupyter notebook support
    "myst_parser",                # Markdown support
    "sphinx.ext.mathjax",
    "sphinx.ext.autodoc",         # Python API auto-documentation
    "sphinx.ext.autosummary",     # Auto-generates summary tables
    "sphinx.ext.napoleon",        # Google / NumPy docstring style
    "sphinx.ext.viewcode",        # Link to source code
    "sphinx_last_updated_by_git",
    "sphinx.ext.inheritance_diagram",
]

# Markdown math support
myst_enable_extensions = [
    "amsmath",
    "dollarmath",
]


# -----------------------------------------------------------------------------
# HTML output configuration
# -----------------------------------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_show_sourcelink = True
html_last_updated_fmt = "%b %d, %Y"


# -----------------------------------------------------------------------------
# Autodoc behavior
# -----------------------------------------------------------------------------
# Move type hints out of function signatures
autodoc_typehints = "description"     # or "none"

# Allow short signatures from the first docstring line
autodoc_docstring_signature = True

# Default autodoc options
autodoc_default_options = {
    "members": True,
    "undoc-members": False,
    "private-members": False,
    "special-members": "__call__",
    "inherited-members": False,
    "show-inheritance": True,
}

# Autosummary: auto-generate stub pages
autosummary_generate = True


# -----------------------------------------------------------------------------
# Custom autodoc behavior (never skip special methods)
# -----------------------------------------------------------------------------
def skip(app, what, name, obj, would_skip, options):
    if name in ("__init__", "__repr__", "__str__"):
        return False
    return would_skip


def setup(app):
    app.connect("autodoc-skip-member", skip)


# -----------------------------------------------------------------------------
# Version from VERSION file
# -----------------------------------------------------------------------------
VERSION_FILE = os.path.join(PROJECT_ROOT, "VERSION")
if os.path.exists(VERSION_FILE):
    with open(VERSION_FILE) as f:
        release = f.read().strip()
else:
    release = "0.0.0"  # fallback if VERSION missing

# Short version (major.minor)
version = ".".join(release.split(".")[:2])

# html_context = {
#   'current_version' : "1.0",
#   'versions' : [["1.0", "link to 1.0"], ["2.0", "link to 2.0"]],
#   'current_language': 'en',
#   'languages': [["en", "link to en"], ["de", "link to de"]]
# }


html_context = {
    "current_version": release,
    "versions": [
        # Fill this dynamically via gh-pages if you want,
        # or keep static list for now
        [release, f"https://your-site-url/{release}/"],
    ],
}
