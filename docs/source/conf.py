# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

from datetime import date

import toml

PY_PROJECT = toml.load("../../pyproject.toml")["tool"]["poetry"]

project = PY_PROJECT["name"]
version = PY_PROJECT["version"]
author: list[str] = [a.split("<")[0].strip() for a in PY_PROJECT["authors"]]

if len(author) > 3:
    shorts = []
    for a in author:
        first, last = a.split(" ")
        shorts.append(f"{first[0]}. {last}")
    author = shorts

author = ", ".join(author)
copyright = f"{date.today().year}, {author}"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = ['_templates']
extensions = [
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode'
]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
# html_static_path = ['_static']

# -- Napoleon configuration --------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#configuration

napoleon_include_init_with_doc = True
napoleon_preprocess_types = True
napoleon_type_aliases = None
