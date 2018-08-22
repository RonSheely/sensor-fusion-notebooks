# M. P. Hayes UCECE
import numpy as np
from matplotlib.pyplot import arrow
from ipywidgets import interact, interactive, fixed
from matplotlib.pyplot import figure, show, savefig, rcParams
from numpy.random import randn, uniform, seed
from .lib.robot import robot_draw, Robot

def particles_motion_model_demo1_plot(Xmin=-1, Xmax=1,
                                      Ymin=0, Ymax=1, Tmin=90,
                                      Tmax=90, Nparticles=10,
                                      v=1, omega=0, steps=0):

    Tmin = np.radians(Tmin)
    Tmax = np.radians(Tmax)    

    seed(1)
    
    robots = []
    for m in range(Nparticles):
        robot = Robot(uniform(Xmin, Xmax), uniform(Ymin, Ymax),
                      uniform(Tmin, Tmax))
        robots.append(robot)


    fig = figure(figsize=(10, 5))
    ax = fig.add_subplot(111)
    ax.set_xlim(-5, 5)
    ax.set_ylim(0, 5)
    ax.grid(True)

    for n in range(steps + 1):
        colour = ['red', 'orange', 'green', 'blue', 'magenta'][n % 5]
        
        for m, robot in enumerate(robots):
            robot_draw(ax, robot.x, robot.y, robot.heading, colour=colour)
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
    
