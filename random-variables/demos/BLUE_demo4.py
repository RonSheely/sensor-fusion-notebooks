# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed
from .lib.signal_plot import signal_plot3
from .lib.utils import gauss, rect, trap2

def BLUE_demo4_plot(sigmaZ1=1.0, sigmaZ2=2.0, w1=0.5):

    w2 = 1.0 - w1
    
    muZ1 = 2
    muZ2 = 2

    WZ1 = sigmaZ1 * np.sqrt(12)
    WZ2 = sigmaZ2 * np.sqrt(12)

    muZ = w1 * muZ1 + w2 * muZ2
    sigmaZ = np.sqrt(w1**2 * sigmaZ1**2 + w2**2 * sigmaZ2**2)    
    WZ = w1 * WZ1 + w2 * WZ2
    TZ = abs(w1 * WZ1 - w2 * WZ2)
    
    N = 401
    z = np.linspace(-8, 8, N)
    
    fZ1 = rect((z - muZ1) / WZ1) / WZ1
    fZ2 = rect((z - muZ2) / WZ2) / WZ2
    fZ = trap2(z, TZ, WZ) * (2 / (TZ + WZ))
    
    signal_plot3(z, fZ1, z, fZ2, z, fZ, ylim=(0, 1.0))

def BLUE_demo4():
    interact(BLUE_demo4_plot,
             sigmaZ1=(0.5, 4.0, 0.1),
             sigmaZ2=(0.5, 4.0, 0.1),
             w1=(0, 1.0, 0.1))
    
    

    

