import scipy.ndimage as ndi
import numpy as np
import utility


class Agent:
    x = 0
    y = 0
    state = [[]]

    def __init__(self, xposition, yposition, world):
        self.x = xposition
        self.y = yposition
        self.state = np.array(world)
        self.initialize()

    def initialize(self):
        f = np.array([[1,1,1],[1,0,1],[1,1,1]])
        w0 = ndi.convolve(self.state[:,:,0],f)
        wpt = w0[self.x, self.y]*self.state[self.x,self.y] + w0[self.x,self.y]
        wavg = w0.mean()

