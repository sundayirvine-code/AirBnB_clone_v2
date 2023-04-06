#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack.
"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Compresses the contents of the web_static folder into a .tgz archive
    """
    try:
        if not os.path.exists('versions'):
            os.makedirs('versions')
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = "web_static_" + timestamp + ".tgz"
        filepath = os.path.join('versions', filename)
        local("tar -cvzf {} web_static".format(filepath))
        return filepath
    except:
        return None
