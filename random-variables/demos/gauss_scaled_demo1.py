# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_plot2
from .lib.utils import gauss

def gauss_scaled_demo1_plot(muX=0, sigmaX=1, a=1):

    N = 401
    x = np.linspace(-10, 10, N)

    muY = a * muX
    sigmaY = abs(a) * sigmaX
    
    fX = gauss(x, muX, sigmaX)
    fY = gauss(x, muY, sigmaY)
    
    signal_plot2(x, fX, x, fY)

def gauss_scaled_demo1():
    interact(gauss_scaled_demo1_plot, muX=(-5, 5), sigmaX=(0.01, 5, 0.01),
             a = (0.01, 5, 0.01),
             continuous_update=False)
    
    

    

