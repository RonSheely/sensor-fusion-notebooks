# M. P. Hayes UCECE
import numpy as np
from matplotlib.pyplot import arrow
from ipywidgets import interact, interactive, fixed
from matplotlib.pyplot import figure, show, savefig, rcParams
from numpy.random import randn, uniform, seed


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


def particles_motion_model_demo1_plot(Xmin=-1, Xmax=1,
                                      Ymin=0, Ymax=1, Tmin=90,
                                      Tmax=90, Nparticles=10,
                                      v=1, omega=0, steps=0):

    Tmin = np.radians(Tmin)
    Tmax = np.radians(Tmax)    

    opt = {'head_width': 0.4, 'head_length': 0.4, 'width': 0.2,
           'length_includes_head': True}

    seed(1)
    
    robots = []
    for m in range(Nparticles):
        robot = Robot(uniform(Xmin, Xmax), uniform(Ymin, Ymax),
                      uniform(Tmin, Tmax))
        robots.append(robot)


    fig = figure(figsize=(10, 5))
    ax = fig.add_subplot(111)
    ax.set_xlim(-10, 10)
    ax.set_ylim(0, 10)
    ax.grid(True)

    for n in range(steps + 1):
        colour = ['red', 'orange', 'green', 'blue'][n % 4]
        
        for m, robot in enumerate(robots):

            dx = 0.2 * np.cos(robot.heading)
            dy = 0.2 * np.sin(robot.heading)
                
            ax.arrow(robot.x, robot.y, dx, dy, **opt, color=colour)

            robot.transition(v, omega, dt=1)
    

def particles_motion_model_demo1():
    interact(particles_motion_model_demo1_plot,
             v=(0, 2, 0.1), omega=(-2, 2, 0.1),
             Xmin=(-1, 1, 0.1), Xmax=(-1, 1, 0.1),
             Ymin=(-1, 1, 0.1), Ymax=(-1, 1, 0.1),
             Tmin=(-180, 180, 15), Tmax=(-180, 180, 15),
             Nparticles=(10, 100, 10),
             steps=(0, 5),
             continuous_update=False)
    
