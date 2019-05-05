import socket
import time
import sys
import os


rpi_addr = '192.168.1.217'
path = ':/media/pi/9802-3A2C/Vision/remote.jpeg'

if 'snap' in sys.argv:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((rpi_addr, 2222))
    s.send('snap')
    ack = s.recv(128)
    if ack:
        time.sleep(1)
        os.system('sftp pi@'+rpi_addr+path+' $PWD')
        s.send('flush')
        if s.recv(124) == 'ACK':
            s.close()
        print "Image Acquired and Flushed from Remote System"
        os.system('python image_proc.py load')
