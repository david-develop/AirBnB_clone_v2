#!/usr/bin/python3
"""Fabric script that creates and distributes an archive to web servers"""

from fabric.api import local, put, env, run
from fabric.context_managers import lcd, cd
import os
import datetime


env.hosts = ['34.74.113.207', '35.227.64.73']
env.user = 'ubuntu'


def do_clean(number=0):
    """Clean unnecesary versions"""

    number = int(number)

    if number == 0:
        erase = 2
    else:
        erase = int(number) + 1

    if os.path.exists('versions'):
        with lcd("versions"):
            local('ls -t | tail -n +{} | xargs rm -rf'.format(erase))
    try:
        with cd("/data/web_static/releases"):
            run('ls -t | tail -n +{} | xargs rm -rf'.format(erase))
    except:
        pass
