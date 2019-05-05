from Crypto.Random import get_random_bytes
import pysnmp as snmp
import numpy as np
import paramiko
import socket
import os


def swap(fname, destroy):
    data = []
    for line in open(fname, 'r').readlines():
        data.append(line.replace('\n', ''))
    if destroy:
        os.remove(fname)
    return data


def ssh_command(ip, user, password, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=user, password=password)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.exec_command(command)
        response = ssh_session.recv(1024)
        return response


class Host:
    ip = ''
    ext_ip = ''
    geo_loc = ''
    os = ''
    os_info = {}
    # OS Environ Vars
    PATH = ''
    HOME = ''
    DESKTOP_SESSION = ''

    def __init__(self):
        self.initialize()

    def initialize(self):
        # Determine Internal LAN IP
        internal_ip = "ifconfig | grep ' netmask 255.255.255.0 ' | cut -b 14-28"
        os.system(internal_ip + ' >> ip.txt')
        self.ip = swap('ip.txt', True).pop()

        # Get External IP
        ext = 'echo $(curl -s https://ipinfo.io/$(curl -s https://api/ipify.org))'
        os.system(ext+' >> where.txt')
        location = swap('where.txt', True)
        for line in location:
            try:
                self.ext_ip = line.split('"ip":')[1].split(',')[0].replace('"','').replace(' ','')
            except IndexError:
                pass
            try:
                self.geo_loc = line.split('"loc":')[1].split(', "postal')[0].replace('"','')
            except IndexError:
                pass

        # Get Hostname
        self.os = os.name
        self.os_info['uid'] = os.getuid()
        self.os_info['username'] = os.getlogin()
        machine = os.uname()
        self.os_info['type'] = machine[0]
        self.os_info['cname'] = machine[1]
        self.os_info['kernel'] = machine[2]
        self.os_info['last_update'] = machine[3]
        self.os_info['env'] = os.environ

    def display_host(self):
        print '\033[1m' + self.os_info['cname']+'\033[0m\t Last Updated: \033[1m' +\
            self.os_info['last_update']
        print '\033[1m\033[32mOS: ' + self.os + ' ['+self.os_info['type']+']\033[0m'
        print '\033[1m\033[34mUserName: '+self.os_info['username']+'\033[0m'
        print '\033[1m\033[31mUID: '+str(self.os_info['uid'])+'\033[0m'
        for field in self.os_info['env'].keys():
            if field == 'PATH':
                print '\033[1m\033[36mPATH: '+self.os_info['env'][field]+'\033[0m'
                self.PATH = self.os_info['env'][field]
            if field == 'HOME':
                self.HOME = self.os_info['env'][field]
                print '\033[1m\033[33mHOME: '+self.os_info['env'][field]
            if field == 'DESKTOP_SESSION':
                self.DESKTOP_SESSION = self.os_info['env'][field]
                print '\033[1m\033[95mSESSION: '+self.os_info['env'][field]


def main():
    localhost = Host()
    localhost.display_host()


if __name__ == '__main__':
    main()
