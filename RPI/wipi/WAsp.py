from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from threading import Thread
import numpy as np
import socket
import time
import sys
import os

users = []
banned = []



def add_host(name):
    users.append(name)
    print '\033[1m\033[34m[' + name +\
          '\033[0m\033[1m has been added to KNOWN_HOSTS\033[0m]'


def run(runtime, port):
    known_hosts = []
    t0 = time.time()
    tokens = []
    while((time.time()-t0)<=runtime):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        newport = len(known_hosts)+port
        try:
            sock.bind(('0.0.0.0', newport))
            sock.listen(5)
        except socket.error:
            print "Having Issues Starting Server..."
            time.sleep(5)
            pass
        try:
            client, addr = sock.accept()
            request = client.recv(1024)
            ''' HANDLE REQUEST '''
            ip = addr[0]
            rmt_port = addr[1]
            if ip not in known_hosts:
                token = get_random_bytes(16)
                client.send(token)
                client.close()
                known_hosts.append(ip)
                tokens.append(token)
            elif request in tokens:
                add_host(ip)
                client.close()
                break
        except socket.error:
            break
        sock.close()

run(100, 8881)
