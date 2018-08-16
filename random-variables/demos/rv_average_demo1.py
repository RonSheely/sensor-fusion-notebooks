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
        u = 1.0 * ((x >= xmin) & (x <= xmax))
        u /= np.trapz(u, x)
        return u        
    raise ValueError('Unknown distribution %s' % distribution)

def rv_average_demo1_plot(muX=0, sigmaX=1, N=5, distribution=distributions[1]):

    Nx = 201
    x = np.linspace(-5, 5, Nx)
    dx = x[1] - x[0]    

    fX = pdf(x, muX, sigmaX, distribution)
    fZ = fX
    for n in range(1, N):
        fZ = np.convolve(fZ, fX) * dx

    fZ = fZ[::N] * N
        
    fG = gauss(x, muX / N, sigmaX / np.sqrt(N))
        
    mx = (x < 5) & (x > -5)
        
    fig = signal_plot(x[mx], fZ[mx])
    fig.axes[0].plot(x[mx], fG[mx], '--')

def rv_average_demo1():
    interact(rv_average_demo1_plot, muX=(-2, 2), sigmaX=(0.01, 5, 0.01),
             distribution=distributions, N=(1, 100))
