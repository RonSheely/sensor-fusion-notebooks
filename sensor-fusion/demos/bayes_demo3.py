# Michael P. Hayes UCECE, Copyright 2018--2019
import numpy as np
from ipywidgets import interact, interactive, fixed
from matplotlib.pyplot import subplots
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


def bayes_demo3_plot(show_model=True, muX=2, sigmaX=0.5, sigmaV=0.2, z=1,
                     distX=distributions[0],
                     distV=distributions[0]):

    Nx = 801
    x = np.linspace(0, 5, Nx)

    d = 0.5
    a = 5.0 / d

    h = (a * x) * (x <= d) + (a * d**2 / (x + 1e-6)) * (x > d)

    fZgX = pdf(z - h, 0, sigmaV, distV)
    fX = pdf(x, muX, sigmaX, distX)

    fXgZ = fZgX * fX
    eta = np.trapz(fXgZ, x)
    fXgZ /= eta

    if show_model:
        fig, axes = subplots(2, figsize=(10, 5))
        ax1, ax2 = axes

        mx = np.argwhere(abs(h - z) < 0.02)
        print(mx)
        mx = mx[0, :]
        ax1.plot(x[mx], z, 'o')        
        ax1.plot(x, h, color='black')
        
    else:
        fig, ax2 = subplots(1, figsize=(10, 5))
    
    ax2.grid(True)

    ax2.plot(x, fZgX, '--', label='$L_{X|Z}(x|%d)$ likelihood' % z)
    ax2.plot(x, fX, '-.', label='$f_X(x)$ prior')
    ax2.plot(x, fXgZ, '-', label='$f_{X|Z}(x|%d)$ posterior' %z)

    ax2.legend()
    

def bayes_demo3():
    interact(bayes_demo3_plot, muX=(0, 4, 0.2), sigmaX=(0.01, 5, 0.01),
             sigmaV=(0.01, 0.5, 0.01), z=(0, 5, 0.1),
             distX=distributions, distV=distributions)
