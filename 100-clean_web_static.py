#!/usr/bin/python3
"""Fabric script that creates and distributes an archive to web servers"""

from fabric.api import local, put, env, run
from fabric.context_managers import lcd, cd
import os
import datetime


env.hosts = ['34.74.113.207', '35.227.64.73']
env.user = 'ubuntu'


def do_pack():
    """Function that generates a .tgz archive from the contents of the
    web_static"""
    try:
        local("mkdir -p versions")
        now = datetime.datetime.now()
        date = now.strftime("%Y%m%d%H%M%S")
        filename = "versions/web_static_" + date + ".tgz"
        tar_cmd = "tar -cvzf " + filename + " web_static"
        local(tar_cmd)
        return filename
    except:
        return None


def do_deploy(archive_path):
    """Function that distributes an archive to web servers"""
    if not os.path.exists(archive_path):
        return False
    else:
        try:
            arch_name = archive_path.split("/")[-1]
            remote_path_tgz = "/tmp/" + arch_name
            release_path = "/data/web_static/releases/" + arch_name[:-4] + "/"
            put(archive_path, "/tmp/")
            run("mkdir -p {}".format(release_path))
            run("tar -xzf {} -C {}".format(remote_path_tgz, release_path))
            run("rm {}".format(remote_path_tgz))
            run("mv {}web_static/* {}".format(release_path, release_path))
            run("rm -rf {}web_static".format(release_path))
            run("rm -rf /data/web_static/current")
            run("ln -s {} /data/web_static/current".format(release_path))
            return True
        except:
            return False


def deploy():
    """creates and distributes an archive"""
    filename = do_pack()
    if not filename:
        return False
    else:
        return do_deploy(filename)


def do_clean(number=0):
    """Clean unnecesary versions"""

    number = int(number)

    if number == 0:
        erase = 2
    else:
        erase = int(number) + 1

    if os.path.exists('versions'):
        with lcd("versions"):
            local('ls -1t | tail -n +{} | xargs rm -rf'.format(erase))
    try:
        with cd("/data/web_static/releases"):
            run('ls -1t | tail -n +{} | xargs rm -rf'.format(erase))
    except:
        pass
