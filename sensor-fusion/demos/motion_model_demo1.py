# M. P. Hayes UCECE
import numpy as np
from matplotlib.pyplot import arrow
from ipywidgets import interact, interactive, fixed
from matplotlib.pyplot import figure, show, savefig, rcParams


class Robot(object):

    def __init__(self, x=0, y=0, heading=np.pi/2):

        self.x = x
        self.y = y
        self.heading = heading

    def transition(self, v, omega, dt=0.1):

        from numpy import sin, cos
        
        hp = self.heading

        if omega == 0.0:
            self.x += v * cos(hp) * dt
            self.y += v * sin(hp) * dt
        else:
            self.x += -v / omega * sin(hp) + v / omega * sin(hp + omega * dt)
            self.y += v / omega * cos(hp) - v / omega * cos(hp + omega * dt)
            self.heading += omega * dt


def motion_model_demo1_plot(v=1, omega=0, heading=90, steps=10):

    x = np.zeros(steps + 1)
    y = np.zeros(steps + 1)
    theta = np.zeros(steps + 1)        
    
    robot = Robot(heading=np.radians(heading))

    for m in range(steps + 1):
        x[m] = robot.x
        y[m] = robot.y
        theta[m] = robot.heading        
        robot.transition(v, omega, dt=1)

    fig = figure(figsize=(10, 5))
    ax = fig.add_subplot(111)
    ax.set_xlim(-10, 10)
    ax.set_ylim(0, 10)
    ax.grid(True)
    #ax.axis('equal')

    #ax.plot(x, y, 'o')
    
    dx = 0.2 * np.cos(theta)
    dy = 0.2 * np.sin(theta)    

    opt = {'head_width': 0.4, 'head_length': 0.4, 'width': 0.2,
           'length_includes_head': True}
    
    for m in range(len(x)):
        ax.arrow(x[m], y[m], dx[m], dy[m], **opt, color='blue')
    

def motion_model_demo1():
    interact(motion_model_demo1_plot, v=(0, 2, 0.1), omega=(-2, 2, 0.1),
             steps=(0, 10),
             heading=(0, 180, 15), continuous_update=False)
    
