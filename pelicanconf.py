#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#AUTHOR = 'Jim Newsome'
SITENAME = 'jimnewsome.net'
SITEURL = 'http://localhost:8000'

#THEME = 'themes/pelican-themes/notmyidea-cms'
THEME = 'notmyidea'

PATH = 'source'
OUTPUT_PATH = 'output_local/'
DELETE_OUTPUT_DIRECTORY = True

ARTICLE_PATHS = ['posts']
ARTICLE_URL = 'posts/{slug}/'
ARTICLE_SAVE_AS = 'posts/{slug}/index.html'

USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'posts'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
SLUGIFY_SOURCE = 'basename'

STATIC_PATHS = ['images', 'projects', 'static']

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'css_class': 'highlight',
            'guess_lang': False},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins/pelican-jupyter']
PLUGINS = ['pelican_jupyter.markup']
IPYNB_MARKUP_USE_FIRST_CELL = True
IPYNB_SKIP_CSS = False
IPYNB_FIX_CSS = True

# if you create jupyter files in the content dir, snapshots are saved with the same
# metadata. These need to be ignored.
IGNORE_FILES = [".ipynb_checkpoints"]

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_RSS = 'feeds/rss.xml'
RSS_FEED_SUMMARY_ONLY = True
FEED_ATOM = 'feeds/atom.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
TAG_FEED_ATOM = 'feeds/tags/{slug}.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Mastodon', 'https://mastodon.social/@sporksmith'),
          ('Twitter', 'https://twitter.com/sporksmith'),
          ('GitHub', 'http://github.com/sporksmith'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
