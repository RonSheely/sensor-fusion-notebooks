# Michael P. Hayes UCECE, Copyright 2018--2019
import numpy as np
from matplotlib.pyplot import arrow
from ipywidgets import interact, interactive, fixed
from matplotlib.pyplot import subplots
from .lib.robot import robot_draw, Robot
from .lib.pose import Pose

xmin = -10
xmax = 10
ymin = 0
ymax = 10
tmin = -180
tmax = 180

Nx = 21
Ny = 11

x = np.linspace(xmin, xmax, Nx)
y = np.linspace(ymin, ymax, Ny)

beamwidth = 15


class Line(object):

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
    @property
    def A(self):
        return self.p1[1] - self.p2[1]
    
    @property
    def B(self):        
        return self.p2[0] - self.p1[0]
    
    @property
    def C(self):
        return self.p2[0] * self.p1[1] - self.p1[0] * self.p2[1]
    
    def intersection(self, line):
        
        if not isinstance(line, Line):
            line = Line(*line)
            
        D  = self.A * line.B - self.B * line.A
        Dx = self.C * line.B - self.B * line.C
        Dy = self.A * line.C - self.C * line.A
        
        if D == 0:
            return False
        x = Dx / D
        y = Dy / D
        return x, y

class Sonar(object):

    def __init__(self, beamwidth, rmax=20):
        self.beamwidth = beamwidth
        self.rmax = rmax

    def draw_beam(self, axes, pose, walls=None, **kwargs):
        # Ignore walls for now...
    
        xmin, xmax = axes.get_xlim()
        ymin, ymax = axes.get_ylim()
        
        axes.set_xlim(xmin, xmax)
        axes.set_ylim(ymin, ymax)        
        
        xr, yr, hr = pose

        dangle = np.radians(2.5)
        Nrays = int(np.ceil(self.beamwidth / dangle))
        angles = np.linspace(hr - 0.5 * (self.beamwidth - dangle),
                             hr + 0.5 * (self.beamwidth - dangle), Nrays)

        for angle in angles:

            x = xr + np.cos(angle) * self.rmax
            y = yr + np.sin(angle) * self.rmax

            t1 = angle - 0.5 * dangle
            t2 = angle + 0.5 * dangle

            x1 = xr + np.cos(t1) * self.rmax
            x2 = xr + np.cos(t2) * self.rmax
            y1 = yr + np.sin(t1) * self.rmax
            y2 = yr + np.sin(t2) * self.rmax
            
            axes.fill((xr, x1, x2), (yr, y1, y2),
                      alpha=kwargs.pop('alpha', 0.5),
                      color=kwargs.pop('color', 'tab:blue'),
                      **kwargs)

class Wall(object):

    def __init__(self, p1, p2):

        self.x = (p1[0], p2[0])
        self.y = (p1[1], p2[1])

    def draw(self, axes):

        axes.plot(self.x, self.y, 'k')

wall1 = Wall((-1, 8), (4, 8))
wall2 = Wall((4, 8), (4, 6))
walls = (wall1, wall2)
        

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
        self.grid = np.ones((Ny, Nx)) * 0.5
        

    def draw(self, axes, skip=[]):

        heatmap(axes, self.x, self.y, self.grid, skip=skip)

ogrid = Ogrid(x, y)
sonar = Sonar(np.radians(beamwidth))
        
def ogrid_demo1_plot(x=3, y=1, heading=90):

    robot = Robot(x, y, heading=np.radians(heading))    

    fig, ax = subplots(figsize=(10, 5))
    ax.axis('equal')
    ogrid.draw(ax, ((robot.x, robot.y), ))
    robot.draw(ax)
    for wall in walls:
        wall.draw(ax)
    sonar.draw_beam(ax, robot.pose)

def ogrid_demo1():
    interact(ogrid_demo1_plot,
             x=(xmin, xmax, 1),
             y=(ymin, ymax, 1),
             heading=(tmin, tmax, 15),              
             continuous_update=False)
    
