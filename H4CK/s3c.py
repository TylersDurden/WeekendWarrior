import sys
import os

CMDS = {'nx_stat': 'iw dev wlp2s0 link',
        'nx_connect': 'sudo wpa_supplicant -c /etc/wpa_supplicant.conf -i wlps0',
        'watch_live_stream': 'vlc rtsp://'}


def arp():
    try:
        from scapy.all import arping
        arping('192.168.1.*')
    except ImportError:
        print "Couldn't Import Scapy "
    except KeyError:
        print "ARP Scan didn't work right..."


def ssh_command(ip, user, passwordd, command):
    try:
        import paramiko
    except ImportError:
        print "Missing \033[1mParamiko\033[0m Library"
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=user, password=passwordd)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.exec_command(command)
        response = ssh_session.recv(1024)
        return response


def swap(fname, destroy):
    data = []
    [data.append(line.replace('\n','')) for line in open(fname, 'r').readlines()]
    if destroy:
        os.remove(fname)
    return data


def readir(dir_path, verbose):
    content = {'files': [], 'dirs': []}
    for item in os.listdir(dir_path):
        if os.path.isdir(dir_path + item):
            content['dirs'].append(item)
        else:
            content['files'].append(item)
    if verbose:
        print '\033[1m\033[33mExploring '+dir_path+'\033[0m'
        print '\033[1m'+str(len(content['dirs'])) + '\033[34m Directories\033[0m'
        print '\033[1m'+str(len(content['files'])) + '\033[31m Files\033[0m'
    return content


if 'run' in sys.argv:
    # Gets linux kernel version
    os.system('uname -mrs>>self.txt')
    os.system('w>>self.txt;id>>self.txt;who>>self.txt')
    user_data = swap('self.txt', True)
    readir('/proc/', True)

if 'arp' in sys.argv:
    arp()

