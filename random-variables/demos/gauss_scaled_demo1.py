# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed
from matplotlib.pyplot import show
from .lib.signal_plot import signal_plot2
from .lib.utils import gauss

def gauss_scaled_demo1_plot(muX=0, sigmaX=1, a=1):

    N = 401
    x = np.linspace(-10, 10, N)

    muY = a * muX
    sigmaY = abs(a) * sigmaX
    
    fX = gauss(x, muX, sigmaX)
    fY = gauss(x, muY, sigmaY)

    fXmax = max(fX)
    fYmax = max(fY)    
    
    signal_plot2(x, fX, x, fY, ylim=(0, max(fXmax, fYmax)))
    show()

def gauss_scaled_demo1():
    interact(gauss_scaled_demo1_plot, muX=(-5, 5), sigmaX=(0.01, 5, 0.01),
             a = (0.01, 5, 0.01))
    
    

    

