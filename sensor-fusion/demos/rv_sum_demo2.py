# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed
from .lib.signal_plot import signal_plot3
from .lib.utils import gauss, pdf, distributions


def rv_sum_demo2_plot(muX=0, sigmaX=1, muY=0, sigmaY=1,
                      distribution=distributions[1]):

    N = 401
    x = np.linspace(-10, 10, N)
    dx = x[1] - x[0]        

    fX = pdf(x, muX, sigmaX, distribution)
    fY = pdf(x, muY, sigmaY, distribution)    
    
    fZ = np.convolve(fX, fX) * dx

    M = fZ.shape[-1]
    z = np.arange(-M // 2, M // 2) * dx    
    mz = (z < 8) & (z > -8)
    
    mx = (x < 8) & (x > -8)        
    
    signal_plot3(x[mx], fX[mx], x[mx], fY[mx], z[mz], fZ[mz], ylim=(0, 0.55))

def rv_sum_demo2():
    interact(rv_sum_demo2_plot, muX=(-2, 2), sigmaX=(0.55, 2, 0.01),
             muY=(-2, 2), sigmaY=(0.55, 2, 0.01),
             distribution=distributions,
             continuous_update=False)
    
    

    

