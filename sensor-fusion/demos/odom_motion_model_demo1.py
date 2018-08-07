# M. P. Hayes UCECE
import numpy as np
from matplotlib.pyplot import arrow
from ipywidgets import interact, interactive, fixed
from matplotlib.pyplot import figure, show, savefig, rcParams

def wrapto2pi(angle):
    """Convert angle into range [0, 2 * pi)."""

    return angle % (2 * np.pi)


def wraptopi(angle):
    """Convert angle into range [-pi, pi)."""

    return wrapto2pi(angle + np.pi) - np.pi


class Robot(object):

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


def odom_motion_model_demo1_plot(d=1, phi1=0, phi2=0, heading=90, steps=10):

    x = np.zeros(steps + 1)
    y = np.zeros(steps + 1)
    theta = np.zeros(steps + 1)        

    phi1 = np.radians(phi1)
    phi2 = np.radians(phi2)        
    
    robot = Robot(heading=np.radians(heading))

    for m in range(steps + 1):
        x[m] = robot.x
        y[m] = robot.y
        theta[m] = robot.heading        
        robot.transition(d, phi1, phi2, dt=1)

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
    

def odom_motion_model_demo1():
    interact(odom_motion_model_demo1_plot, d=(0, 2, 0.1),
             phi1=(-180, 180, 15),
             phi2=(-180, 180, 15),             
             steps=(1, 10),
             heading=(0, 180, 15), continuous_update=False)
    
