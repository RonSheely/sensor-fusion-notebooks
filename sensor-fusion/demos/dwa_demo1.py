# M. P. Hayes UCECE
import numpy as np
from matplotlib.pyplot import arrow
from ipywidgets import interact, interactive, fixed
from matplotlib.pyplot import figure, show, savefig, rcParams
from matplotlib.ticker import NullFormatter
from .lib.utils import wraptopi, angle_difference

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
            self.heading = wraptopi(hp + omega * dt)

def objective(speed, speed_goal, heading, heading_goal):

    w1 = np.exp(-abs(speed - speed_goal) / 1.0)
    w2 = np.exp(-abs(angle_difference(heading, heading_goal)) / np.radians(30))
    return w1 * w2
            
def calc_objective(weights, heading, vv, ww, speed_goal, heading_goal, dt):

    ww = np.radians(ww)
    heading = np.radians(heading)
    heading_goal = np.radians(heading_goal)    
    
    for m, w in enumerate(ww):
        for n, v in enumerate(vv):
            robot = Robot(0, 0, heading)
            robot.transition(v, w, dt)
            weights[n, m] = objective(v, speed_goal,
                                      robot.heading, heading_goal)

            
def dwa_demo1_plot(dt=1, v_max=4, omega_max=360, a_max=1, alpha_max=60, v=1,
                   omega=0, heading=90, speed_goal=1, heading_goal=90):

    w = omega
    w_max = omega_max
    
    v_min = -v_max
    w_min = -w_max
    
    v1_max = v + a_max * dt
    v1_min = v - a_max * dt
    w1_max = w + alpha_max * dt
    w1_min = w - alpha_max * dt        
    
    v1_min = max(v_min, v1_min)
    v1_max = min(v_max, v1_max)
    w1_min = max(w_min, w1_min)
    w1_max = min(w_max, w1_max)

    extra = 0.2
    
    fig = figure(figsize=(10, 5))
    ax = fig.add_subplot(111)
    ax.set_xlim(w_min - extra, w_max + extra)
    ax.set_ylim(v_min - extra, v_max + extra)

    # Region of all possible speeds
    ax.plot((w_min, w_max, w_max, w_min, w_min), (v_min, v_min, v_max, v_max, v_min), 'b-')

    # Region of all achievable speeds
    ax.plot((w1_min, w1_max, w1_max, w1_min, w1_min), (v1_min, v1_min, v1_max, v1_max, v1_min), '-', color='orange')    

    Nv = 9
    Nw = 9

    weights = np.zeros((Nv, Nw))
    
    vv = np.linspace(v1_min, v1_max, Nv)
    ww = np.linspace(w1_min, w1_max, Nw)    

    calc_objective(weights, heading, vv, ww, speed_goal, heading_goal, dt)
    
    p1 = ax.transLimits.transform((w1_min, v1_min))
    p2 = ax.transLimits.transform((w1_max, v1_max))    

    if False:
        rect_im = [p1[0], p1[1], p2[0] - p1[0], p2[1] - p1[1]]
        im_ax = fig.add_axes(rect_im)
        im_ax.imshow(weights, origin='lower', interpolation=None, aspect='auto')
        im_ax.xaxis.set_major_formatter(NullFormatter())
        im_ax.yaxis.set_major_formatter(NullFormatter())
        im_ax.set_xticks([])
        im_ax.set_yticks([])
        im_ax.axis('tight')
    else:
        ax.imshow(weights, origin='lower', interpolation=None, aspect='auto',
                  extent=(w1_min, w1_max, v1_min, v1_max))

    ax.grid(True)
    

def dwa_demo1():
    interact(dwa_demo1_plot, dt=(0.1, 1, 0.1),
             v=(0, 2, 0.1), omega=(-60, 60, 15),
             steps=(0, 10), v_max=(1, 5), omega_max=(90, 360, 15),
             a_max=(0.5, 2, 0.5), alpha_max=(30, 180, 15),
             heading=(0, 180, 15), heading_goal=(0, 180, 15),
             speed_goal=(0, 2, 0.1), continuous_update=False)
