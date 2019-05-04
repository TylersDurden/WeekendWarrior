import matplotlib.animation as animation
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import numpy as np
import utility
import rgb

k0 = [[1,1,1],[1,0,1],[1,0,1]]
k1 = [[1,1,1,1],[1,0,0,1],[1,0,0,1],[1,1,1,1]]

def initialize_configuration(config):
    state = np.zeros((config['width'], config['height'], 3))
    test = np.zeros((config['width'], config['height']))
    for reds in range(config['nred']):
        [rx,ry] = utility.spawn_random_point(test)
        state[rx,ry,:] = [1,0,0]
    for blus in range(config['nblue']):
        [bx,by] = utility.spawn_random_point(test)
        state[bx,by,:] = [0,0,1]
    for grns in range(config['ngreen']):
        [gx,gy] = utility.spawn_random_point(test)
        state[gx,gy,:] = [0,1,0]
    if config['show_init']:
        plt.imshow(state)
        plt.show()
    return state


def color_automata(state, config):
    f = plt.figure()
    simulation = []
    dims = state.shape
    for gen in range(config['ngenerations']):
        # Process RED
        rworld = np.array(state[:,:,0])
        rdecay = ndi.convolve(rworld,k1).flatten()
        rflat = rworld.flatten()
        ract = config['ract']
        ri = 0
        for rcell in ndi.convolve(rworld,k0).flatten():
            if rcell >= ract and rflat[ri]==0:
                rflat[ri] = 1
            if rflat[ri]==1 and rdecay[ri] % ract-1 ==0:
                rflat[ri] = 0
            ri += 1
        state[:,:,0] = rflat.reshape(rworld.shape)
        # Process GREEN
        gact =  config['gact']
        gworld = np.array(state[:,:,1])
        gdecay = ndi.convolve(gworld,k1).flatten()
        gflat = gworld.flatten()
        gact = config['gact']
        gi = 0
        for gcell in ndi.convolve(gworld,k0).flatten():
            if gcell >= gact and gflat[gi]==0:
                gflat[gi] = 1
            if gflat[gi]==1 and gdecay[gi] % gact-1 == 0:
                gflat[gi] = 0
            gi += 1
        state[:,:,1] = gflat.reshape(gworld.shape)
        # Process BLUE
        bact = config['bact']
        bworld = np.array(state[:,:,2])
        bdecay = ndi.convolve(bworld,k1).flatten()
        bflat = bworld.flatten()
        bact = config['bact']
        bi = 0
        for bcell in ndi.convolve(bworld, k0).flatten():
            if bcell >= bact and bflat[bi]==0:
                bflat[bi] = 1
            if bflat[bi]==1 and bdecay[bi] % bact-1 ==0:
                bflat[bi] = 0
            bi += 1
        state[:,:,2] = bflat.reshape(bworld.shape)
        simulation.append([plt.imshow(state)])
    a = animation.ArtistAnimation(f, simulation, interval=60,blit=True,repeat_delay=900)
    plt.show()


config = {'nred':550,
          'ngreen':550,
          'nblue':550,
          'width':100,
          'height':100,
          'ngenerations':20,
          'ract':3,'gact':3,'bact':3, # Activation Points
          'show_init':False}
initial_state = initialize_configuration(config)
color_automata(initial_state, config)
