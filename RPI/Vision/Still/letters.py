import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import numpy as np
import time
import sys
import os

t0 = time.time()

Letters = {}
raw_images = {}
alphabet = {}
letter_box = {0:[240,220],1:[240,360],2:[365,360],3:[365,220]}
shape = []
images = os.listdir('alphabet')
for image in images:
    alpha = plt.imread('alphabet/'+image)
    l = image.split('.jpeg')[0]
    raw_images[l] = alpha
    x1=letter_box[0][1]
    y1=letter_box[0][0]
    x2=letter_box[1][1]
    y2=letter_box[2][0]

    alphabet[l] = alpha[y1:y2,x1:x2,:]
    shape = np.array(alpha[y1:y2,x1:x2,:]).shape

    im = np.array(alphabet[l][:,:,2]) > np.array(alphabet[l][:,:,2]).mean()
    m = ndi.binary_erosion(im).astype(im.dtype)
    mask = ndi.binary_closing(im).astype(im.dtype)
    Letters[l] = [im, m, mask]

print '\033[1mPreprocessed \033[31m' + str(len(alphabet.keys())) +\
      ' ' + str(shape)+ '\033[0m\033[1m Images\033[0m'
print '\033[1m\033[31m' + str(time.time()-t0) + 's Elapsed\033[0m'
