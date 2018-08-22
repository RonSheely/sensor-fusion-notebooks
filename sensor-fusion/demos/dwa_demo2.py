# M. P. Hayes UCECE
import numpy as np
from matplotlib.pyplot import arrow, Circle
from ipywidgets import interact, interactive, fixed
from matplotlib.pyplot import figure, show, savefig, rcParams, subplots
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

            
def dwa_demo2_plot(dt=0.5, x=0, y=1, heading=90, v=1, omega=0, speed_goal=1,
                   heading_goal=90, steps=10, obstacle=False):

    v_max = 4
    omega_max = 360
    a_max = 2
    alpha_max = 180
    
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

    obstacles = ((0.5, 3, 0.5, 'purple'), )
    
    extra_v = v_max * 0.05
    extra_w = w_max * 0.05    
    
    fig, axes = subplots(1, 2, figsize=(12, 6))
    xax, vax = axes
    
    vax.set_xlim(w_min - extra_w, w_max + extra_w)
    vax.set_ylim(v_min - extra_v, v_max + extra_v)

    # Region of all possible speeds
    vax.plot((w_min, w_max, w_max, w_min, w_min), (v_min, v_min, v_max, v_max, v_min), 'b-')

    # Region of all achievable speeds
    vax.plot((w1_min, w1_max, w1_max, w1_min, w1_min), (v1_min, v1_min, v1_max, v1_max, v1_min), '-', color='orange')    

    Nv = 9
    Nw = 9

    weights = np.zeros((Nv, Nw))
    
    vv = np.linspace(v1_min, v1_max, Nv)
    ww = np.linspace(w1_min, w1_max, Nw)    

    calc_objective(weights, heading, vv, ww, speed_goal, heading_goal, dt)
    
    p1 = vax.transLimits.transform((w1_min, v1_min))
    p2 = vax.transLimits.transform((w1_max, v1_max))    

    vax.imshow(weights, origin='lower', interpolation=None, aspect='auto',
              extent=(w1_min, w1_max, v1_min, v1_max))


    xax.set_xlim(-2, 2)
    xax.set_ylim(0, 4)
    xax.grid(True)

    if obstacle:
        for obs in obstacles:
            circle = Circle((obs[0], obs[1]), obs[2], color=obs[3], fill=True)
        xax.add_artist(circle)
    
    xv = np.zeros(steps + 1)
    yv = np.zeros(steps + 1)
    thetav = np.zeros(steps + 1)        
    
    robot = Robot(x=x, y=y, heading=np.radians(heading))

    for m in range(steps + 1):
        xv[m] = robot.x
        yv[m] = robot.y
        thetav[m] = robot.heading        
        robot.transition(v, np.radians(omega), dt=dt)

    dx = 0.2 * np.cos(thetav)
    dy = 0.2 * np.sin(thetav)

    opt = {'head_width': 0.4, 'head_length': 0.4, 'width': 0.2,
           'length_includes_head': True}
    for m in range(len(xv)):
        xax.arrow(xv[m], yv[m], dx[m], dy[m], **opt, color='blue')
    
    vax.grid(True)
    

def dwa_demo2():
    interact(dwa_demo2_plot, x=(-4, 4, 0.5), y=(0, 4, 0.5),
             dt=(0.1, 1, 0.1),
             v=(0, 2, 0.1), omega=(-60, 60, 15),
             v_max=(1, 5), omega_max=(90, 360, 15),
             a_max=(0.5, 2, 0.5), alpha_max=(30, 180, 15),
             heading=(0, 180, 15), heading_goal=(0, 180, 15),
             speed_goal=(0, 2, 0.1), steps=(0, 5, 1),
             continuous_update=False)
    
