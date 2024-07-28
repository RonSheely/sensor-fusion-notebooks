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

    m1 = x < d
    m2 = x >= d

    x1 = np.interp(z, h[m1], x[m1])
    # Can only interpolate a monotonic function, so
    # invert values to achieve a monotonic function.
    x2 = np.interp(1 / z, 1 / h[m2], x[m2])

    if show_model:
        fig, axes = subplots(2, figsize=(10, 5))
        ax1, ax2 = axes

        axes[0].plot(x, h, color='C0', label='$h(x)$')
        axes[0].plot(x1, z, 'o', color='C0')
        axes[0].plot(x2, z, 'o', color='C0')
        axes[0].grid(True)
        axes[0].set_ylabel('$z$')

    else:
        fig, ax2 = subplots(1, figsize=(10, 5))

    ax2.grid(True)

    ax2.plot(x, fZgX, '--', label='$L(x|%d)$ likelihood' % z)
    ax2.plot(x, fX, '-.', label='$f_X(x)$ prior')
    ax2.plot(x, fXgZ, '-', label='$f_{X|Z}(x|%d)$ posterior' % z)

    ax2.legend()


def bayes_demo3():
    interact(bayes_demo3_plot, muX=(0, 4, 0.2), sigmaX=(0.01, 5, 0.01),
             sigmaV=(0.01, 0.5, 0.01), z=(0, 5, 0.1),
             distX=distributions, distV=distributions)
