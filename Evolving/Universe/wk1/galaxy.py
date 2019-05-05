import matplotlib.animation as animation
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import numpy as np
import generate
import utility
import time

class cloud:
    width = 0
    height = 0
    state = [[]]

    def __init__(self, x, y, n_particles):
        self.state = np.zeros((x,y,3))
        self.width = x
        self.height = y
        self.initialize(n_particles)


    def initialize(self,n):
        for i in range(n):
            x = np.random.random_integers(0,self.width-1,1)[0]
            y = np.random.random_integers(0,self.height-1,1)[0]
            self.state[x,y,:] = [1,0,0]

def color_classifier(pixel):
    colors = {'r':[1,0,0],'g':[0,1,0],'b':[0,0,1],
              'c':[0,1,1],'m':[1,0,1],'y':[1,1,0],
              'k':[0,0,0],'w':[1,1,1]}
    for k in colors.keys():
        val = colors[k]
        if pixel[0]==pixel[0] and pixel[1]==val[1] and pixel[2]==val[2]:
            return k

''' Create/Initialize Dust Cloud '''
width = 100
height = 100
dust = cloud(width/2,height/2, 50)
world = np.zeros((width, height, 3))
cx = width/2
cy = height/2
padx =  width-dust.state.shape[0]
pady = height - dust.state.shape[1]
world[cx-padx/2:cx+padx/2,cy-pady/2:cy+pady/2,:] = np.array(dust.state)[:,:,:]
# plt.imshow(world)
# plt.show()
''' Let Gravity take hold'''
particles = {'r':[],'g':[],'b':[],
             'c':[],'m':[],'y':[]}
ii = 0
flats = world.flatten()
for particle in flats:
    [y, x] = utility.ind2sub(ii,[width, height])
    if color_classifier(world[y,x,:]) == 'r':
        particles['r'].append([y,x])
    ii += 1
print len(particles)
''' If star, let time progress. If older>thresh: supernova'''
