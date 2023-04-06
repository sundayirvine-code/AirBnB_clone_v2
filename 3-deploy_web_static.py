#!/usr/bin/python3
"""Distributes an archive to your web servers, using the function deploy"""

from fabric.api import *
from os.path import exists
env.hosts = ['54.160.103.207', '34.202.159.134']

def do_pack():
    """Creates a .tgz archive from the contents of the web_static folder"""
    local("mkdir -p versions")
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    path = "versions/web_static_{}.tgz".format(time)
    cmd = "tar -cvzf {} web_static".format(path)
    if local(cmd).succeeded:
        return path
    return None

def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    if not exists(archive_path):
        return False
    try:
        filename = archive_path.split("/")[-1]
        no_ext = filename.split(".")[0]
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}".format(no_ext))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(filename, no_ext))
        run("rm /tmp/{}".format(filename))
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(no_ext, no_ext))
        run("rm -rf /data/web_static/releases/{}/web_static".format(no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(no_ext))
        return True
    except:
        return False

def deploy():
    """Creates and distributes an archive to your web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
