import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import numpy as np
import sys
import os


def video_2_images(file_in, fps):
    D = file_in.split('.')[0].replace('_','')
    os.system('mkdir '+D)
    cmd = 'ffmpeg -loglevel quiet -i '+file_in+' -r '+str(fps)+' '+ D +'/image%d.jpeg'
    os.system(cmd)
    return D


if 'auto' in sys.argv:
    cmd = 'python control.py snap_vid; clear; ' \
          'find -name "*.mp4" | cut -b 3- | while read n;' \
          ' do python video_proc.py $n; done'
    os.system(cmd)
elif len(sys.argv) > 1:
    img_path = video_2_images(sys.argv[1], 10)
    print '\033[1m' + str(len(os.listdir(img_path))) + ' Images Made from \033[31m' + sys.argv[1] + '\033[0m'
    os.system('mv ' + sys.argv[1] + ' ' + img_path)