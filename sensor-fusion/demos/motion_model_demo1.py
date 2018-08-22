# M. P. Hayes UCECE
import numpy as np
from matplotlib.pyplot import arrow
from ipywidgets import interact, interactive, fixed
from matplotlib.pyplot import figure, show, savefig, rcParams
from .lib.robot import robot_draw, Robot

def motion_model_demo1_plot(v=1, omega=0, heading=90, steps=10):

    x = np.zeros(steps + 1)
    y = np.zeros(steps + 1)
    theta = np.zeros(steps + 1)        
    
    robot = Robot(heading=np.radians(heading))

    for m in range(steps + 1):
        x[m] = robot.x
        y[m] = robot.y
        theta[m] = robot.heading        
        robot.transition(v, np.radians(omega), dt=1)

    fig = figure(figsize=(10, 5))
    ax = fig.add_subplot(111)
    ax.set_xlim(-5, 5)
    ax.set_ylim(0, 5)
    ax.grid(True)

    for m in range(len(x)):
        robot_draw(ax, x[m], y[m], theta[m])
    

def motion_model_demo1():
    interact(motion_model_demo1_plot, v=(0, 2, 0.1), omega=(-60, 60, 15),
             steps=(0, 10), heading=(0, 180, 15), continuous_update=False)
    
