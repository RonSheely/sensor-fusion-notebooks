# Michael P. Hayes UCECE, Copyright 2018--2019
import numpy as np
from matplotlib.pyplot import arrow
from ipywidgets import interact, interactive, fixed
from matplotlib.pyplot import subplots
from .lib.robot import robot_draw, Robot
from .lib.pose import Pose

xmin = -5
xmax = 5
ymin = 0
ymax = 10
tmin = -180
tmax = 180

Nx = 11
Ny = 11

x = np.linspace(xmin, xmax, Nx)
y = np.linspace(ymin, ymax, Ny)


wall1 = ((-1, 5), (0, 5), (1, 5), (1, 4), (1, 3))
walls = (wall1, 1)

beamwidth = 15


def heatmap(ax, x, y, data, fmt='%.1f', skip=[], **kwargs):

    dx = x[1] - x[0]
    dy = y[1] - y[0]

    # These are the corners.
    xc = np.linspace(x[0] - dx / 2, x[-1] + dx / 2, len(x) + 1)
    yc = np.linspace(y[0] - dy / 2, y[-1] + dy / 2, len(y) + 1)    
    
    c = ax.pcolor(xc, yc, data, linewidths=4, vmin=0.0, vmax=1.0,
                  edgecolors=kwargs.pop('edgecolors', 'w'),
                  cmap=kwargs.pop('cmap', 'RdBu'),
                  **kwargs)

    c.update_scalarmappable()

    for p, color, value in zip(c.get_paths(), c.get_facecolors(), c.get_array()):
        x, y = p.vertices[:-2, :].mean(0)
        if np.all(color[:3] > 0.5):
            color = (0.0, 0.0, 0.0)
        else:
            color = (1.0, 1.0, 1.0)

        draw_text = True
        for skip1 in skip:
           xs, ys = skip1
           if abs(x - xs) < 0.1 and abs(y - ys) < 0.1:
               draw_text = False
               break

        if draw_text:
            ax.text(x, y, fmt % value, ha="center", va="center",
                    color=color, **kwargs)


class Ogrid(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.grid = np.ones((Nx, Ny)) * 0.5
        

    def draw(self, axes, skip=[]):

        heatmap(axes, self.x, self.y, self.grid, skip=skip)

ogrid = Ogrid(x, y)

        
def ogrid_demo1_plot(x=3, y=1, heading=90):

    robot = Robot(x, y, heading=np.radians(heading))    

    fig, ax = subplots(figsize=(10, 5))
    ax.axis('tight')
    ogrid.draw(ax, ((robot.x, robot.y), ))
    robot.draw(ax)
    

def ogrid_demo1():
    interact(ogrid_demo1_plot,
             x=(xmin, xmax, 1),
             y=(ymin, ymax, 1),
             heading=(tmin, tmax, 15),              
             continuous_update=False)
    
