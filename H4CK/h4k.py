import os


def swap(fname, destroy):
    data = []
    for line in open(fname, 'r').readlines():
        data.append(line.replace('\n', ''))
    if destroy:
        os.remove(fname)
    return data


def dir_ect(dir_path, verbose):
    content = {'files': [], 'dirs': []}
    for item in os.listdir(dir_path):
        if os.path.isdir(dir_path + item):
            content['dirs'].append(item)
        else:
            content['files'].append(item)
    if verbose:
        print '\033[1m\033[33mExploring '+dir_path+'\033[0m'
        print '\033[1m'+str(len(content['dirs'])) + '\033[34m Directories\033[0m'
        print '\033[1m'+str(len(content['files'])) + '\033[31m Files\033[0m'
    return content


# Gets linux kernel version
os.system('uname -mrs>>self.txt')
os.system('w>>self.txt;id>>self.txt;who>>self.txt')
user_data = swap('self.txt', True)
dir_ect('/proc/',True)
