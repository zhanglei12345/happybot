from fabric.api import *

#env.hosts = ['user@ip:port']

def prepare():
    local("whoami")

def deploy():
    run('whoami')
    run('cd;ls')
