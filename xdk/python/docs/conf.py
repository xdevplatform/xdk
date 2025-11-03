import os
import sys
from datetime import datetime

# Ensure package is importable
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)

project = "XDK Python SDK"
author = "XDK"
copyright = f"{datetime.now().year}, {author}"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
]

autosummary_generate = True
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
}

# Napoleon (Google/NumPy docstrings)
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_attr_annotations = True

# Autodoc settings
autodoc_docstring_signature = False
autodoc_inherit_docstrings = True
autodoc_typehints = "description"

# Reduce cross-ref noise
nitpicky = False

templates_path = ["_templates"]
exclude_patterns = []

html_theme = "alabaster"
