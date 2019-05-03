import urllib
import urllib2
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
