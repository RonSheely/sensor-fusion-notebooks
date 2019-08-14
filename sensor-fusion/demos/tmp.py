# M. P. Hayes UCECE
import numpy as np
from matplotlib.pyplot import subplots, arrow
from ipywidgets import interact, interactive, fixed
from matplotlib.pyplot import figure, show, savefig, rcParams

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


def motion_decompose_demo1_plot(x0=0, y0=0, theta0=0, x1=2, y1=0, theta1=15):

    pose0 = (x0, y0, np.radians(theta0))
    pose1 = (x1, y1, np.radians(theta1))    
    
    phi1, d, phi2 = odom_decompose(pose1, pose0)

    v, omega = speeds_decompose(pose1, pose0, 1.0)    

    fig = figure(figsize=(5, 5))
    ax = fig.add_subplot(111)
    ax.axis('equal')
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-2.5, 2.5)
    ax.grid(True)

    opt = {'head_width': 0.4, 'head_length': 0.4, 'width': 0.2,
           'length_includes_head': True}

    dx0 = 0.2 * np.cos(pose0[2])
    dy0 = 0.2 * np.sin(pose0[2]) 
    ax.arrow(pose0[0], pose0[1], dx0, dy0, **opt, color='blue')

    dx1 = 0.2 * np.cos(pose1[2])
    dy1 = 0.2 * np.sin(pose1[2]) 
    ax.arrow(pose1[0], pose1[1], dx1, dy1, **opt, color='blue')        

    if True:
        print('phi1 = %.1f deg, d = %.1f m, phi2 = %.1f deg' %
              (np.degrees(phi1), d, np.degrees(phi2)))
        
        print('v = %.1f m/s, omega = %.1f deg/s' %
              (v, np.degrees(omega)))
    

def motion_decompose_demo1():
    interact(motion_decompose_demo1_plot,
             x0=(-2, 2, 0.1), y0=(-2, 2, 0.1), theta0=(-180, 180, 15),
             x1=(-2, 2, 0.1), y1=(-2, 2, 0.1), theta1=(-180, 180, 15),
             continuous_update=False)
