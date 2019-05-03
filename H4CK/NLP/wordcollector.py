import matplotlib.pyplot as plt
import numpy as np
import knowledge
import utils
import time
import sys


def sort_by_size(wordbag):
    words = {1:[],2:[],3:[],4:[],
             5:[],6:[],7:[],8:[],
             9:[],10:[],11:[],12:[],
             13:[],14:[],15:[],16:[],17:[],
             18:[],19:[],20:[],21:[],22:[],
             23:[],24:[],25:[],26:[],27:[],
             28:[],29:[],30:[],31:[],32:[]}
    for word in wordbag:
        try:
            words[int(len(word))].append(word)
        except:
            pass
    bins = {}
    for size in words.keys():
        bins[size] = len(words[size])
    return words, bins


t0 = time.time()
word_bag = utils.swap('words.txt', False)
sentiment = {}
sorted_bag, binned = sort_by_size(word_bag)
print '\033[1m' + str(len(word_bag)) + ' Words added to \033[31mBag Of Words '+\
      '\033[33m['+str(time.time()-t0)+'s Elapsed]\033[0m'

plt.bar(binned.keys(),binned.values())
plt.title('Bag Of Words Histogram [Word Length]')
plt.xlabel('Word Length [Letters]')
plt.ylabel('N Words')
plt.show()
