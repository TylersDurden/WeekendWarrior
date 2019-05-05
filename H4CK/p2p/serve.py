import socket
import os


def swap(fname,destroy):
    data = []
    for line in open(fname, 'r').readlines():
        data.append(line.replace('\n', ''))
    if destroy:
        os.remove(fname)
    return data


def serve(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', port))
    s.listen(5)
    running = True

    clients = []
    requests = []
    while running:
        try:
            client, addr = s.accept()
            ip = addr[0]
            prt = addr[1]
            request = client.recv(1024)
            print '%s is requesting "%s"' % (ip, request)
            clients.append(ip)
            requests.append(request)
            client.send('ACK')
            client.close()
            running = False
        except socket.error:
            socket.close()
            running = False
    return requests, clients


request, client = serve(9999)
print client