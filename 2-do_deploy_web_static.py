#!/usr/bin/python3
"""
Fabric script to deploy a static website.
"""

from fabric.api import run, put, env
import os

env.hosts = ['54.160.103.207', '54.160.103.207']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'

def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload archive to web server
        put(archive_path, '/tmp/')

        # Uncompress archive to folder /data/web_static/releases/<archive filename without extension> on web server
        archive_filename = os.path.basename(archive_path)
        folder_name = '/data/web_static/releases/' + archive_filename.split('.')[0]
        run('mkdir -p {}'.format(folder_name))
        run('tar -xzf /tmp/{} -C {}'.format(archive_filename, folder_name))

        # Delete archive from web server
        run('rm /tmp/{}'.format(archive_filename))

        # Delete symbolic link /data/web_static/current from web server
        run('rm -rf /data/web_static/current')

        # Create new symbolic link /data/web_static/current on web server linked to new version of code
        run('ln -s {} /data/web_static/current'.format(folder_name))

        print("New version deployed!")
        return True
    except:
        return False
