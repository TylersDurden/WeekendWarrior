import socket
import os


def swap(fname,destroy):
    data = []
    for line in open(fname, 'r').readlines():
        data.append(line.replace('\n', ''))
    if destroy:
        os.remove(fname)
    return data


def get_ext_ip():
    os.system('echo $(GET https://api.ipify.org) >> ip.txt')
    return swap('ip.txt', True)


home = '104.143.92.210'
ip = ''
try:
    os.system('sh whatsmyip.sh >> ip.txt')
    lan_ip = swap('ip.txt', True).pop()
    ip = get_ext_ip()
    print ip
except IndexError:
    print 'No Internet Connection!'
    pass

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((home, 54321))
s.send('0000')
print s.recv(1024)
s.close()
