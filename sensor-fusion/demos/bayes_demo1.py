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

def bayes_demo1_plot(muX=0, sigmaX=1, sigmaV=0.5, z=2,
                     prior=distributions[0],
                     likelihood=distributions[0]):

    Nx = 801
    x = np.linspace(-5, 5, Nx)
    dx = x[1] - x[0]    

    fX = pdf(x, muX, sigmaX, prior)
    fV = pdf(x, 0, sigmaV, likelihood)
    fZgX = pdf(x, z, sigmaV, likelihood)

    fXgZ = fZgX * fX
    eta = np.trapz(fXgZ, x)
    fXgZ /= eta

    fig = figure(figsize=(10, 5))
    ax = fig.add_subplot(111)
    ax.grid(True)

    ax.plot(x, fX, ':', label='$f_X$ prior')
    ax.plot(x, fZgX, '--', label='$f_{Z|X}$ likelihood')
    ax.plot(x, fXgZ, '-', label='$f_{X|Z}$ posterior')

    ax.legend()
    

def bayes_demo1():
    interact(bayes_demo1_plot, muX=(-2, 2),
             sigmaX=(0.01, 5, 0.01), sigmaV=(0.01, 5, 0.01),
             prior=distributions, likelihood=distributions)
