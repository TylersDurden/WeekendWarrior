import urllib
import urllib2
import sys


if 'get' in sys.argv:
    url = sys.argv[2]

    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    values = {'name': 'KnowledgeBot',
              'location': 'Interwebs',
              'language': 'Python' }
    headers = {'User-Agent': user_agent}
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(req)
    the_page = response.read()

    print "RESPONSE SIZE: " + str(len(the_page))
