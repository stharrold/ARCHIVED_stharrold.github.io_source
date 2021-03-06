#!/usr/bin/env python
# -*- coding: utf-8 -*- #
r"""Configuration settings for pelican.

See Also:
    publishconf.py

Notes:
    * Settings are defined in order from [1]_.
    * Undefined settings have default values from [1]_.

References:
    .. [1] http://docs.getpelican.com/en/3.6.3/settings.html

"""


# Import standard packages.
# For Python 2x compatibility:
from __future__ import unicode_literals
import os


# Basic settings
AUTHOR = 'Samuel Harrold'
OUTPUT_PATH = os.path.join(
    os.path.expanduser(r'~'),
    'stharrold.github.io/')
PATH = 'content'
# # Plugins
# # https://github.com/getpelican/pelican-plugins/tree/master/liquid_tags
# PLUGINS = ['liquid_tags.notebook']
# PLUGIN_PATHS = 'pelican-plugins'
# NOTEBOOK_DIR = 'notebooks'
SITENAME = 'Data Science Demos'
# Define SITEURL only when publishing.
SITEURL = ''
TIMEZONE = 'Etc/UTC'

# Feed settings
# Disable feed generation for developing.
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Translations
TRANSLATION_FEED_ATOM = None

# Themes
# TODO: https://github.com/duilio/pelican-octopress-theme
#THEME = 'pelican-themes/octopress'
# TODO: add other widget sfrom octopress
#SEARCH_BOX = True
#DISQUS_SITENAME = ''
GITHUB_URL = 'https://github.com/stharrold/stharrold.github.io_source'
#GOOGLE_ANALYTICS = 'UA-XXXX-YYYY'
SOCIAL = (
    ('stharrold', 'https://github.com/stharrold'),
    ('Samuel Harrold', 'https://www.linkedin.com/in/samuelharrold'),
    ('stharrold', 'https://twitter.com/stharrold'),
    ('Samuel Harrold', 'https://plus.google.com/+SamuelHarrold'),)
