# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed
from .lib.signal_plot import create_axes


def BLUE_demo5_plot(sigmaZ1=1.0, sigmaZ2=2.0):

    w1 = np.linspace(0, 1, 201)
    w2 = 1 - w1

    sigmaZ = np.sqrt(w1**2 * sigmaZ1**2 + w2**2 * sigmaZ2**2)    

    axes, kwargs = create_axes(1)
    axes.plot(w1, sigmaZ)
    axes.set_xlabel('Weight $w_1$')
    axes.set_ylabel('Std dev. $\sigma_Z$')
    axes.grid(True)
        

def BLUE_demo5():
    interact(BLUE_demo5_plot,
             sigmaZ1=(0.1, 4.0, 0.1),
             sigmaZ2=(0.1, 4.0, 0.1))

    
    

    

