# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed
from matplotlib.pyplot import subplots
from .lib.utils import gauss

def likelihood_demo3_plot(sigmaV=0.2, z=2):

    Nx = 801
    x = np.linspace(0, 5, Nx)

    d = 0.5
    a = 5.0 / d

    h = (a * x) * (x <= d) + (a * d**2 / (x + 1e-6)) * (x > d)

    fZgX = gauss(z - h, 0, sigmaV)

    fig, axes = subplots(2, figsize=(10, 5))

    axes[0].plot(x, h, color='orange', label='$h(x)$')
    axes[0].grid(True)
    axes[0].set_xlabel('$x$')
    axes[0].set_ylabel('$h(x)$')
    axes[0].legend()    
    
    axes[1].grid(True)
    axes[1].plot(x, fZgX, '--', label='$f_{Z|X}(%d|x)$ likelihood' % z)
    axes[1].set_xlabel('$x$')

    axes[1].legend()
    

def likelihood_demo3():
    interact(likelihood_demo3_plot, sigmaV=(0.01, 0.5, 0.01), z=(0, 5, 0.1))
    

