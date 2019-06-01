import shodan
import sys
import os


def swap(fname, destroy):
    data = []
    [data.append(line.replace('\n', '')) for line in open(fname, 'r').readlines()]
    if destroy:
        os.remove(fname)
    return data


def import_handler(package):
    os.system('yes | pip install '+package+';clear')
    print '\033[1mInstalled \033[34m'+package+'\033[0m'
    return True


def retrieve_api_key(verbose):
    os.system('python ../PiPwn/aes.py -d >> api.txt')
    api_key = swap('api.txt', True).pop().split('Result: ')[1]
    if verbose:
        print '\033[1m\033[31m Retrieved API_KEY: \033[0m\033[1m'+\
            api_key + '\033[0m'
    return api_key


def finger(sh, target):
    return sh.host(target)


def discover_ip_self():
    os.system('sh whatsmyip.sh >> local.txt')
    os.system('sh whatsmyextip.sh >> ext.txt')
    local_ip = swap('local.txt', True)
    ext_ip = swap('ext.txt', True)
    return local_ip, ext_ip


# Get your own IPs for testing
lip, eip = discover_ip_self()
# Initialize Shodan API Key and get Stats
api_key = retrieve_api_key(True)
shod = shodan.Shodan(api_key)
print shod.info()


if '-self' in sys.argv:
    self = finger(shod, eip)
    for field in self.keys():
        print field + ' : ' + str(self[field])
'''
Important fields: 
data, ports, lattitude, longitude, isp, org, region_code
'''
