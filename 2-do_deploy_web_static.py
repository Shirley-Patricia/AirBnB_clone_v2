#!/usr/bin/python3
"""Write a Fabric script (based on the file 1-pack_web_static.py)
   that distributes an archive to your web servers,
   using the function do_deploy:
"""

import os
from fabric.api import *
from fabric.operations import run, put, sudo
from fabric.context_managers import cd
import time
env.user = 'ubuntu'
env.hosts = ['34.138.198.203 web-01', '100.25.219.41 web-02']


def do_deploy(archive_path):
    """To distribute an archive to web servers
       Returns False if the file at the path archive_path doesn’t exist
    """
    try:
        if not os.path.isfile(archive_path):
            return False
        """Upload the archive to the /tmp/ directory of the web server"""
        put(archive_path, "/tmp/")
        unpack = archive_path.split("/")[-1]
        folder = ("/data/web_static/releases/" + unpack.split(".")[0])
        run("mkdir -p {}/".format(folder))

        """Uncompress the archive to the folder
        /data/web_static/releases/<archive filename without extension>
        on the web server"""
        run("tar -xzf /tmp/{} -C {}/".format(unpack, folder))

        """Delete the archive from the web server"""
        run("rm /tmp/{}".format(unpack))
        run("mv {}/web_static/* {}/".format(folder, folder))
        run("rm -rf {}/web_static")

        """Delete the symbolic link /data/web_static/current
           from the web server"""
        run("rm -rf /data/web_static/current")
        """Create a new the symbolic link /data/web_static/current on the
           web server, linked to the new version of your code
           (/data/web_static/releases/<archive filename without extension>)
        """
        run("ln -s {} /data/web_static/current".format(folder))
        return True
    except:
        return False
