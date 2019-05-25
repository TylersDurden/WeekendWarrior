import utils
import time
import sys
import os


t0 = time.time()

if '-e' in sys.argv:
    ''' using the aes module for quick encryption '''

    test = ''
    for e in sys.argv[2:]:
        test += e
    os.system('python aes.py -eF "' + test + '"')
    print '\033[1m\033[31mKey:\033[0m'
    for line in utils.swap('key.txt', False):
        print line
    print '\033[1m[\033[32mDONE\033[0m\033[1m KEY dumped to <key.txt>\033[0m\033[1m ' + \
          '\033[31m'+str(time.time() - t0) + 's Elapsed]\033[0m'

if '-d' in sys.argv:
    ''' using the aes module for quick decryption '''
    os.system('python aes.py -d clear')


# TODO: Recognize any new/unique aps and add them to growing list
if '-sniff' in sys.argv:
    iface = 'wlp2s0'
    find_aps = 'iw ' + iface + ' scan | grep SSID:* | cut -b 8-20 >> ssids.txt'
    os.system(find_aps)
    networks = []
    aps_raw = utils.swap('ssids.txt', True)
    for ap in aps_raw:
        if ap not in networks and len(list(ap)) >= 1:
            networks.append(ap)
    if 'ID List' in networks:
        networks.remove('ID List')
    print networks
    print '\033[32m\033[1m[DONE\033[0m\033[1m ' + str(time.time() - t0) + 's Elapsed]\033[0m'

