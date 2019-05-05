import urllib2
import urllib
import time
import sys
import os

btc_resource_1 = 'https://api.coindesk.com/v1/bpi/currentprice.json'


def query(link):
    r = urllib2.Request(link)
    response = urllib2.urlopen(r)
    return response.read()


def parse_btc_query(btc_raw,verbose):
    data = {'date': '',
            'prices': []}
    for item in btc_raw.split(','):
        dat = item.split(':')
        if 'time' in dat[0].replace('}', '').replace('"', ''):
            date = dat[2].replace('}','').replace('"', '')
            if verbose:
                print date
            data['date'] = date
        if 'rate_float' in dat[0]:
            price = dat[1].replace('}', '')
            if verbose:
                print '\033[1mPRICE: \033[33m$' + price +'\033[0m'
            data['prices'].append(price)
    return data


def create_datestr():
    localtime = time.localtime(time.time())
    mm = str(localtime.tm_mon)
    dd = str(localtime.tm_mday)
    yy = str(localtime.tm_year)

    hh = str(localtime.tm_hour)
    min = str(localtime.tm_min)

    datestr = 'Prices/market' + mm + yy + dd + '_' + hh + '-' + min + '.txt'
    return datestr


log_name = create_datestr()
print '\033[1mCreating LOG %s \033[0m' % (log_name)
db = False
if not os.path.isdir('Prices/'):
    print 'Making Price Tracking DataBase'
    os.system('mkdir Prices/')
    db = True
else:
    db = True

t0 = time.time()
pause = 10
current_prices = parse_btc_query(query(btc_resource_1), True)
if os.path.isfile('Prices/'+log_name):
    print '\t\t** Creating Prices/ Directory For Logging **'
    log_name = 'Prices/' + current_prices['date'].replace(' ', '_') + '.txt'
    print 'touch '+log_name
    os.system('touch '+log_name)
if db:
    os.system('echo + str(current_prices[date]) + ttPrice LOG+>>'+log_name)
    for price in current_prices['prices']:
        os.system('echo '+str(price)+' >> '+log_name)
dt = 0
while dt < 36000:
    current_prices = parse_btc_query(query(btc_resource_1), True)
    for price in current_prices['prices']:
        os.system('echo '+str(price)+' >> '+log_name)
    os.system('echo **************************************** >> '+log_name)
    dt += (time.time()-t0)
    time.sleep(pause)
    print str(dt)+'s Elapsed'

