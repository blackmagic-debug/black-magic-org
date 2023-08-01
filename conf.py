# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os

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
copyright = '2022-2023, Piotr Esden-Tempski <piotr@esden.net>; 2022-2023, Rachel Mant <git@dragonmux.network>'
author = 'Piotr Esden-Tempski <piotr@esden.net>, Rachel Mant <git@dragonmux.network>'
language  = 'en'
html_baseurl = 'https://black-magic.org'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'ablog',
    'myst_parser',
    'sphinx_favicon',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.githubpages',
    'sphinx.ext.graphviz',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinxcontrib.asciinema',
    'sphinxcontrib.platformpicker',
    'sphinxcontrib.youtube',
    'sphinxext.opengraph',
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Make sure autosectionlabel targets are unique
autosectionlabel_prefix_document = True

todo_include_todos = True

myst_heading_anchors = 3

napoleon_use_ivar = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'env', 'README.md']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'
html_copy_source = False

html_theme_options = {
    'logo': 'blackmagic-logo.svg',
    'github_user': 'blackmagic-debug',
    'github_repo': 'blackmagic',
    'description': 'The Plug&Play MCU Debugger',
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'ablog/recentposts.html',
        'ablog/archives.html',
        'relations.html',
        'searchbox.html',
        'donate.html',
    ]
}

blog_baseurl = "https://black-magic.org"

blog_authors = {
    'esden': ('Piotr Esden-Tempski', 'https://github.com/esden'),
}

# Favicon settings
favicons = [
    {
        "rel": "icon",
        "static-file": "favicon/icon.svg",  # => use `_static/icon.svg`
        "type": "image/svg+xml",
    },
    {
        "rel": "icon",
        "sizes": "16x16",
        "static-file": "favicon/favicon-16x16.png",
        "type": "image/png",
    },
    {
        "rel": "icon",
        "sizes": "32x32",
        "static-file": "favicon/favicon-32x32.png",
        "type": "image/png",
    },
    {
        "rel": "apple-touch-icon",
        "sizes": "57x57",
        "static-file": "favicon/apple-touch-icon-57x57.png",
        "type": "image/png",
    },
    {
        "rel": "apple-touch-icon",
        "sizes": "60x60",
        "static-file": "favicon/apple-touch-icon-60x60.png",
        "type": "image/png",
    },
    {
        "rel": "apple-touch-icon",
        "sizes": "72x72",
        "static-file": "favicon/apple-touch-icon-72x72.png",
        "type": "image/png",
    },
    {
        "rel": "apple-touch-icon",
        "sizes": "76x76",
        "static-file": "favicon/apple-touch-icon-76x76.png",
        "type": "image/png",
    },
    {
        "rel": "apple-touch-icon",
        "sizes": "96x96",
        "static-file": "favicon/apple-touch-icon-96x96.png",
        "type": "image/png",
    },
    {
        "rel": "apple-touch-icon",
        "sizes": "114x114",
        "static-file": "favicon/apple-touch-icon-114x114.png",
        "type": "image/png",
    },
    {
        "rel": "apple-touch-icon",
        "sizes": "120x120",
        "static-file": "favicon/apple-touch-icon-120x120.png",
        "type": "image/png",
    },
    {
        "rel": "apple-touch-icon",
        "sizes": "144x144",
        "static-file": "favicon/apple-touch-icon-144x144.png",
        "type": "image/png",
    },
    {
        "rel": "apple-touch-icon",
        "sizes": "152x152",
        "static-file": "favicon/apple-touch-icon-152x152.png",
        "type": "image/png",
    },
    {
        "rel": "apple-touch-icon",
        "sizes": "180x180",
        "static-file": "favicon/apple-touch-icon-180x180.png",
        "type": "image/png",
    },
    {
        "rel": "android-icon",
        "sizes": "192x192",
        "static-file": "favicon/android-icon-192x192.png",
        "type": "image/png",
    },
]

ogp_site_url = "https://black-magic.org"
ogp_site_name = "Black Magic Debug"
ogp_image = "_static/blackmagic-logo.png"

# Generate pinout diagrams

os.system('./_pinouts/generate.py')
