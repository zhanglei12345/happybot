#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import *

# env.hosts = ['user@ip:port']

def prepare():
    local("git add . && git commit")
    local("git push")

def deploy():
    code_dir = '/root/study/happybot'
    # Fabric默认程序出错就退出，设置warn_only可以只发出警告而不退出
    with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
            run("git clone https://github.com/zhanglei12345/happybot.git %s" % code_dir)
    with cd(code_dir):
        run("git pull")
    # 重启Python服务:
    with settings(warn_only=True):
        sudo('supervisorctl stop happybot')
        sudo('supervisorctl start happybot')