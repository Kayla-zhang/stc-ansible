# Configuration file for the Sphinx documentation builder.
# For the full list of built-in options see:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = "STC Ansible"
author = "VIAVI Solutions Inc."
copyright = "2019-2026, VIAVI Solutions Inc."

# The full version, including alpha/beta/rc tags
release = "1.0"
version = "1.0"

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The master toctree document.
master_doc = "index"

# The suffix(es) of source filenames.
source_suffix = {".rst": "restructuredtext"}

# Show "todo" admonitions in the build output.
todo_include_todos = True

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"

# VIAVI brand-color accents on the ReadTheDocs theme.
html_theme_options = {
    "logo_only": False,
    "prev_next_buttons_location": "bottom",
    "style_external_links": True,
    # VIAVI brand purple ~#491E88, set the navigation/banner color.
    "style_nav_header_background": "#491E88",
    "collapse_navigation": False,
    "sticky_navigation": True,
    "navigation_depth": 4,
}

html_static_path = ["_static"]

# Add a custom stylesheet for fine-tuning brand colors.
html_css_files = ["viavi-brand.css"]

# Page title and short title.
html_title = "STC Ansible Documentation"
html_short_title = "STC Ansible"

# -- Options for intersphinx -------------------------------------------------

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "ansible": ("https://docs.ansible.com/ansible/latest", None),
}
