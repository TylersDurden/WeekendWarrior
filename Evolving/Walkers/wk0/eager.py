import numpy as np
import utils
import time


def evaluate_walk(config):
    displacement = []
    captures = []
    for step in config['steps']:
        if config['state'][step[0],step[1]] == 1:
            captures.append(step)
        dx = config['start'][0] - step[0]
        dy = config['start'][1] - step[1]
        displacement.append(np.sqrt((dx**2) + (dy**2)))
    return captures, displacement


def build_batch(config):
    raw_walks = {}
    captures = {}
    moves = {}
    configs = []
    ii = 0
    for walk in range(config['n_trials']):
        c = init(config)
        c['steps'] = utils.spawn_random_walk(c['start'], c['n_steps'])
        configs.append(c)
        capt, disp = evaluate_walk(c)
        captures[ii] = len(captures)
        moves[ii] = np.array(disp)
        raw_walks[ii] = c['steps']
        ii += 1
    return captures, moves, raw_walks, configs


def init(config):
    c = config
    c['state'] = build_map(config)
    if config['start'] == []:
        c['start'] = np.array(utils.spawn_random_point(c['initial_state']))
    return c


def build_map(config):
    state = np.zeros((config['width'], config['height']))
    for point in range(config['n_obstacles']):
        pt = utils.spawn_random_point(state)
        state[pt[0],pt[1]] = 1
    return state


t0 = time.time()
config = {'width': 100,
          'height': 100,
          'color': False,
          'n_obstacles': 500,
          'n_steps': 100,
          'n_trials': 000,
          'start': [50, 50],
          'goal': [100, 100],
          'frame_rate': 50}

captures, displaced, walks, configs = build_batch(config)
print '\033[1mFINISHED [' + str(time.time() - t0) + 's] \033[0m'
print 'Min Captures: '+str(np.array(captures.values()).min())
print 'Max Displacement: ' + str(np.array(displaced.values()).max())




# Find the walk with max captures
cmin = np.array(captures.values()).min()
max_capt = []
# Find the walk with max displacement
dmax = np.array(displaced.values()).max()
long_walks = []
for II in range(len(walks.keys())):
    if captures.values()[II] == cmin:
        utils.animate_walk(walks[II], configs[II]['state'], configs[II]['frame_rate'], False, '')
    if np.array((displaced.values()[II])).max() >= dmax:
        long_walks.append(walks[II])
        utils.animate_walk(walks[II], configs[II]['state'], configs[II]['frame_rate'], False, '')
print '-------------------------------------------------'
