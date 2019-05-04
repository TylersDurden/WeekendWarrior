import matplotlib.pyplot as plt
import numpy as np
import sys


colors = {'r':[1,0,0],'g':[0,1,0],'b':[0,0,1],
          'c':[0,1,1],'m':[1,0,1],'y':[1,1,0],
          'k':[0,0,0],'w':[1,1,1]}

def show_colors():
    block = np.zeros((3,3,3))
    rbx = np.zeros((3,3,3))
    gbx = np.zeros((3,3,3))
    bbx = np.zeros((3,3,3))
    cbx = np.zeros((3,3,3))
    mbx = np.zeros((3,3,3))
    ybx = np.zeros((3,3,3))

    rbx[:,:,:] = [1,0,0]
    gbx[:,:,:] = [0,1,0]
    bbx[:,:,:] = [0,0,1]
    cbx[:,:,:] = [0,1,1]
    mbx[:,:,:] = [1,0,1]
    ybx[:,:,:] = [1,1,0]

    row1 = np.concatenate((rbx,gbx,bbx),1)
    row2 = np.concatenate((cbx,mbx,ybx),1)
    sample = np.concatenate((row1,row2),0)
    plt.imshow(sample)
    plt.show()


if 'demo' in sys.argv:
    show_colors()
