#!/usr/bin/python3
"""Write a Fabric script (based on the file 2-do_deploy_web_static.py)
   that creates and distributes an archive to your web servers,
   using the function deploy.
"""

import os
from fabric.api import *
from fabric.operations import run, put
import time
env.user = 'ubuntu'
env.hosts = ['34.138.198.203', '100.25.219.41']


def do_pack():
    """It generate a tgz archive"""
    date = time.strftime("%Y%m%d%H%M%S")

    """-c - instructs tar to create a new archive.
        -z - sets the compression method to gzip.
        -f archive-name.tgz - specifies the archive name.
        -v option to make the tar command more visible and print the names
        of the files being added to the archive on the terminal.
    """
    local("mkdir -p versions")
    local("tar -cvzf versions/web_static_{}.tgz web_static/".format(date))
    pathf = "versions/web_static_{}.tgz".format(date)
    if os.path.exists(pathf) and os.path.getsize(pathf) > 0:
        return (pathf)
    return None


def do_deploy(archive_path):
    """To distribute an archive to web servers
       Returns False if the file at the path archive_path doesn’t exist
    """
    if not os.path.exists(archive_path):
        return False

    """Upload the archive to the /tmp/ directory of the web server"""
    unpack = archive_path.split("/")[-1]
    arch_path = "/data/web_static/releases/"
    ext = unpack.split(".")[0]
    put(archive_path, "/tmp/")
    run("mkdir -p {}{}/".format(arch_path, ext))

    """Uncompress the archive to the folder
    /data/web_static/releases/<archive filename without extension>
    on the web server"""
    run("tar -xzf /tmp/{} -C {}{}/".format(unpack, arch_path, ext))

    """Delete the archive from the web server"""
    run("rm /tmp/{}".format(unpack))
    run("mv {0}{1}/web_static/* {0}{1}/".format(arch_path, ext))
    run("rm -rf {}{}/web_static".format(arch_path, ext))

    """Delete the symbolic link /data/web_static/current
        from the web server"""
    run("rm -rf /data/web_static/current")
    """Create a new the symbolic link /data/web_static/current on the
        web server, linked to the new version of your code
        (/data/web_static/releases/<archive filename without extension>)
    """
    run("ln -s {}{}/ /data/web_static/current".format(arch_path, ext))
    return True


def deploy():
    archive_path = do_pack()
    if archive_path:
        archive_created = do_deploy(archive_path)
        return archive_created
    return False
