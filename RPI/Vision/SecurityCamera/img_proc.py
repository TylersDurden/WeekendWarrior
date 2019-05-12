import matplotlib.animation as animation
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import numpy as np
import control
import sys
import os

drive_way_box = {'c1': [1700, 2300], 'c2': [1700, 3200],
                 'c3': [2300, 2300], 'c4': [2500, 3200]}


if '-img' in sys.argv:
    [date, timestamp] = control.create_timestamp()
    # Dealing with a security photo
    imat = plt.imread('example.jpeg')
    x1 = drive_way_box['c1'][1]
    x2 = drive_way_box['c2'][1]
    y1 = drive_way_box['c1'][0]
    y2 = drive_way_box['c3'][0]
    drive = imat[y1:y2, x1:x2]
    pov = ndi.gaussian_laplace((drive[:,:,0]-drive[:,:,0].mean()),sigma=.51)
    focus = drive[:, :, 2]*pov/drive[:, :, 1]
    if 'show' in sys.argv:
        f, ax = plt.subplots(1, 3)
        ax[0].imshow(imat)
        ax[0].set_title(date+' @ '+timestamp)
        ax[1].imshow(drive)
        ax[1].set_title('drive_way')
        ax[2].imshow(focus,'gray_r')
        ax[2].set_title('Focus View: drive_way')
        plt.show()

    print drive.shape

if '-vid' in sys.argv:
    [date, timestamp] = control.create_timestamp()
    # Break video into stills
    fname = date.replace('/','_')+'-'+\
                     timestamp.replace(':','_')+'_test.mp4'
    cmd = ''
    os.system(cmd)
