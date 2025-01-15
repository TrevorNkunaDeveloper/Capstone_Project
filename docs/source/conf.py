# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Accomodation Booking System'
copyright = '2025, Hlulani Trevor Nkuna'
author = 'Hlulani Trevor Nkuna'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

import os
import sys
import django

# Add the root path of the Django project
sys.path.insert(0, os.path.abspath('../../'))

# Add the virtual environment's site-packages directory
sys.path.insert(1, os.path.abspath('../../venv/Lib/site-packages'))

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'booking_system.settings'

# Initialize Django
django.setup()
