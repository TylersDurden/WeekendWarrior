import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import utils
import time
import sys


def initialize(config):
    config['state'] = np.zeros((config['width'], config['height']))
    config['steps'] = utils.spawn_random_walk(config['start'], config['n_steps'])
    return config


def eval_init(config):
    config['stop'] = config['steps'].pop(len(config['steps'])-1)
    disp = utils.displacement(config['start'], config['stop'])
    config['state'] = utils.simulate_walk(config['steps'], config['state'])
    score = utils.count_tiles(config['state'])
    return [disp, score]


def batch_pre_process(config, show_plot, t0):
    displacements = []
    scores = []
    batch_data = {}
    for trial in range(config['batch_size']):
        conf = initialize(config)
        [disp, rating] = eval_init(conf)
        displacements.append(disp)
        batch_data[trial] = [disp, rating]
        scores.append(len(rating))
    print "\033[1m\033[32mFINISHED SIMULATING \033[0m\033[1m[" + \
          str(time.time() - t0) + 's Elapsed\033[0m]'

    if show_plot:
        print 'Plotting '+str(config['batch_size'])+' Batch Data'
        avg = np.array(scores).mean()
        maximum = np.array(scores).max()
        minimum = np.array(scores).min()

        davg = np.array(displacements).mean()
        dmax = np.array(displacements).max()
        dmin = np.array(displacements).min()

        print "Avg Score: " + str(avg)
        print "Max Score: " + str(maximum)
        print "Min Score: " + str(minimum)
        print '\033[1m\033[31m=======================================\033[0m'
        print "Avg Displacement: " + str(davg)
        print "Max Displacement: " + str(dmax)
        print "Min Displacement: " + str(dmin)

        f, ax = plt.subplots(1, 2)
        ax[0].hist(displacements, 10)
        ax[0].set_title('Displacement(s) [10 Bins]')
        ax[1].hist(scores, 50)
        ax[1].set_title('Scores(s) [50 Bins]')
        plt.grid(True)
        plt.show()

    return [displacements, scores, batch_data]


def main():
    t0 = time.time()

    if 'demo' in sys.argv:
        config = {'width': 250,
                  'height': 250,
                  'start': [100, 100],
                  'stop': [],
                  'steps': [],
                  'n_steps': 250,
                  'state': [[]]}
        config = initialize(config)
        utils.animate_walk(config['steps'], config['state'], 50, False, '')
        [dR, score] = eval_init(config)
        print "Displacement: " + str(dR)
        print "Score: " + str(len(score))

    if 'test' in sys.argv:
        config = {'width': 250,
                  'height': 250,
                  'start': [100, 100],
                  'stop': [],
                  'steps': [],
                  'n_steps': 100,
                  'batch_size': 750,
                  'state': [[]]}
        [displaced, scores, batch_data] = batch_pre_process(config, True,t0)

    print "\033[1m\033[34mFINISHED\t   \033[0m\033[1m[" + \
          str(time.time() - t0) + 's Elapsed\033[0m]'



if __name__ == '__main__':
    main()
