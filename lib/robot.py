# Michael P. Hayes UCECE, Copyright 2018--2019

import numpy as np
from matplotlib.pyplot import arrow, Circle, Arrow
from .utils import wraptopi

def robot_draw(ax, x, y, theta, d=0.25, colour='blue', linestyle='-'):

    dx = d * np.cos(theta)
    dy = d * np.sin(theta)

    opt = {'head_width': 0.15, 'head_length': 0.15, 'width': 0.05,
           'length_includes_head': True}
    circle = Circle((x, y), d, color=colour, fill=False, linestyle=linestyle)
    ax.add_artist(circle)
    ax.arrow(x, y, dx, dy, **opt, color=colour)        


class Robot(object):

    def __init__(self, x=0, y=0, heading=np.pi/2):

        self.x = x
        self.y = y
        self.heading = heading

    @property
    def pose(self):
        return self.x, self.y, self.heading
        
    def transition(self, v, omega, dt=0.1):

        from numpy import sin, cos
        
        hp = self.heading

        if omega == 0.0:
            self.x += v * cos(hp) * dt
            self.y += v * sin(hp) * dt
        else:
            self.x += -v / omega * sin(hp) + v / omega * sin(hp + omega * dt)
            self.y += v / omega * cos(hp) - v / omega * cos(hp + omega * dt)
            self.heading = wraptopi(hp + omega * dt)

    def draw(self, ax, colour='blue', linestyle='-'):
        robot_draw(ax, self.x, self.y, self.heading,
                   colour=colour, linestyle=linestyle)
    

class Robot2(object):

    def __init__(self, x=0, y=0, heading=np.pi/2):

        self.x = x
        self.y = y
        self.heading = heading

    def transition(self, d, phi1, phi2, dt=0.1):

        from numpy import sin, cos

        p = self.heading
        self.x += d * np.cos(p + phi1)
        self.y += d * np.sin(p + phi1)
        self.heading = wraptopi(p + phi1 + phi2)

    def robot_draw(self, colour='blue', linestyle='-'):
        robot_draw(ax, self.x, self.y, self.heading,
                   colour=colour, linestyle=linestyle)
            
