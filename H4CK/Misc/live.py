import vol
import os

try:
    import socket
except ImportError:
    vol.import_hander('socket')
    import socket
try:
    import paramiko
except ImportError:
    vol.import_handler('paramiko')
    import paramiko


def listener():
    # Listens for commands
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s1.bind(('0.0.0.0', 2139))
    s1.listen(10)


APs = vol.ap_discovery('wlp2s0')
for ap in APs:
    print ap
