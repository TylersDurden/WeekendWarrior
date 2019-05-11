import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import numpy as np
import sys
import os


def slice_image_boxes(im, show):
    drive_way_box = {'x1': 450, 'y1': 1000, 'x2': 2500, 'y2': 1650}
    street_box = {'x1': 400, 'y1': 1100, 'x2': 1850, 'y2': 1550}
    sky = {'x1': 400, 'y1': 0, 'x2': 2650, 'y2': 950}

    drive_way = im[drive_way_box['y1']:drive_way_box['y2'],
                drive_way_box['x1']:drive_way_box['x2'], :]

    street = im[street_box['y1']:street_box['y2'],
             street_box['x1']:street_box['x2'], :]

    sky_box = im[sky['y1']:sky['y2'],
              sky['x1']:sky['x2'], :]

    if show:
        f, ax = plt.subplots(3, 1, figsize=(12,6))
        ax[0].imshow(street)
        ax[1].imshow(drive_way)
        ax[2].imshow(sky_box)
        plt.show()
    return drive_way, street


if '-split' in sys.argv:
    file_in = 'example.jpeg'
    im = plt.imread(file_in)
    driveway, steet = slice_image_boxes(im, True)

