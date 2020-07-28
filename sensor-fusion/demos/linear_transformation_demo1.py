# Michael P. Hayes UCECE, Copyright 2018--2019
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

def linear_transformation_demo1_plot(muX=0, sigmaX=1, c=1, d=0, distribution=distributions[1]):

    Nx = 801
    x = np.linspace(-10, 10, Nx)
    dx = x[1] - x[0]    
    offset = int(-x[0] / dx)

    fX = pdf(x, muX, sigmaX, distribution)
    fZ = pdf(x, c * muX + d, c * sigmaX, distribution)
    signal_plot(x, fZ)

def linear_transformation_demo1():
    interact(linear_transformation_demo1_plot, muX=(-2, 2), sigmaX=(0.01, 5, 0.01),
             c=(0.5, 5, 0.5), d=(-5, 5, 1),
             distribution=distributions)
