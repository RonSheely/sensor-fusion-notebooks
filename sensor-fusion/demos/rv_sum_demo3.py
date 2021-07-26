# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed
from .lib.signal_plot import signal_plot3
from .lib.utils import gauss, pdf, distributions


def rv_sum_demo3_plot(muX=0, rangeX=2, muY=0, rangeY=2):


    N = 401
    x = np.linspace(-5, 5, N)
    dx = x[1] - x[0]

    xmin = muX - 0.5 * rangeX
    xmax = muX + 0.5 * rangeX

    ymin = muY - 0.5 * rangeY
    ymax = muY + 0.5 * rangeY        

    fX = 1.0 * ((x >= xmin) & (x <= xmax))
    fX /= np.trapz(fX, x)

    fY = 1.0 * ((x >= ymin) & (x <= ymax))
    fY /= np.trapz(fY, x)    
    
    fZ = np.convolve(fX, fX) * dx

    M = fZ.shape[-1]
    z = np.arange(-M // 2, M // 2) * dx    
    mz = (z < 5) & (z > -5)
    
    mx = (x < 5) & (x > -5)        
    
    fig = signal_plot3(x[mx], fX[mx], x[mx], fY[mx], z[mz], fZ[mz], ylim=(0, 0.55))
    fig.axes[0].set_xlabel('')
    

def rv_sum_demo3():
    interact(rv_sum_demo3_plot, muX=(-2, 2), rangeX=(1, 4, 0.5),
             muY=(-2, 2), rangeY=(1, 4, 0.5),
             continuous_update=False)
    
    

    

