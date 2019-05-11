from skimage.feature import blob_dog, blob_log, blob_doh
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import numpy as np
import sys
import os


def blobify(dims, activation, depth, show):
    dims = [width, height]
    state = np.random.random_integers(0,1,width*height).reshape((width,height))
    k0 = [[1,1,1,1],[1,0,0,1],[1,0,0,1],[1,1,1,1]]
    data = []
    if show:
        f = plt.figure()
    for frame in range(depth):
        ii = 0
        dims = state.shape
        s = state.flatten()
        for cell in ndi.convolve(state, k0).flatten():
            try:
                if cell >= activation:
                    s[ii] = 1
                else:
                    s[ii] = 0
                ii += 1
            except IndexError:
                pass
        state = s.reshape((dims))
        data.append([plt.imshow(state,'gray_r')])
    if show:
        a = animation.ArtistAnimation(f, data,interval=100,blit=True,repeat_delay=900)
        plt.show()
    return state


if 'blobs' in sys.argv:
    width = 450
    height = 450
    state = blobify([width, height], 7, 5, False)

    plt.imshow(state, 'gray_r')
    plt.show()
    plt.imsave('ex.jpeg', state, cmap='gray_r')
    os.system('python blobs.py ex.jpeg;rm ex.jpeg')
