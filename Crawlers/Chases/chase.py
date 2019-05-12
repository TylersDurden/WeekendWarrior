from matplotlib.animation import FFMpegWriter
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import utils
import sys
import os


def initialize(config):
    if not config['color']:
        config['state'] = np.zeros((config['width'], config['height']))
    else:
        config['state'] = np.zeros((config['width'], config['height'], 3))

    if not config['start']:
        if not config['color']:
            config['start'] = utils.spawn_random_point(np.zeros((config['width'], config['height'])))
        else:
            config['start'] = utils.spawn_random_point(np.zeros((config['width'], config['height'], 3)))
    if not config['target_start']:
        if not config['color']:
            config['target_start'] = utils.spawn_random_point(np.zeros((config['width'], config['height'])))
        else:
            config['target_start'] = utils.spawn_random_point(np.zeros((config['width'], config['height'], 3)))
    state = config['state']
    pt = config['start']
    if config['color']:
        state[pt[0], pt[1], :] = [1, 0, 0]
    else:
        state[pt[0], pt[1]] = 1
    config['state'] = state
    return config


config = {'width': 250,
          'height': 250,
          'color': True,
          'size': 2,
          'start': [],
          'target_start': []}

config = initialize(config)

