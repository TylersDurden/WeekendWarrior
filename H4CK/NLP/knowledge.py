import urllib
import urllib2
import utils
import sys
import os


class MetaAgent:
    wiki_src = 'https://en.wikipedia.org/wiki/'
    subject = ''
    link = ''

    def __init__(self, topic):
        self.subject = topic
        self.link = self.wiki_src+topic
        raw_data = fetch_resource(self.link)
        print '\033[1mFETCHING \033[33m'+self.link+'...\033[0m'
        os.system('touch '+topic+'_result'+".txt")
        fd = os.open(topic+'_result'+".txt",os.O_RDWR)
        ret = os.write(fd,raw_data)


class Knowledge:
    kb = {}
    vocabulary = list()

    def __init__(self):
        self.initialize()

    def initialize(self):
        os.system('ls KB/ >> topics.txt')
        known_subjects = utils.swap('topics.txt',True)
        for subj in known_subjects:
            topic = subj.split('_result.txt')[0].replace('_',"")
            self.kb[topic] = utils.swap('KB/'+subj, False)
            sz = len(self.kb[topic])
            print 'Importing Knowledge of subject\t%s\033[1m\t\b%d lines\033[0m' % (topic,sz)
        vocabulary = utils.swap('words.txt', False)
        print '\033[1m\033[34m%d Words Added to Vocabulary\033[0m' % (len(vocabulary))


def fetch_resource(url):
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    values = {'name': 'KnowledgeBot',
              'location': 'Interwebs',
              'language': 'Python' }
    headers = {'User-Agent': user_agent}
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(req)
    the_page = response.read()
    return the_page


if 'get' in sys.argv:
    MetaAgent(sys.argv[2])
else:
    knowledge_base = Knowledge()
