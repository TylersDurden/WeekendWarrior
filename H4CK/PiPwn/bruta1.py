import numpy as np
import paramiko
import os


def swap(fname,destroy):
    data = []
    for line in open(fname, 'r').readlines():
        data.append(line.replace('\n', ''))
    if destroy:
        os.remove(fname)
    return data


def ssh_command(ip, user, passwordd, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=user, password=passwordd)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.exec_command(command)
        response = ssh_session.recv(1024)
        return response


def prep_word_list(words):
    bins = {}
    for i in range(105):
        bins[i] = []
    for word in words:
        bins[len(word)].append(word)
    probs = {}

    for val in bins.keys():
        nwords = len(bins[val])
        probs[val] = 1000*(float(nwords)/len(words))
    try:
        print 'Mean Probability Words: ' + str(np.mean(probs.values())) + '%\t' + \
              str(probs[int(np.array(probs.values()).mean())]) + ' Letters'
    except KeyError:
        pass
    try:
        print "Max Probability Words: " + str(np.array(probs.values()).max()) + '%\t' + \
              str(probs[int(np.array(probs.values()).max())]) + ' Letters '
    except KeyError:
        pass

    best = np.array(probs.values())
    best.sort()
    better = {}
    for b in best:
        for k in probs.keys():
            if probs[k] == b:
                better[k] = bins[k]
    return better


TARGET = '192.168.1.229'
uname = 'pi'
raw_word_list = swap('../NLP/words.txt', False)
print '\033[1m\033[31m' + str(len(raw_word_list)) +\
      "\033[0m\033[1m Words In \033[2mBag Of Words\033[0m"
sorted_words = prep_word_list(raw_word_list)

most_common = []
for length in np.arange(2,10,1):
    for word in sorted_words[length]:
        most_common.append(word)
print str(len(most_common)) + ' word list compiled of most probably words '
most_common.reverse()



