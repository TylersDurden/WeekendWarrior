import os
import sys


def import_handler(package):
    os.system('yes | pip install '+package+';clear')
    print '\033[1mInstalled \033[34m'+package+'\033[0m'
    return True


try:
    import base64
    foundB64 = True
except ImportError:
    import_handler('base64')
    import base64
try:
    from Crypto.Cipher import AES
    foundAES = True
except ImportError:
    import_handler('PyCrypto')
    from Crypto.Cipher import AES
try:
    import time
except ImportError:
    import_handler('time')
    import time
try:
    print 'importing socket package [requires root]'
    import socket   # Needs root
except ImportError:
    import_handler('socket')
    import socket
try:
    import paramiko
except ImportError:
    import_handler('paramiko')
    import paramiko
try:
    import psutil
except ImportError:
    import_handler('psutil')
    import psutil
try:
    from threading import Thread
except ImportError:
    import_handler('threading')
    from threading import Thread
'''                                 END OF IMPORTs                                    '''
# ====================================UTIL_FCNs========================================== #


def ap_discovery(iface):
    t0 = time.time()
    find_aps = 'iw '+iface+' scan | grep "SSID:*" | cut -b 8-20 >> ssids.txt'
    os.system(find_aps)
    networks = []
    for ap in swap('ssids.txt', True):
        if ap not in networks and len(list(ap))>=1:
            networks.append(ap)
    if 'ID List' in networks:
        networks.remove('ID List')
    return networks


def swap(fname, destroy):
    data = []
    for line in open(fname,'r').readlines():
        data.append(line.replace('\n', ''))
    if destroy:
        os.remove(fname)
    return data


def file_encrypt(fname, destroy):
    BSZ = 16
    PADDING = '{'
    # DEFINE PADDING FUNCTION
    PAD = lambda s: s + (BSZ - len(s) % BSZ) * PADDING
    # EXTRACT FILE's CLEAR_TEXT
    content = ''
    for element in open(fname, 'r').readlines():
        content += element
    if destroy:
        os.remove(fname)
    # GET SOME RANDOM BYTES AND ENCRYPT
    secret = os.urandom(BSZ)
    if foundAES and foundB64:
        c = AES.new(secret)
        EncodeAES = lambda c, s: base64.b64encode(c.encrypt(PAD(s)))
        encrypted_data = EncodeAES(c, content)
        open('enc.txt', 'w').write(encrypted_data)
    return secret


def file_decrypt(fname, destroy, key):
    PADDING = '{'
    # EXTRACT FILE's CLEAR_TEXT
    content = ''
    for element in open(fname, 'r').readlines():
        if element.split(' ')[0] == '\n ':
            content += element
        else:
            content += element + ' '
    if destroy:
        os.remove(fname)
    if foundAES and foundB64:
        c = AES.new(key)
        DecodeAES = lambda c, s: c.decrypt(base64.b64decode(s)).rstrip(PADDING)
        return DecodeAES(c, content)


def ssh_command(ip, user, password, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=user, password=password)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.exec_command(command)
        response = ssh_session.recv(1024)
        return response


def show_nx_cnx():
    connections = {}
    for connection in psutil.net_connections():
        pid = str(connection.pid)
        lia = str(connection.laddr).split('ip=')[1].split(',')[0]
        lip = str(connection.laddr).split(', port=')[1].split(')')[0]
        try:
            ria = str(connection.raddr).split('ip=')[1].split(',')[0]
            rip = str(connection.raddr).split(', port=')[1].split(')')[0]
        except IndexError:
            rip = ''
            ria = ''
            pass
        print pid + '\t'+lia+':'+lip+' -> '+ria+':'+rip
        if pid == 'None':
            connections[lia+':'+lip] = ria+':'+rip
        else:
            connections[lia + ':' + lip] = ria + ':' + rip+'['+pid+']'
    return connections


Commander = {'#!': '\x23\x21',
             '$?': '\x24\x3f',
             ';': '\x3b',
             '>>': '\x3e\x3e',
             'exit': '\x65\x78\x69\x74',
             }


# ======================================================================================= #


def main():
    # A Demonstration of taking a program, deleting/encrypting it, and
    #    # Then proceeding to decrypt and execute successfully
    if 'demo' in sys.argv:
        prog = 's3c.py'
        key = file_encrypt(prog, True)
        clear_prog = file_decrypt('enc.txt', True, key)
        ln1 = clear_prog.split('\n')[0]
        rest = clear_prog.split(ln1)[1:]

        os.system('ls; sleep 3')
        print 'Creating Program from encrypted BLOB'
        open('program.py', 'w').write(clear_prog)
        print 'Attempting to run decrypted program'
        os.system('python program.py run')
        os.system('rm program.py')
        print '===================== FINISHED ======================'

    elif 'launch' in sys.argv:
        host = sys.argv[2]
        ip = sys.argv[3]
        failures = 0
        try:
            print ssh_command(ip, host, '', 'echo $PWD; echo $PATH')
        except paramiko.ssh_exception.AuthenticationException:
            failures += 1

    else:
        nx_connections = show_nx_cnx()


if __name__ == '__main__':
    main()
