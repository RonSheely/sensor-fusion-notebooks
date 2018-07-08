# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_plot3
from .lib.utils import gauss

def rv_sum_demo1_plot(muX=0, sigmaX=1, muY=1, sigmaY=1):

    N = 401
    x = np.linspace(-10, 10, N)

    fX = gauss(x, muX, sigmaX)
    fY = gauss(x, muY, sigmaY)

    muZ = muX + muY
    sigmaZ = np.sqrt(sigmaX**2 + sigmaY**2)
    
    fZ = gauss(x, muZ, sigmaZ)        

    signal_plot3(x, fX, x, fY, x, fZ)

def rv_sum_demo1():
    interact(rv_sum_demo1_plot, muX=(-2, 2), muY=(-2, 2),
             sigmaX=(-5, 5), sigmaY=(-5, 5),
             continuous_update=False)
    
    

    

