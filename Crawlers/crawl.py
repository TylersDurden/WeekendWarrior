from matplotlib.animation import FFMpegWriter
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import utils
import time
import sys


def animated_crawler(config):
    f = plt.figure()
    film = []
    captured = []
    state = config['initial_state']
    for step in config['steps']:
        if config['color']:
            try:
                if state[step[0], step[1], 0] == 1 and state[step[0], step[1], 1]==0 and state[step[0], step[1], 2]==0:
                    captured.append(step)
                state[step[0], step[1], :] = [0, 0, 1]
            except IndexError:
                pass
        else:
            try:
                if state[step[0], step[1]] == 1:
                    captured.append(step)
                state[step[0], step[1]] = -1
            except IndexError:
                pass
        film.append([plt.imshow(state)])
    a = animation.ArtistAnimation(f,film,interval=config['frame_rate'], blit=True,repeat_delay=900)
    plt.show()
    print '\033[1m' + str(len(captured)) + '\033[31m Particle(s) Captured \033[0m'
    return captured


def high_speed_crawler(config):
    captured = []
    state = config['initial_state']
    for step in config['steps']:
        if config['color']:
            try:
                if state[step[0],step[1],0]==1 and state[step[0],step[1],1]==0 and state[step[0],step[1],2]==0:
                    captured.append(step)
            except IndexError:
                pass
        else:
            try:
                if state[step[0], step[1]] == 1:
                    captured.append(step)
            except IndexError:
                pass
    return len(captured)


def initialize(config):
    n_points = config['n_obstacles']
    if config['color']:
        state = utils.add_random_points_color(np.zeros((config['width'], config['height'], 3)), n_points,'r')
        if config['start'] == []:
            start = utils.spawn_random_point(np.zeros((config['width'], config['height'])))
            state[start[0], start[1],:] = [0,0,1]
    else:
        state = utils.add_random_points(np.zeros((config['width'], config['height'])), n_points)
        if config['start'] == []:
            start = utils.spawn_random_point(np.zeros((config['width'], config['height'])))
            state[start[0], start[1]] = -1
    config['initial_state'] = state
    if config['start'] == []:
        config['start'] = np.array(utils.spawn_random_point(config['initial_state']))
    config['steps'] = utils.spawn_random_walk(config['start'], config['n_steps'])
    return high_speed_crawler(config)


def main():
    t0 = time.time()
    config = {'width': 100,
              'height': 100,
              'color': False,
              'n_obstacles': 500,
              'n_steps': 200,
              'n_trials': 45000,
              'start': [],
              'goal': [100, 100],
              'frame_rate': 50}

    if 'random walk distributions' in sys.argv:
        untrained_capture_data = []
        [untrained_capture_data.append(initialize(config)) for trial in range(config['n_trials'])]

        print '\033[1mFINISHED [' + str(time.time() - t0) + '] \033[0m'
        print 'N Trials: ' + str(config['n_trials'])
        print 'Mean Pts Captured: ' + str(np.array(untrained_capture_data).mean())
        print 'Max Pts Captured: ' + str(np.array(untrained_capture_data).max())
        print '-------------------------------------------------'

        plt.hist(untrained_capture_data)
        plt.show()





if __name__ == '__main__':
    main()
