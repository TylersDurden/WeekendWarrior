from skimage.feature import blob_dog, blob_doh, blob_log
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import numpy as np
import time
import sys
import os

T0 = time.time()
verbose = True

if len(sys.argv)==2:
    # file_name = sys.argv[1]
    image = plt.imread(sys.argv[1])
    dims = image.shape
    if verbose:
        print "Image Loaded [Dimension: "+str(dims)+"]"
        r = image[:,:,0]
        g = image[:,:,1]
        b = image[:,:,2]

        rt = np.array(b > b.mean()).astype(np.float)
        gt = np.array(g > g.mean()).astype(np.float)
        bt = np.array(b > b.mean()).astype(np.float)

        com = np.zeros(image.shape)

        com[:,:,2] = ndi.gaussian_laplace(rt,sigma=.42)
        com[:,:,1] = ndi.gaussian_laplace(gt,sigma=.51)
        com[:,:,0] = ndi.gaussian_laplace(bt, sigma=.42)
        sight = image/com

        igray = rgb2gray(sight)
        #blog = blob_log(igray, max_sigma=30,num_sigma=10,threshold=.1)
        #blog[:,:,2] = blog[:,:,2]*np.sqrt(2)
        f, ax = plt.subplots(1,3)
        ax[0].imshow(image)
        ax[1].imshow(com)
        ax[2].imshow(ndi.gaussian_laplace(sight,sigma=1))
        plt.show()
