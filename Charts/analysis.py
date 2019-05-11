import matplotlib.pyplot as plt
import numpy as np
import os


def swap(fname, destroy):
    data = []
    for line in open(fname, 'r').readlines():
        data.append(line.replace('\n',''))
    if destroy:
        os.remove(fname)
    return data


def unpack_price_data():
    content = {}
    os.system('find -name *.txt* | cut -b 3- >> price_data.txt')
    price_files = swap('price_data.txt', True)
    for f in price_files:
        if f != 'price_data.txt':
            data = swap(f, False)
            print str(len(data)) + ' Lines in ' + f
            content[f] = data

    prices = {}
    for f in price_files:
        date = ''
        if f != 'price_data.txt':
            buffer = []
            n_samples = 0

            for line in swap(f, False):
                try:
                    if len(line.split('Price LOG')) >= 2:
                        date = line.split('Price LOG')[0]
                    else:
                        pass
                except IndexError:
                    pass
                try:
                    ln = float(line.split('.')[0]) + float(line.split('.')[1])
                    print ln
                    buffer.append(ln)
                except IndexError and ValueError:
                    pass
                try:
                    if len(line.split('*')) > 20:
                        prices[n_samples] = buffer
                        n_samples += 1
                        buffer = []

                except IndexError:
                    pass
    return content, prices


content, price_data = unpack_price_data()
print np.array(price_data.keys()).shape
print np.array(price_data.values()).shape
f = plt.figure()
lines = []
for k in price_data.keys():
    for point in price_data[k]:
        lines.append(point)

trend = np.array(lines)
print 'Min Price: ' + str(trend.min())
print 'Max Price: ' + str(trend.max())
print 'Mean Price: ' + str(trend.mean())
print 'Deviation: ' + str(trend.std())

plt.plot(np.array(lines).flatten(),'o')
plt.show()