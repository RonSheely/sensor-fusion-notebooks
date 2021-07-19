# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed
from matplotlib.pyplot import show
from .lib.signal_plot import signal_plot2
from .lib.utils import gauss

def gauss_scaled_demo1_plot(muX=0, sigmaX=1, a=1, autoscale=False):

    if a == 0:
        a = 1e-3
    
    N = 401
    x = np.linspace(-10, 10, N)

    muY = a * muX
    sigmaY = abs(a) * sigmaX
    
    fX = gauss(x, muX, sigmaX)
    fY = gauss(x, muY, sigmaY)

    ylim = None
    if not autoscale:
        ylim = [0, 0.55]    
    
    signal_plot2(x, fX, x, fY, ylim=ylim)
    show()

def gauss_scaled_demo1():
    interact(gauss_scaled_demo1_plot, muX=(-5, 5), sigmaX=(0.01, 5, 0.01),
             a = (0.0, 5, 0.1))
    
    

    

