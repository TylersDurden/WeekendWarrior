import subprocess
import threading
import sys
import os

'''  TRY TO IMPORT PARAMIKO  '''
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
'''  ~ ~ (|{||!:~SSH~:!||}|) ~ ~  '''
def swap(fname, destroy):
    data = []
    for line in open(fname, 'r').readlines():
        data.append(line.replace('\n', ''))
    if destroy:
        os.remove(fname)
    return data

def geoloc(rmt, passwd):
    ip = 'ifconfig | grep " netmask 255.255.255.0 " | cut -b 14-28'
    os.system('python monitor.py '+passwd+' -command "'+ip+'" >>cc.txt')
    ip_result = swap('cc.txt',True).pop()
    print ip_result
    geo = 'curl https://ipinfo.io/'+ip_result
    print '\033[1m\t\tREMOTE_HOST \033[31mGEO_LOCATION:\033[0m'
    ssh_command(rmt,'pi',passwd, geo)
    os.system('python monitor.py '+passwd+' -command "'+geo+'" >>cc.txt')
    geoloc = swap('cc.txt', True)
    return ip_result, geoloc

def main():
    rmt = '192.168.1.217'
    if hasMiko and len(sys.argv)<=2:
        remote_host, geo_location = geoloc(rmt,sys.argv[1])
        for i in range(1,8,1):
            print geo_location[i]
    if hasMiko and len(sys.argv)>2 and '-command' in sys.argv:
        ssh_command(rmt,'pi',sys.argv[1],sys.argv[3])
    elif len(sys.argv)>2:
        os.system('whoami')


if __name__ == '__main__':
    main()
