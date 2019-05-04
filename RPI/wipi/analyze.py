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
        
