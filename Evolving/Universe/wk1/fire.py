import matplotlib.animation as animation
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import numpy as np
import utility

colors = {'r':[1,0,0],'g':[0,1,0],'b':[0,0,1],
          'c':[0,1,1],'m':[1,0,1],'y':[1,1,0],
          'k':[0,0,0],'w':[1,1,1]}

def build_forest(width,height,N, show):
    tree_size = 2
    forest = np.zeros((width, height, 3))
    for y in np.arange(10,height-10,N):
        for x in np.arange(10,width-10,N):
            forest[x-tree_size:x+tree_size,
                   y-tree_size:y+tree_size,:] = [0,1,0]
    if show:
        plt.imshow(forest)
        plt.show()
    return forest

build_forest(155,155,16,True)
