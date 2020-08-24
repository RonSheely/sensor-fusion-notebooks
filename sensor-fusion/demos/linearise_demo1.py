# Michael P. Hayes UCECE, Copyright 2018--2019
import numpy as np
from ipywidgets import interact, interactive, fixed
from .lib.signal_plot import signal_plot

def linearise_demo1_plot(x0=1):

    Nx = 201
    x = np.linspace(0, 10, Nx)

    k1 = 10
    k2 = 1
    
    h = k1 / (k2 + x)

    J = -k1 / (k2 + x0)**2

    h2 = J * (x - x0) + k1 / (k2 + x0)

    fig = signal_plot(x, h)
    ax = fig.axes[0]
    ax.set_xlabel('$x$')    
    ax.plot(x, h2)
    ax.set_ylim(0, k1)
    

def linearise_demo1():
    interact(linearise_demo1_plot, x0=(0, 10))
