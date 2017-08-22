from fabric.api import *

env.hosts = ['root@198.181.59.210:26580']

def prepare():
    local("whoami")

def deploy():
    run('whoami')
    run('cd;ls')