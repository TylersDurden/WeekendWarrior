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

def wordsearch(target,close, verbose):
    found = False
    if close:
        almost = []
    else:
        close = False
    for word in word_bag:
        if str(target).upper() == str(word).upper():
            found = True
            if verbose:
                print "Found \033[1m\033[35m" + target + '\033[0m'
        if str(target).upper() in str(word).upper() and close:
            found = True
            almost.append(word)
            if verbose:
                print "Found \033[1m\033[35m" + word + '\033[0m'
        if str(target).upper() in str(word).upper().split(' ') and close:
            found = True
            almost.append(word)
            if verbose:
                print "Found \033[1m\033[35m" + word + '\033[0m'
    if not found and verbose:
        print "\033[1mCouldn't Find\033[31m " + target + '\033[0m'
    if close:
        if verbose:
            print '\033[1m\033[91m'+ str(len(almost))+" Similar Words Found\033[0m"
        return almost, found
    else:
        return found

def bow_hist(bOw):
    plt.bar(bOw.keys(),bOw.values())
    plt.title('Bag Of Words Histogram [Word Length]')
    plt.xlabel('Word Length [Letters]')
    plt.ylabel('N Words')
    plt.show()

word_bag = utils.swap('words.txt', False)
sentiment = {}
sorted_bag, binned = sort_by_size(word_bag)

def main():
    t0 = time.time()
    print '\033[1m' + str(len(word_bag)) + ' Words added to \033[31mBag Of Words '+\
          '\033[33m['+str(time.time()-t0)+'s Elapsed]\033[0m'

    if 'bins' in sys.argv:
        bow_hist(binned)
    if 'search' in sys.argv:
        close = False
        target = sys.argv[2]
        if '-similar' in sys.argv:
            close = True
        result = wordsearch(targetclose,True)

    print '\033[1m['+str(time.time()-t0)+'s Elapsed]\033[0m'

if __name__ == '__main__':
    main()
