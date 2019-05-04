import subprocess
import threading
import sys
import os

hasMiko = False
try:
    import paramiko
    hasMiko = True
except ImportError:
    pass

if hasMiko:
    def ssh_command(ip, user, passwd, command):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, username=user, password=passwd)
        ssh_session = client.get_transport().open_session()
        if ssh_session.active:
            ssh_session.exec_command(command)
            response = ssh_session.recv(1024)
            print response
            return response


def main():
    if hasMiko:
        ssh_command('192.168.1.217','pi',sys.argv[1],'sh ~/Desktop/whereami.sh')
    else:
        os.system('installing software')
        os.system('yes | pip install paramiko')
if __name__ == '__main__':
    main()
