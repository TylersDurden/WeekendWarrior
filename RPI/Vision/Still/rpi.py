import numpy as np
import socket
import time
import sys
import os


def snap_im(file_name):
    cmd = 'raspistill -t 1 -o '+file_name+'.jpeg'
    os.system(cmd)


def flush_im(name):
    os.remove(name+'.jpeg')

def operate(run_time, port):
    t0 = time.time()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', port))
    sock.listen(5)
    while (time.time()-t0) < run_time:
        try:
            client, addr = sock.accept()
            request = client.recv(1024)
            if request:
                if request == 'snap':
                    snap_im('remote')
                if request == 'flush':
                    flush_im('remote')
                client.send('ACK')
                if client.recv(1024)=='flush':
                    flush_im('remote')
                client.close()
                break
        except socket.error:
            sock.close()
    sock.close()

t0 = time.time()
operate(100, 2222)
