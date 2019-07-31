# M. P. Hayes UCECE
import numpy as np
from matplotlib.pyplot import show
from scipy.interpolate import interp1d
from ipywidgets import interact, interactive, fixed, interact
from IPython.display import display
from .lib.signal_plot import hist_plot
from .lib.utils import rect, sinc, gauss

distributions = ['gaussian', 'uniform']


def pdf(x, muX, sigmaX, distribution):

    if distribution == 'gaussian':
        return gauss(x, muX, sigmaX)
    elif distribution == 'uniform':
        xmin = muX - np.sqrt(12) * sigmaX / 2
        xmax = muX + np.sqrt(12) * sigmaX / 2
        return 1.0 * ((x >= xmin) & (x <= xmax)) / (xmax - xmin)
    raise ValueError('Unknown distribution %s' % distribution)

def sampling_demo0_plot(distX=distributions[0], muX=0, sigmaX=1,
                        seed=1, N=2, show_pdf=False):

    Nx = 801
    x = np.linspace(-10, 10, Nx)
    dx = x[1] - x[0]    
    
    fX = pdf(x, muX, sigmaX, distX)    
    FX = np.cumsum(fX) * dx

    np.random.seed(seed)
    
    interp = interp1d(FX, x, kind='linear', bounds_error=False,
                      fill_value=x[-1])

    samples = interp(np.random.rand(N))
    values = ','.join(['%.1f' % sample for sample in samples])

    display(values)
    display('est muX = %.1f  est sigmaX = %.1f' % (np.mean(samples),
                                                   np.std(samples)))

    if show_pdf:
        fig = hist_plot(x, samples, density=True)
        axes = fig.axes    
        axes[0].plot(x, fX, label='desired')
        axes[0].set_xlim(-5, 5)    

def sampling_demo0():
    interact(sampling_demo0_plot, distX=distributions,
             muX=(-2, 2), sigmaX=(0.01, 5, 0.01), seed=(1, 100, 1),
             N=(1, 20, 1),  continuous_update=False)
    
