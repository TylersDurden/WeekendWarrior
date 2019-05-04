import matplotlib.animation as animation
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import numpy as np
import utility


colors = {'r': [1,0,0],
          'g': [0,1,0],
          'b': [0,0,1],
          'c': [0,1,1],
          'm': [1,0,1],
          'y': [1,1,0]}

k0 = [[1,1,1],[1,0,1],[1,1,1]]
k1 = [[1,1,1,1],[1,0,0,1],[1,0,0,1],[1,1,1,1]]
k2 = [[0,-1,0],[-1,5,-1],[0,-1,0]]


def pulsar(state, depth):
    f = plt.figure()
    sim = []
    dims = np.array(state).shape
    state = np.array(state)
    for ii in range(depth):
        world = ndi.convolve(np.array(state), k0, origin=0)
        state = state.flatten()
        avg = world.mean()
        max = world.max()
        i = 0
        for cell in world.flatten():
            if avg >= cell > 0:
                state[i] = -1
            elif max >= cell > avg:
                state[i] *= -1
            elif cell % 4 == 0:
                state[i] = 1
            if state[i] == 0 and avg <= cell < max:
                state[i] = 1
            i += 1
        state = state.reshape(dims)
        sim.append([plt.imshow(state, 'gray_r')])
    a = animation.ArtistAnimation(f,sim,interval=250,blit=True,repeat_delay=900)
    plt.show()
    return state

# staging
width = 250
height = 250
world = np.zeros((width, height,3))
bz = 10
c = [width/2, height/2]
world = np.random.random_integers(0,12,width*height).reshape((width,height))
world[c[0]-bz:c[0]+bz, c[1]-bz:c[1]+bz] = 1

# pre process and render/simulate
image = pulsar(world, 80)
# eval and evolve

'''
RULE Set 1 (MAZY)
            if avg >= cell > 0:
                state[i] = -1
            elif max >= cell > avg and state[i]==0:
                state[i] *= -1
            elif cell % 5 == 0:
                state[i] = 1
            if state[i] == 1 and avg <= cell < max:
                state[i] = 0
RULE Set 2 (Blotches)
            if avg >= cell > 0:
                state[i] = -1
            elif max >= cell > avg:
                state[i] *= -1
            elif cell % 4 == 0:
                state[i] = 1
            if state[i] == 0 and avg <= cell < max:
                state[i] = 1

'''
