# Michael P. Hayes UCECE, Copyright 2018--2019
import numpy as np
from matplotlib.pyplot import arrow
from matplotlib.gridspec import GridSpec
from ipywidgets import interact, interactive, fixed
from matplotlib.pyplot import figure
from numpy.random import randn, uniform, seed
from .lib.robot import robot_draw, Robot2
from .lib.pose import Pose
from .lib.utils import gauss

def particles_odom_motion_model_demo1_plot(Xmin=-1, Xmax=1, Ymin=0, Ymax=1,
                                           Thetamin=90, ThetaMax=90, Nparticles=10,
                                           muD=1, sigmaD=0,
                                           muPhi1=0, sigmaPhi1=0,
                                           muPhi2=0, sigmaPhi2=0, 
                                           steps=0):

    Thetamin = np.radians(Thetamin)
    ThetaMax = np.radians(ThetaMax)    

    seed(1)
    
    robots = []
    for m in range(Nparticles):
        robot = Robot2(uniform(Xmin, Xmax), uniform(Ymin, Ymax),
                       uniform(Thetamin, ThetaMax))
        robots.append(robot)

    fig = figure(figsize=(12, 5))                
    gs = GridSpec(8, 4)
    ax1 = fig.add_subplot(gs[0:8,0:3])
    ax2 = fig.add_subplot(gs[0:2, 3])
    ax3 = fig.add_subplot(gs[3:5, 3])
    ax4 = fig.add_subplot(gs[6:8, 3])        

    Pose(0, 0, 0).draw_axes(ax1)        

    ax1.set_xlim(-5, 5)
    ax1.set_ylim(0, 5)
    ax1.grid(True)

    for n in range(steps + 1):
        colour = ['red', 'orange', 'green', 'blue', 'magenta'][n % 5]
        
        for m, robot in enumerate(robots):
            robot_draw(ax1, robot.x, robot.y, robot.heading, colour=colour)
            d = muD + np.random.randn() * sigmaD
            phi1 = muPhi1 + np.random.randn() * sigmaPhi1
            phi2 = muPhi2 + np.random.randn() * sigmaPhi2            
            
            robot.transition(d, np.radians(phi1), np.radians(phi2), dt=1)

    d = np.linspace(-5, 5, 100)
    ax2.plot(d, gauss(d, muD, sigmaD + 1e-12))
    ax2.set_xlabel('$d$')
    ax2.set_ylabel('$f_D(d)$')    
    ax2.set_yticks([])    

    phi1 = np.linspace(-20, 20, 100)
    ax3.plot(phi1, gauss(phi1, muPhi1, sigmaPhi1 + 1e-12))
    ax3.set_xlabel('$\phi_1$')
    ax3.set_ylabel('$f_{\Phi_1}(\phi)$')        
    ax3.set_yticks([])

    phi2 = np.linspace(-20, 20, 100)
    ax4.plot(phi2, gauss(phi2, muPhi2, sigmaPhi2 + 1e-12))
    ax4.set_xlabel('$\phi_2$')
    ax4.set_ylabel('$f_{\Phi_2}(\phi)$')        
    ax4.set_yticks([])    
            

def particles_odom_motion_model_demo1():
    interact(particles_odom_motion_model_demo1_plot,
             Xmin=(-1, 1, 0.1), Xmax=(-1, 1, 0.1),
             Ymin=(-1, 1, 0.1), Ymax=(-1, 1, 0.1),
             Phimin=(-180, 180, 15), PhiMax=(-180, 180, 15),
             Nparticles=(10, 100, 10),
             muD=(0, 2, 0.1), sigmaD=(0.1, 1, 0.1),
             muPhi1=(-2, 2, 0.1), sigmaPhi1=(1, 10, 1),
             muPhi2=(-2, 2, 0.1), sigmaPhi2=(1, 10, 1),             
             steps=(0, 5),
             continuous_update=False)
    
