# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed
from matplotlib.pyplot import show
from .lib.signal_plot import signal_plot
from .lib.utils import gauss

def gauss_demo1_plot(muX=0, sigmaX=1):

    N = 401
    x = np.linspace(-10, 10, N)

    fX = gauss(x, muX, sigmaX)
    signal_plot(x, fX)
    show()    

def gauss_demo1():
    interact(gauss_demo1_plot, muX=(-5, 5), sigmaX=(0.01, 5, 0.01))

    
    

    

