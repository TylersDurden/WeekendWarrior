import matplotlib.pyplot as plt
from threading import Thread
import subprocess
import paramiko
import signal
import utils
import time
import sys
import os

snap_image = 'raspistill -t 1 -o test.jpeg'
snap_video = 'raspivid -o video_in.h264 -t 5000'
unpack_vid = 'ffmpeg -loglevel quiet -r 30 -i video_in.h264 -vcodec copy '


def ssh_command(ip, user, passwd, command, verbose):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=user, password=passwd)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.exec_command(command)
        response = ssh_session.recv(1024)
        if verbose:
            print response
    return response


def remote_photography(file_name, remote_host, passwd, remote_ip):
    ssh_command(remote_ip, remote_host, passwd, snap_image, False)
    print "Image Taken"
    # Now Transfer it
    cmd = 'sshpass -p ' + passwd + ' sftp ' + remote_host + '@' +\
          remote_ip + ':/home/' + remote_host + '/test.jpeg $PWD'
    os.system(cmd)
    # Remove it from remote system
    ssh_command(remote_ip, remote_host, passwd, 'rm test.jpeg', False)
    os.system('mv test.jpeg '+file_name)
    return plt.imread(file_name)


def credential_manager():
    os.system('find -name encrypted.txt | cut -b 3- >> hasname.txt')
    if utils.swap('hasname.txt', True).pop() == 'encrypted.txt':
        uname = 'pi'
        os.system('echo $(python aes.py -d) >> passd.txt')
        passwd = utils.swap('passd.txt', True).pop().split('Result: ')[1]
    return uname, passwd


def main():
    # Get Remote Host Password for session use
    uname, passwd = credential_manager()
    print '\033[1m\033[32m\t\t~ Credentials Stored ~\033[0m'
    remote_ip = '192.168.1.217'

    # Snap Image on remote system and transfer it to current dir
    if 'snap_demo' in sys.argv:
        t0 = time.time()
        image = remote_photography('example.jpeg', uname, passwd, remote_ip)
        print '\033[1m\033[31m' + str(time.time() - t0) + 's Elapsed]\033[0m'
        plt.imshow(image)
        plt.show()

    if 'snap_vid' in sys.argv:
        t0 = time.time()
        ssh_command('192.168.1.217', uname, passwd, snap_video, True)
        cmd = 'sshpass -p' + passwd + ' sftp ' + uname + '@' + \
              remote_ip + ':/home/' + uname + '/video_in.h264 $PWD'
        os.system(cmd)
        print '\033[1m\033[31m' + str(time.time() - t0) + 's Elapsed]\033[0m'
        os.system(unpack_vid + 'test.mp4; rm video_in.h264')
        p = subprocess.Popen(["xdg-open", "test.mp4"], stdout=subprocess.PIPE)
        p.communicate()


if __name__ == '__main__':
    main()
