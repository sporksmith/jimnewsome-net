# -*- coding: utf-8 -*-

import os
import shutil
import sys
import datetime

from invoke import task
from invoke.util import cd
from pelican.server import ComplexHTTPRequestHandler, RootedHTTPServer
from pelican.settings import DEFAULT_CONFIG, get_settings_from_file

SETTINGS_FILE_BASE = 'pelicanconf.py'
SETTINGS = {}
SETTINGS.update(DEFAULT_CONFIG)
SETTINGS.update(get_settings_from_file(SETTINGS_FILE_BASE))

SETTINGS_FILE_PUBLISH = 'publishconf.py'
SETTINGS_PUBLISH = {}
SETTINGS_PUBLISH.update(DEFAULT_CONFIG)
SETTINGS_PUBLISH.update(get_settings_from_file(SETTINGS_FILE_PUBLISH))

CONFIG = {
    'settings_base': SETTINGS_FILE_BASE,
    'settings_publish': SETTINGS_FILE_PUBLISH,
    # Github Pages configuration
    'github_pages_branch': 'master',
    'commit_message': "'Publish site on {}'".format(datetime.date.today().isoformat()),
    # Port for `serve`
    'port': 8000,

    # For rsync deployment
    'ssh_host': 'ssh.phx.nearlyfreespeech.net',
    'ssh_user': 'jnewsome_jimnewsome',
    'ssh_port': 22,
    'ssh_path': '/home/public/'
}

@task
def clean(c):
    """Remove generated files"""
    for path in (SETTINGS['OUTPUT_PATH'], SETTINGS_PUBLISH['OUTPUT_PATH']):
        if os.path.isdir(path):
            shutil.rmtree(path)
            os.makedirs(path)

@task
def build(c):
    """Build local version of site"""
    c.run('pelican -s {settings_base}'.format(**CONFIG))

@task
def rebuild(c):
    """`build` with the delete switch"""
    c.run('pelican -d -s {settings_base}'.format(**CONFIG))

@task
def regenerate(c):
    """Automatically regenerate site upon file modification"""
    c.run('pelican -r -s {settings_base}'.format(**CONFIG))

@task
def serve(c):
    """Serve site at http://localhost:$PORT/ (default port is 8000)"""

    class AddressReuseTCPServer(RootedHTTPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(
        SETTINGS['output_path'],
        ('', CONFIG['port']),
        ComplexHTTPRequestHandler)

    sys.stderr.write('Serving on port {port} ...\n'.format(**CONFIG))
    server.serve_forever()

@task
def reserve(c):
    """`build`, then `serve`"""
    build(c)
    serve(c)

@task
def preview(c):
    """Build production version of site"""
    c.run('pelican -s {settings_publish}'.format(**CONFIG))

@task
def livereload(c):
    """Automatically reload browser tab upon file modification."""
    from livereload import Server
    build(c)
    server = Server()
    # Watch the base settings file
    server.watch(CONFIG['settings_base'], lambda: build(c))
    # Watch content source files
    content_file_extensions = ['.md', '.rst']
    for extension in content_file_extensions:
        content_blob = '{0}/**/*{1}'.format(SETTINGS['PATH'], extension)
        server.watch(content_blob, lambda: build(c))
    # Watch the theme's templates and static assets
    theme_path = SETTINGS['THEME']
    server.watch('{}/templates/*.html'.format(theme_path), lambda: build(c))
    static_file_extensions = ['.css', '.js']
    for extension in static_file_extensions:
        static_file = '{0}/static/**/*{1}'.format(theme_path, extension)
        server.watch(static_file, lambda: build(c))
    # Serve output path on configured port
    server.serve(port=CONFIG['port'], root=SETTINGS['OUTPUT_PATH'])


@task
def publish(c):
    """Publish to production via rsync"""
    c.run('pelican -s {settings_publish}'.format(**CONFIG))
    c.run(
        'rsync --delete --exclude ".DS_Store" -pthrvz -c '
        '-e "ssh -p {ssh_port}" '
        '{} {ssh_user}@{ssh_host}:{ssh_path}'.format(
            SETTINGS_PUBLISH['OUTPUT_PATH'].rstrip('/') + '/',
            **CONFIG))
