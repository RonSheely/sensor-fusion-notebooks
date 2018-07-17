# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed
from .lib.signal_plot import signal_plot3
from .lib.utils import gauss

def BLUE_demo2_plot(w1=0.5):

    w2 = 1.0 - w1
    
    muZ1 = 2
    muZ2 = 2
    sigmaZ1 = 1
    sigmaZ2 = 2

    muZ = w1 * muZ1 + w2 * muZ2
    sigmaZ = np.sqrt(w1**2 * sigmaZ1**2 + w2**2 * sigmaZ2**2)    
    
    N = 401
    z = np.linspace(-10, 10, N)

    fZ1 = gauss(z, muZ1, sigmaZ1)
    fZ2 = gauss(z, muZ2, sigmaZ2)    
    fZ = gauss(z, muZ, sigmaZ)
    
    signal_plot3(z, fZ1, z, fZ2, z, fZ)

def BLUE_demo2():
    interact(BLUE_demo2_plot, w1=(0, 1.0, 0.1))
    
    

    

