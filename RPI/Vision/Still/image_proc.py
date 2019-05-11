import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import numpy as np
import sys
import os

if 'load' in sys.argv:
    im = plt.imread('remote.jpeg')

target = {'c1': [620,1200],  # [y1, x1]
          'c2': [620,1830],  # [y1, x2]
          'c3': [1096,1830], # [y2, x2]
          'c4': [1096,1200]} # [y2, x1]

c1 = target['c1']
c2 = target['c2']
c3 = target['c3']
c4 = target['c4']

sharpen = [[0,-1,0],[-1,5,-1],[0,-1,0]]

# Create a Field of View
fov = im[c1[0]:c3[0],c1[1]:c3[1]]
fov = ndi.convolve(fov[:,:,2],np.array(sharpen))

edges = 10*fov /ndi.gaussian_laplace(im[c1[0]:c3[0],c1[1]:c3[1]][:,:,2],sigma=2)
f, ax = plt.subplots(1, 2, sharex=True,sharey=True)
#ax[0].imshow(im[c1[0]:c3[0],c1[1]:c3[1]], 'gray_r')
#ax[1].imshow(edges,'gray_r')
#plt.show()

plt.imsave('fov.jpeg', edges)
os.remove('remote.jpeg')
