# Michael P. Hayes UCECE, Copyright 2018--2019
import numpy as np
from scipy.interpolate import interp1d
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import hist_plot
from .lib.utils import rect, sinc, gauss
from .lib.kde import KDE

distributions = ['uniform', 'gaussian']


def pdf(x, muX, sigmaX, distribution):

    if distribution == 'gaussian':
        return gauss(x, muX, sigmaX)
    elif distribution == 'uniform':
        xmin = muX - np.sqrt(12) * sigmaX / 2
        xmax = muX + np.sqrt(12) * sigmaX / 2
        return 1.0 * ((x >= xmin) & (x <= xmax)) / (xmax - xmin)
    raise ValueError('Unknown distribution %s' % distribution)

def sampling_demo2_plot(distX=distributions[0], muX=0, sigmaX=1, N=1000, seed=1):

    np.random.seed(seed)
    
    Nx = 801
    x = np.linspace(-10, 10, Nx)
    dx = x[1] - x[0]    
    
    fX = pdf(x, muX, sigmaX, distX)    
    FX = np.cumsum(fX) * dx
    
    interp = interp1d(FX, x, kind='linear', bounds_error=False,
                      fill_value=x[-1])

    samples = interp(np.random.rand(N))

    fXest = KDE(samples).estimate(x)

    fig = hist_plot(x, samples, density=True)
    axes = fig.axes
    axes[0].plot(x, fX, label='desired')    
    axes[0].plot(x, fXest, label='estimated')    
    axes[0].set_xlim(-5, 5)
    axes[0].legend()

def sampling_demo2():
    interact(sampling_demo2_plot, distX=distributions,
             muX=(-2, 2), sigmaX=(0.01, 5, 0.01),             
             N=[10, 100, 1000, 10000, 100000, 1000000],
             seed=(1, 100, 1),
             continuous_update=False)
    
