# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed
from .lib.signal_plot import signal_plot
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

def rv_sum_demo1_plot(muX=0, sigmaX=1, N=5, distribution=distributions[1]):

    Nx = 801
    x = np.linspace(-50, 50, Nx)
    dx = x[1] - x[0]    
    offset = int(-x[0] / dx) + 1
    
    fZ = pdf(x, muX, sigmaX, distribution)
    for n in range(1, N):
        fX = pdf(x, muX, sigmaX, distribution)
        fZ = np.convolve(fZ, fX)[offset:offset + len(x)] * dx

    mx = (x < 20) & (x > -20)
        
    signal_plot(x[mx], fZ[mx])

def rv_sum_demo1():
    interact(rv_sum_demo1_plot, muX=(-2, 2), sigmaX=(0.01, 5, 0.01),
             distribution=distributions, N=(1, 100))
