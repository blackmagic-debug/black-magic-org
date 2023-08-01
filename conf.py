# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
from urllib.parse import urlunparse, ParseResult

# -- Helper functions --------------------------------------------------------


# Build valid URL from parts
def build_url(netloc='', path='', params='', query='', fragment='', scheme='https'):
    if '__contains__' in dir(path) and not isinstance(path, str):
        path = '/'.join(path)  # merge path parts into a single string
    return urlunparse(ParseResult(scheme, netloc, path, params, query, fragment))


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
language = 'en'

# -- Project information not required by sphinx ------------------------------

project_decription = 'The Plug&Play MCU Debugger'

# URLs
netloc_black_magic_org = 'black-magic.org'
netloc_1b2 = '1bitsquared.com'
netloc_1b2_eu = netloc_1b2.replace('.com', '.de')
netloc_github = 'github.com'

github_org_slug = 'blackmagic-debug'
github_bmd_slug = 'blackmagic'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'ablog',
    'myst_parser',
    'sphinx_favicon',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.extlinks',
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

extlinks = {
    'black-magic-org-gh': (build_url(netloc_github, [github_org_slug, '%s']), None),
    'bmd-gh': (build_url(netloc_github, [github_org_slug, github_bmd_slug, '%s']), None),
    'bmd-issue': (build_url(netloc_github, [github_org_slug, github_bmd_slug, 'issues/%s']), 'BMD Issue #%s'),
    '1b2': (build_url(netloc_1b2, '%s'), None),
    '1b2-eu': (build_url(netloc_1b2_eu, '%s'), None),
    '1b2-product': (build_url(netloc_1b2, 'products/%s'), '1BitSquared US store product %s'),
    '1b2-product-eu': (build_url(netloc_1b2_eu, 'products/%s'), '1BitSquared EU store product %s'),
    'github': (build_url(netloc_github, '%s'), None),
    'github-user': (build_url(netloc_github, '%s'), '@%s'),
}

# Produce warnings for hard-coded external links that can be replaced with extlinks
extlinks_detect_hardcoded_links = True

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

html_baseurl = build_url(netloc_black_magic_org)

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'
html_copy_source = False

html_theme_options = {
    'logo': 'blackmagic-logo.svg',
    'github_user': github_org_slug,
    'github_repo': github_bmd_slug,
    'description': project_decription,
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

blog_baseurl = html_baseurl

blog_authors = {
    'esden': ('Piotr Esden-Tempski', build_url(netloc_github, 'esden')),
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

ogp_site_url = html_baseurl
ogp_site_name = project
ogp_image = "_static/blackmagic-logo.png"

# Generate pinout diagrams

os.system('./_pinouts/generate.py')
