# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed
from matplotlib.pyplot import figure
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

def likelihood_demo1_plot(sigmaV=0.5, z=2,
                          prior_dist=distributions[0],
                          noise_dist=distributions[0]):

    Nx = 801
    x = np.linspace(-5, 5, Nx)

    fZgX = pdf(x, z, sigmaV, noise_dist)

    fig = figure(figsize=(10, 5))
    ax = fig.add_subplot(111)
    ax.grid(True)

    ax.plot(x, fZgX, '--', label='$f_{Z|X}(%d|x)$ likelihood' % z)

    ax.legend()
    

def likelihood_demo1():
    interact(likelihood_demo1_plot, sigmaV=(0.01, 5, 0.01), z=(-4, 4, 1),
             prior_dist=distributions, noise_dist=distributions)
