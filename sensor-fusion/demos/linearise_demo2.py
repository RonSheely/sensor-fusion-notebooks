# Michael P. Hayes UCECE, Copyright 2018--2019
import numpy as np
from ipywidgets import interact, interactive, fixed
from .lib.signal_plot import signal_plot

def linearise_demo2_plot(x0=1):

    Nx = 201
    x = np.linspace(0, 10, Nx)

    a = 1
    b = -9
    c = 27
    d = 100

    h = a * x**3 + b * x**2 + c * x + d
    
    J = 3 * a * x0**2 + 2 * b * x0 + c
    u = a * x0**3 + b * x0**2 + c * x0 + d    
    h2 = (x - x0) * J + u

    fig = signal_plot(x, h)
    ax = fig.axes[0]
    ax.set_xlabel('$x$')
    ax.plot(x, h2)
    ax.set_ylim(0, max(max(h), max(h2)))
    

def linearise_demo2():
    interact(linearise_demo2_plot, x0=(0, 10))
