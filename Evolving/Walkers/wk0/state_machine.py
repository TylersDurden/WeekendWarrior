import matplotlib.animation as animation
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import numpy as np
import utils
import time
import sys


class Transformer:
    state = [[]]
    point = []
    n_collisions = 0

    def __init__(self, config):
        self.initialize(config)
        self.run(config)

    def initialize(self, config):
        self.state = config['map']
        if 'start' not in config.keys():
            self.point = point(utils.spawn_random_point(self.state))
        else:
            self.point = point(config['start'])
        self.state[self.point.x,self.point.y] = 2

    def run(self, config):
        steps = utils.spawn_random_walk([self.point.x,self.point.y],
                                        config['n_steps'])
        if 'show' in config.keys() and config['show']:
            f = plt.figure()
        film = []
        collisions = []
        for step in steps:
            try:
                if self.state[step[0],step[1]] == 1:
                    collisions.append(step)
                    self.n_collisions += 1
                self.state[step[0],step[1]] = 2
                self.state[self.point.x,self.point.y] = 0
                self.point.set_position(step)
            except IndexError:
                pass
            film.append([plt.imshow(self.state, 'gray_r')])
        if 'show' in config.keys() and config['show']:
            a = animation.ArtistAnimation(f,film,config['frame_rate'],True,900)
            plt.show()


class point:
    x = 0
    y = 0
    alive = False

    def __init__(self, position):
        self.x = position[0]
        self.y = position[1]

    def set_alive(self):
        self.alive = True

    def kill(self):
        self.alive = False

    def set_position(self, position):
        self.x = position[0]
        self.y = position[1]


def main():
    styles = ['eater','eager','transformer','healer']
    config = {'width':100,
              'height':100,
              'color':False,
              'style':styles[2],
              'n_obstacles':0,
              'n_steps':100,
              'frame_rate':50,
              'show':False,
              'batch_size':10,
              'map':[[]]}


    if 'reaction_rates' in sys.argv:
        t0 = time.time()
        min_density = 10
        max_density = 1000
        particle_counts = np.arange(min_density,max_density,10)
        n_simulations = 0
        config['map'] = utils.build_map(config['width'],config['height'],config['n_obstacles'])
        collison_counter = {}
        for density in particle_counts:
            config['n_obstacles']  = density
            collisions = []
            for i in range(config['batch_size']):
                t = Transformer(config)
                collisions.append(t.n_collisions)
                n_simulations += 1
            collison_counter[density] = np.array(collisions)
        print '\033[32m:: SIMULATION_CONFIG ::\033[0m'
        for field in config.keys():
            if field != 'map':
                print '\033[35m'+field + '\033[0m: \t\t'+str(config[field])
        print '\033[1mFINISHED \033[31m['+str(time.time()-t0) + 's Elapsed]\033[0m'
        print str(n_simulations) + ' Simulations Total'
        print 'Mean Collisions: \t'+str(np.array(collisions).mean())
        print 'Min Collisions: \t'+str(np.array(collisions).min())
        print 'Max Collisions: \t'+str(np.array(collisions).max())

        f = plt.figure()
        for d in collison_counter.keys():
            plt.plot(collison_counter[d])
if __name__ == '__main__':
    main()
