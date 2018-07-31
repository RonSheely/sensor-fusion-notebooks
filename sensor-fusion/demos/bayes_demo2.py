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

def bayes_demo2_plot(muX=1, sigmaX=1, z=2, a=0.3,
                     distX=distributions[0],
                     distV=distributions[0]):

    Nx = 801
    x = np.linspace(-5, 5, Nx)

    sigmaV = a * abs(x) + 0.1
    
    fX = pdf(x, muX, sigmaX, distX)
    fV = pdf(x, 0, sigmaV, distV)
    fZgX = pdf(x, z, sigmaV, distV)

    fXgZ = fZgX * fX
    eta = np.trapz(fXgZ, x)
    fXgZ /= eta

    fig = figure(figsize=(10, 5))
    ax = fig.add_subplot(111)
    ax.grid(True)

    ax.plot(x, fZgX, '--', label='$f_{Z|X}(%d|x)$ likelihood' % z)
    ax.plot(x, fX, '-.', label='$f_X(x)$ prior')
    ax.plot(x, fXgZ, '-', label='$f_{X|Z}(x|%d)$ posterior' %z)

    ax.legend()
    

def bayes_demo2():
    interact(bayes_demo2_plot, muX=(0, 4, 0.2), a=(0.1, 1, 0.1),
             sigmaX=(0.01, 5, 0.01),
             z=(-4, 4, 1),
             distX=distributions, distV=distributions)
