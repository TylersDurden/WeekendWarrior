import utils
import os


p = os.getcwd()+'/Geo/NM0.2'
web_data = utils.readir(p, False)
traces = {}
for city in web_data['dirs']:
    print "Loading "+city+" Data"
    data = utils.readir(p+'/'+city+'/'+utils.readir(p+'/'+city, False)['dirs'].pop(), False)
    if len(data['files']) > 1:
        print '\033[1m\033[31m'+str(len(data['files'])) + ' Traces Found\033[0m'
        traces[city] = []
        for f in data['files']:
            traces[city].append(utils.swap(p+'/'+city+'/LOGS/'+f, False))

