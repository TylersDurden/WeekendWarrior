import matplotlib.animation as animation
import matplotlib.pyplot as plt
from threading import Thread
import numpy as np
import subprocess
import paramiko
import utils
import time
import sys
import os

snap_image = 'raspistill -t 1 -o test.jpeg'
snap_video = 'raspivid -o video_in.h264 -t 5000'
snap_lapse = 'raspistill -t 30000 -tl 200 -o image%03d.jpg'
unpack_vid = 'ffmpeg -loglevel quiet -r 30 -i video_in.h264 -vcodec copy '
pack_vid = 'ffmpeg -r 1/5 -i image%03d.jpg -c:v libx264 -vf fps=25 -pix_fmt yuv420p out.mp4'
clean_pics = "find -name '*.jpg' | cut -b 3- | while read n; do rm $n; done"


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


def remote_video(uname, passwd, remote_ip, file_name, show):
    t0 = time.time()
    ssh_command('192.168.1.229', uname, passwd, snap_video, True)
    cmd = 'sshpass -p' + passwd + ' sftp ' + uname + '@' + \
          remote_ip + ':/home/' + uname + '/video_in.h264 $PWD'
    os.system(cmd)
    print '\033[1m\033[31m' + str(time.time() - t0) + 's Elapsed]\033[0m'
    os.system(unpack_vid + file_name+'; rm video_in.h264')
    if show:
        p = subprocess.Popen(["xdg-open", file_name], stdout=subprocess.PIPE)
        p.communicate()
        return p.returncode
    else:
        return 0


def credential_manager():
    os.system('find -name encrypted.txt | cut -b 3- >> hasname.txt')
    if utils.swap('hasname.txt', True).pop() == 'encrypted.txt':
        uname = 'pi'
        os.system('echo $(python aes.py -d) >> passd.txt')
        passwd = utils.swap('passd.txt', True).pop().split('Result: ')[1]
    return uname, passwd


def create_timestamp():
    date = time.localtime(time.time())
    mo = str(date.tm_mon)
    day = str(date.tm_wday)
    yr = str(date.tm_year)

    hr = str(date.tm_hour)
    min = str(date.tm_min)
    sec = str(date.tm_sec)

    date = mo + '/' + day + '/' + yr
    timestamp = hr + ':' + min + ':' + sec
    return date, timestamp


def main():
    # First get the a current timestamp
    date, timestamp = create_timestamp()
    # Get Remote Host Password for session use
    uname, passwd = credential_manager()
    print '\033[1m\033[32m\t\t~ Credentials Stored ~\033[0m'
    remote_ip = '192.168.1.229'

    # Snap Image on remote system and transfer it to current dir
    if 'snap_img' in sys.argv:
        t0 = time.time()
        image = remote_photography('example.jpeg', uname, passwd, remote_ip)
        print '\033[1m\033[31m' + str(time.time() - t0) + 's Elapsed]\033[0m'
        plt.imshow(image)
        plt.show()

    if 'snap_lap' in sys.argv:
        t0 = time.time()
        ssh_command(remote_ip,uname,passwd,snap_lapse, True)
        ssh_command(remote_ip, uname, passwd, pack_vid, True)
         # TODO: Delete the time lapse photos!
        ssh_command(remote_ip, uname, passwd, clean_pics, False)
        print '\033[1m\033[31m' + str(time.time() - t0) + 's Elapsed]\033[0m'

    # snap a video
    if 'snap_vid' in sys.argv:
        if 'show' in sys.argv:
            show = True
        else:
            show = False
        remote_video(uname, passwd, remote_ip, date.replace('/','_')+'-'+\
                     timestamp.replace(':','_')+'_test.mp4', show)

    if 'live' in sys.argv:
        t0 = time.time()
        # Try to make it as fast as possible to show images in real time
        images = []
        for i in range(100):
            os.system('python control.py snap_vid')
            images.append([plt.imshow(plt.imread('example.jpeg'))])
            os.system('rm example.jpeg')

        print '\033[1m\033[31m' + str(time.time() - t0) + 's Elapsed]\033[0m'

    if 'cmd' in sys.argv:
        t0 = time.time()
        cmd = ''
        for arg in sys.argv[2:]:
            cmd += arg+' '
        answer = ssh_command(remote_ip, uname, passwd, cmd, True)
        print '\033[1m\033[31m' + str(time.time() - t0) + 's Elapsed]\033[0m'


if __name__ == '__main__':
    main()