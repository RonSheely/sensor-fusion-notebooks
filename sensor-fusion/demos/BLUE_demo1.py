# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_plot3
from .lib.utils import gauss

def BLUE_demo1_plot(w1=0.5, w2=0.5):

    muX1 = 0
    muX2 = 0
    sigmaX1 = 1
    sigmaX2 = 2

    muX = w1 * muX1 + w2 * muX2
    sigmaX = np.sqrt(w1**2 * sigmaX1**2 + w2**2 * sigmaX2**2)    
    
    N = 401
    x = np.linspace(-10, 10, N)

    fX1 = gauss(x, muX1, sigmaX1)
    fX2 = gauss(x, muX2, sigmaX2)    
    fX = gauss(x, muX, sigmaX)
    
    signal_plot3(x, fX1, x, fX2, x, fX)

def BLUE_demo1():
    interact(BLUE_demo1_plot, w1=(0, 1.0, 0.1), w2=(0, 1.0, 0.1),
             continuous_update=False)
    
    

    

