# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# from sys import path
# from pathlib import Path
# path.insert(0, str(Path('.').resolve()))


# -- Project information -----------------------------------------------------

project = 'Black Magic Debug'
copyright = '2022, Piotr Esden-Tempski <piotr@esden.net>; 2022, Rachel Mant <git@dragonmux.network>'
author = 'Piotr Esden-Tempski <piotr@esden.net>, Rachel Mant <git@dragonmux.network>'
language  = 'en'
html_baseurl = 'https://black-magic.org'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
    'sphinx.ext.todo',
    'sphinx.ext.githubpages',
    'sphinx.ext.graphviz',
    'sphinx.ext.napoleon',
    'sphinxcontrib.platformpicker',
    'sphinxcontrib.asciinema',
    'sphinxcontrib.youtube',
]

source_suffix = {
	'.rst': 'restructuredtext',
	'.md': 'markdown',
}

todo_include_todos = True

myst_heading_anchors = 3

napoleon_use_ivar = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'env']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'
html_copy_source = False

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
