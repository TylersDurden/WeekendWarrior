import wordcollector
import numpy
import utils
import time
import sys
import os


t0 = time.time()
topic = ''
KB = 'KB/'
if '-find' in sys.argv:
    t = sys.argv[2:]
    for wo in t:
        topic += wo +' '
topic = topic.replace(' ','_')
print "Researching " + topic
os.system('python knowledge.py get '+topic)

test = utils.swap(topic+'_result.txt', True)
result = {}
lines = 0
for line in test:
    try:
        result[lines] = line.split('<p>')[1]
        lines += 1
    except:
        pass
print '\033[1m'+str(len(result.keys())) + '\033[32m Paragraphs Collected\033[0m'
recognized = []
for ln in result.keys():
    for word in result[ln].split(' '):
        w = word.replace('.','')
        w = w.replace('<','')
        w = w.replace('>','')
        w = w.replace('/','')
        w = w.replace('.','')
        w = w.replace('"','')
        w = w.replace('(','')
        w = w.replace(')','')
        w = w.replace(',','')
        if wordcollector.wordsearch(w,False,False):
            recognized.append(w)
        elif word == topic:
            recognized.append(word)
    print 'Finished Analyzing Paragraph '+str(ln)+\
          ' ['+str(len(recognized)) + " Words Recognized]"
print '\033[1m\033[31m FINISHED '+str(time.time()-t0) + 's Elapsed]\033[0m]'
answer = ''
cntr = 0
for lets in recognized:
    answer += lets +' '
    cntr += 1
    if cntr >= 10:
        answer+='\n'
        cntr=0
os.system('touch '+KB+topic+'_result'+".txt")
fd = os.open(KB+topic+'_result'+".txt",os.O_RDWR)
ret = os.write(fd,answer)
os.system('cat '+KB+topic+'_result'+".txt")
