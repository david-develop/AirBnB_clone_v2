#!/usr/bin/python3
"""Fabric script that generates a .tgz"""

from fabric.api import local
import os
import datetime


def do_pack():
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
