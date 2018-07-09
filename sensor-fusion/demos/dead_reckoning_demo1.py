# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed, interact
from matplotlib.pyplot import figure
from .lib.signal_plot import signal_plot2
from .lib.utils import gauss

distributions = ['gaussian', 'uniform']

def pdf(x, muX, sigmaX, distribution):

    if distribution == 'gaussian':
        return gauss(x, muX, sigmaX)
    elif distribution == 'uniform':
        xmin = muX - np.sqrt(12) * sigmaX / 2
        xmax = muX + np.sqrt(12) * sigmaX / 2
        return 1.0 * ((x >= xmin) & (x <= xmax)) / (xmax - xmin)
    raise ValueError('Unknown distribution %s' % distribution)

def dead_reckoning_demo1_plot(steps=5, v=2, sigmaW=0.2):

    dt = 1
    
    Nx = 801
    x = np.linspace(-10, 40, Nx)
    dx = x[1] - x[0]    
    offset = int(-x[0] / dx)

    muX = 0
    sigmaX = 1
    muW = v * dt
    
    fX = pdf(x, muX, sigmaX, 'uniform')

    fW = pdf(x, muW, sigmaW, 'gaussian')    

    fig = figure(figsize=(10, 5))
    ax = fig.add_subplot(111)
    ax.grid(True)

    mx = (x < 20) & (x > -2)
    
    for m in range(steps):

        if m > 0:
            fX = np.convolve(fX, fW)[offset:offset + len(x)] * dx

        ax.plot(x[mx], fX[mx], label='%d' % m)

    ax.legend()

def dead_reckoning_demo1():
    interact(dead_reckoning_demo1_plot, steps=(1, 20), v=(0, 5, 0.25),
             sigmaW=(0.01, 1, 0.01),
             continuous_update=False)
    
    

    

