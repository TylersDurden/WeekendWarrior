import matplotlib.animation as animation
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import numpy as np
import generate
import utility
import time

k0 = [[1,1,1],[1,1,1],[1,1,1]]
k1 = [[1,1,1,1],[1,0,0,1],[1,0,0,1],[1,1,1,1]]


def process(state, config):
    f = plt.figure()
    ngen = config['ngenerations']
    film = []
    for gen in range(ngen):
        rworld = ndi.convolve(state[:,:,0], k0).flatten()
        bworld = ndi.convolve(state[:,:,2], k0).flatten()
        ri = 0
        bi = 0
        for rcell in rworld:
            bcell = bworld[ri]
            if rcell >= 4 and rworld[ri]==1:
                rworld[ri] = 1
            if bcell <= 2 and bworld[ri]==1:
                bworld[ri] = 1
            ri += 1
        state[:,:,0] = rworld.reshape((config['width'], config['height']))
        state[:,:,1] = bworld.reshape((config['width'], config['height']))
        film.append([plt.imshow(state)])
    a = animation.ArtistAnimation(f,film,interval=50,blit=True,repeat_delay=900)
    plt.show()


t0 = time.time()
config = {'width':150, 'height':150,
          'nred':100, 'nblue':120,'ngreen':0,
          'ngenerations':10,'show_init':False}
state = generate.initialize_configuration(config)
process(state,config)
print 'Finished ['+str(time.time()-t0)+'s Elapsed]'
