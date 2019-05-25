import os
import vol


def get_logins():
    os.system('cat /etc/passwd >> logs.txt')
    uids = {}
    for line in vol.swap('logs.txt', True):
        name = line.split(':')[0]
        try:
            uid = int(line.split(':')[2:3].pop())
            uids[name] = uid
        except:
            pass
    return uids


uname = os.getlogin()
uid = os.getuid()
logins = get_logins()

os.system('ps -u root >> procs.txt')
os.system('ps -u '+uname+' | grep tty >> self.txt')
root_procs = vol.swap('procs.txt', True)
self_procs = vol.swap('self.txt', True)

user_procs = {}
for proc in self_procs:
    pid = proc.split('tty2')[0].replace(' ','')
    process = proc.split('tty2')[1].split(':')[2].split(' ')[1]
    user_procs[pid] = process
