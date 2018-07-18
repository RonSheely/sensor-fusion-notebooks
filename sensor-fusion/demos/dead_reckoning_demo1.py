# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed
from matplotlib.pyplot import figure
from .lib.signal_plot import signal_plot2
from .lib.utils import gauss

distributions = ['gaussian', 'uniform']

beliefs = ['uniform sigma = 0.1',
           'uniform sigma = 0.2',
           'uniform sigma = 0.5',           
           'gaussian sigma = 0.1',
           'gaussian sigma = 0.2',
           'gaussian sigma = 0.5']

def pdf(x, muX, sigmaX, distribution):

    if distribution == 'gaussian':
        return gauss(x, muX, sigmaX)
    elif distribution == 'uniform':
        xmin = muX - np.sqrt(12) * sigmaX / 2
        xmax = muX + np.sqrt(12) * sigmaX / 2
        return 1.0 * ((x >= xmin) & (x <= xmax)) / (xmax - xmin)
    raise ValueError('Unknown distribution %s' % distribution)

def pdf_byname(x, muX, name):

    parts = name.split(' ')
    distribution = parts[0]
    sigmaX = float(parts[3])

    return pdf(x, muX, sigmaX, distribution)

def dead_reckoning_demo1_plot(steps=0, v=2, X0=beliefs[0], Wn=beliefs[3]):

    dt = 1
    
    Nx = 801
    x = np.linspace(-10, 40, Nx)
    dx = x[1] - x[0]    
    offset = int(-x[0] / dx)

    Xrange = 1
    sigmaX = Xrange / np.sqrt(12)
    
    muX = 0
    muW = v * dt
    
    fX = pdf_byname(x, muX, X0)

    fW = pdf_byname(x, muW, Wn)

    fig = figure(figsize=(10, 5))
    ax = fig.add_subplot(111)
    ax.grid(True)

    mx = (x < 12) & (x > -2)
    
    for m in range(steps + 1):

        if m > 0:
            fX = np.convolve(fX, fW)[offset:offset + len(x)] * dx

        ax.plot(x[mx], fX[mx], label='%d' % m)

    ax.legend()

def dead_reckoning_demo1():
    interact(dead_reckoning_demo1_plot, steps=(0, 5), v=(0, 5, 0.25),
             X0=beliefs, Wn=beliefs, continuous_update=False)
