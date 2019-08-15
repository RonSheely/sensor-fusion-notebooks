# M. P. Hayes UCECE
import numpy as np
from matplotlib.pyplot import arrow
from ipywidgets import interact, interactive, fixed
from matplotlib.pyplot import subplots
from numpy.random import randn, uniform, seed
from .lib.robot import robot_draw, Robot2
from .lib.pose import Pose

def particles_odom_motion_model_demo1_plot(Xmin=-1, Xmax=1, Ymin=0, Ymax=1,
                                           Tmin=90, Tmax=90, Nparticles=10,
                                           muD=1, sigmaD=0,
                                           muPhi1=0, sigmaPhi1=0,
                                           muPhi2=0, sigmaPhi2=0, 
                                           steps=0):

    Tmin = np.radians(Tmin)
    Tmax = np.radians(Tmax)    

    seed(1)
    
    robots = []
    for m in range(Nparticles):
        robot = Robot2(uniform(Xmin, Xmax), uniform(Ymin, Ymax),
                       uniform(Tmin, Tmax))
        robots.append(robot)


    fig, ax = subplots(figsize=(10, 5))        
    Pose(0, 0, 0).draw_axes(ax)        

    ax.set_xlim(-5, 5)
    ax.set_ylim(0, 5)
    ax.grid(True)

    for n in range(steps + 1):
        colour = ['red', 'orange', 'green', 'blue', 'magenta'][n % 5]
        
        for m, robot in enumerate(robots):
            robot_draw(ax, robot.x, robot.y, robot.heading, colour=colour)
            d = muD + np.random.randn() * sigmaD
            phi1 = muPhi1 + np.random.randn() * sigmaPhi1
            phi2 = muPhi2 + np.random.randn() * sigmaPhi2            
            
            robot.transition(d, np.radians(phi1), np.radians(phi2), dt=1)
    

def particles_odom_motion_model_demo1():
    interact(particles_odom_motion_model_demo1_plot,
             Xmin=(-1, 1, 0.1), Xmax=(-1, 1, 0.1),
             Ymin=(-1, 1, 0.1), Ymax=(-1, 1, 0.1),
             Tmin=(-180, 180, 15), Tmax=(-180, 180, 15),
             Nparticles=(10, 100, 10),
             muD=(0, 2, 0.1), sigmaD=(0, 1, 0.1),
             muPhi1=(-2, 2, 0.1), sigmaPhi1=(0, 10, 1),
             muPhi2=(-2, 2, 0.1), sigmaPhi2=(0, 10, 1),             
             steps=(0, 5),
             continuous_update=False)
    
