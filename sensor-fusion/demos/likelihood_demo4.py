# M. P. Hayes UCECE
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

def likelihood_demo4_plot(sigmaV=0.5, z=2,
                          distV=distributions[0], condpdf=True):

    Nx = 801
    x = np.linspace(0.2, 5, Nx)

    h = 1 / x

    fZgX = pdf(z - h, 0, sigmaV, distV)    

    # Can only interpolate a monotonic function, so
    # invert values to achieve a monotonic function.
    x1 = np.interp(1 / z, 1 / h, x)    
    
    fig, axes = subplots(2 + condpdf * 1, figsize=(10, 5))
    fig.tight_layout()

    axes[0].plot(x, h, color='orange', label='$h(x) = 1/x$')
    axes[0].plot(x1, z, 'o', color='orange')
    axes[0].grid(True)
    axes[0].set_xlabel('$x$')
    axes[0].set_ylabel('$z$')
    axes[0].legend()    

    axes[1].plot(x, fZgX, '--', label='$l_{X|Z}(x|%.1f)$' % z)
    axes[1].set_xlabel('$x$')    
    axes[1].legend()

    if condpdf:
        zv = np.linspace(0, 5, 201)
        
        X, Z = np.meshgrid(x, zv)
        H = 1 / X
        foo = pdf(Z - H, 0, sigmaV, distV)    
        
        axes[2].imshow(foo, origin='lower', extent=(x[0], x[-1], zv[0], zv[-1]))
        axes[2].axis('tight')
        axes[2].set_xlabel('$x$')
        axes[2].set_ylabel('$z$')        

def likelihood_demo4():
    interact(likelihood_demo4_plot, sigmaV=(0.01, 5, 0.01), z=(0, 5, 0.2),
             distV=distributions)
