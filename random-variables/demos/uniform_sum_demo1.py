# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_plot2

def uniform_sum_demo1_plot(xmin=-1, xmax=1):

    N = 401
    x = np.linspace(-10, 10, N)

    fX1 = 1.0 * ((x >= xmin) & (x <= xmax)) / (xmax - xmin)
    fX2 = 1.0 * ((x >= xmin) & (x <= xmax)) / (xmax - xmin)        

    dx = x[1] - x[0]    
    offset = int(-x[0] / dx)

    fZ = np.convolve(fX, fX)[offset:offset + len(x)] * dx    
    signal_plot2(x, fX, x, fZ)

def uniform_sum_demo1():
    interact(uniform_sum_demo1_plot, xmin=(-5, 5), xmax=(-5, 5), 
             continuous_update=False)
    
    

    

