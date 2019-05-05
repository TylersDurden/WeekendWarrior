from threading import Thread
from scapy.all import *
import time
import os


def swap(fname,destroy):
    data = []
    for line in open(fname, 'r').readlines():
        data.append(line.replace('\n', ''))
    if destroy:
        os.remove(fname)
    return data


def listen(t):
    print "STARTING NX LISTENER"
    start = time.time()
    os.system('sudo tshark -i wlp2s0 -n -O http,arp,dns -E separator=/n -c '+str(t)+' >> dump.txt')
    return (time.time()-start)


def listener(dt):
    start = time.time()
    t = Thread(target=listen, args=(dt,))
    t.run()
    start += (time.time()-start)
    return swap('dump.txt', True)


data = listener(2)
for line in data:
    try:
        print line.split('Src:')[1:]
    except IndexError:
        pass
    try:
        print line.split('Src Port:')[1:]
    except IndexError:
        pass
    try:
        print line.split('Ethernet II, ')[1]
    except IndexError:
        pass
    try:
        print line.split('Target IP Address: ')[1]
    except IndexError:
        pass
    try:
        print line.split('Sender IP Address: ')[1]
    except IndexError:
        pass