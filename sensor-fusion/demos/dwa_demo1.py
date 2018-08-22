# M. P. Hayes UCECE
import numpy as np
from matplotlib.pyplot import arrow
from ipywidgets import interact, interactive, fixed
from matplotlib.pyplot import figure, show, savefig, rcParams
from matplotlib.ticker import NullFormatter

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


def dwa_demo1_plot(v_max=4, omega_max=4, a_max=1, alpha_max=1, v=1,
                   omega=0, heading=90, speed_goal=1, heading_goal=15):

    w = omega
    w_max = omega_max
    
    dt = 1
    dv = 0.1
    dw = 0.1

    extra = 0.2

    Nv = 2 * (v_max + extra) / dv + 10
    Nw = 2 * (w_max + extra) / dw + 10    
    
    vv = np.arange(-Nv // 2, Nv // 2) / Nv * dv
    ww = np.arange(-Nw // 2, Nw // 2) / Nw * dw

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

    weights = np.zeros((int((v1_max - v1_min) / dv),
                        int((w1_max - w1_min) / dw)))

    
    fig = figure(figsize=(10, 5))
    ax = fig.add_subplot(111)
    ax.set_xlim(w_min - extra, w_max + extra)
    ax.set_ylim(v_min - extra, v_max + extra)

    # Region of all possible speeds
    ax.plot((w_min, w_max, w_max, w_min, w_min), (v_min, v_min, v_max, v_max, v_min), 'b-')

    # Region of all achievable speeds
    ax.plot((w1_min, w1_max, w1_max, w1_min, w1_min), (v1_min, v1_min, v1_max, v1_max, v1_min), '-', color='orange')    

    p1 = ax.transLimits.transform((w1_min, v1_min))
    p2 = ax.transLimits.transform((w1_max, v1_max))    

    rect_im = [p1[0], p1[1], p2[0] - p1[0], p2[1] - p1[1]]
    im_ax = fig.add_axes(rect_im)
    im_ax.imshow(weights, origin='lower')
    im_ax.xaxis.set_major_formatter(NullFormatter())
    im_ax.yaxis.set_major_formatter(NullFormatter())
    im_ax.set_xticks([])
    im_ax.set_yticks([])
    im_ax.axis('tight')
    
    ax.grid(True)
    

def dwa_demo1():
    interact(dwa_demo1_plot, v=(0, 2, 0.1), omega=(-60, 60, 15),
             steps=(0, 10), v_max=(1, 5), omega_max=(1, 5),
             a_max=(0.5, 2, 0.5), alpha_max=(0.5, 2, 0.5),
             heading=(0, 180, 15), continuous_update=False)
    
