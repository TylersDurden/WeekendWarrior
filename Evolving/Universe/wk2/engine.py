import matplotlib.animation as animation
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import numpy as np
import utility
import agent
import time


def test_kernel(ex_config, k1, verbose):
    r = ndi.convolve(ex_config['state'][:, :, 0], k1)
    g = ndi.convolve(ex_config['state'][:, :, 1], k1)
    b = ndi.convolve(ex_config['state'][:, :, 2], k1)
    c = r + g + b

    print 'Max:\t' + str(np.array(c).max())
    print 'Mean:\t' + str(np.array(c).mean())
    if verbose:
        f, ax = plt.subplots(1, 2, sharey=True, sharex=True)
        ax[0].imshow(ex_config['state'], 'gray_r')
        ax[1].imshow(c)
        plt.show()
    return c


def initial_configuration(config):
    state = np.zeros((config['width'], config['height'], 3))
    if 'n_red' in config.keys():
        for r in range(config['n_red']):
            [rx, ry] = utility.spawn_random_point(state)
            state[rx, ry,:] = [1,0,0]
    if 'n_green' in config.keys():
        for g in range(config['n_green']):
            [gx, gy] = utility.spawn_random_point(state)
            state[gx, gy, :] = [0, 1, 0]
    if 'n_blue' in config.keys():
        for b in range(config['n_blue']):
            [bx, by] = utility.spawn_random_point(state)
            state[bx, by, :] = [0, 0, 1]
    if config['show_init']:
        plt.imshow(state)
        plt.title('Initial State')
        plt.show()
    return state


def main():
    k1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    ex_config = {'width': 100,
                 'height': 100,
                 'n_red': 500,
                 'n_green': 300,
                 'n_blue': 400,
                 'show_init': False}

    t0 = time.time()
    ex_config['state'] = initial_configuration(ex_config)
    dt = time.time() - t0
    print '\033[1m\033[31mFINISHED\t\033[0m\033[1m[' + str(dt) + 's Elapsed]\033[0m'
    test_kernel(ex_config, k1, True)

    random_start = utility.spawn_random_point(ex_config['state'])
    agent.Agent(random_start[0], random_start[1], ex_config['state'])


if __name__ == '__main__':
    main()

