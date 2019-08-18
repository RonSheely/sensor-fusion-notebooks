# Michael P. Hayes UCECE, Copyright 2018--2019
import numpy as np
from matplotlib.pyplot import subplots, arrow
from ipywidgets import interact, interactive, fixed
from matplotlib.pyplot import subplots
from .lib.robot import robot_draw, Robot
from .lib.pose import Pose


def motion_model(pose0, v, omega, dt):

    x0, y0, theta0 = pose0   
    
    if omega == 0.0:
       x1 = x0 + v * np.cos(theta0) * dt
       y1 = y0 + v * np.sin(theta0) * dt
       theta1 = theta0
    else:
        x1 = x0 - v / omega * np.sin(theta0) + v / omega * np.sin(theta0 + omega * dt)
        y1 = y0 + v / omega * np.cos(theta0) - v / omega * np.cos(theta0 + omega * dt)
        theta1 = theta0 + omega * dt

    return (x1, y1, theta1)


def odom_decompose(pose1, pose0):

    x1, y1, p1 = pose0
    x2, y2, p2 = pose1

    phi1 = np.arctan2(y2 - y1, x2 - x1) - p1
    d = np.sqrt((y2 - y1)**2 + (x2 - x1)**2)
    phi2 = p2 - p1 - phi1

    return phi1, d, phi2


def speeds_decompose(pose1, pose0, dt):

    x1, y1, p1 = pose0
    x2, y2, p2 = pose1    
    omega = (pose1[2] - pose0[2]) / dt

    d = np.sqrt((y2 - y1)**2 + (x2 - x1)**2)    

    if omega == 0:
        v = d / dt
    else:
        v = omega * d / (2 * np.tan(omega * dt / 2))
    return v, omega


def motion_decompose_demo1_plot(x0=0, y0=0, theta0=0, v=2, omega=0):

    dt = 1.0
    pose0 = (x0, y0, np.radians(theta0))
    pose1 = motion_model(pose0, v, np.radians(omega), dt)
    
    phi1, d, phi2 = odom_decompose(pose1, pose0)

    v, omega = speeds_decompose(pose1, pose0, 1.0)    

    fig, ax = subplots(figsize=(10, 5))        
    Pose(0, 0, 0).draw_axes(ax)
    
    ax.axis('equal')
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-2.5, 2.5)
    ax.grid(True)

    robot_draw(ax, pose0[0], pose0[1], pose0[2], colour='blue')
    robot_draw(ax, pose1[0], pose1[1], pose1[2], colour='orange')    
    
    if True:
        print('phi1 = %.1f deg, d = %.1f m, phi2 = %.1f deg' %
              (np.degrees(phi1), d, np.degrees(phi2)))
    

def motion_decompose_demo1():
    interact(motion_decompose_demo1_plot,
             x0=(-2, 2, 0.1), y0=(-2, 2, 0.1), theta0=(-180, 180, 15),
             v=(0, 2, 0.1), omega=(-60, 60, 15),
             continuous_update=False)
