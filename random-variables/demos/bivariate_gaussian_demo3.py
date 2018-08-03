# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed
from matplotlib.pyplot import figure
from matplotlib import cm
from .lib.signal_plot import create_axes
from .lib.utils import mgauss2

def bivariate_gaussian_demo3_plot(muX=0, sigmaX=1, muY=0, sigmaY=1, rhoXY=0, slice='x = 0'):

    N = 101
    x = np.linspace(-10, 10, N)
    y = np.linspace(-10, 10, N)    

    X, Y = np.meshgrid(x, y)
    
    fXY = mgauss2(x, y, (muX, muY), (sigmaX, sigmaY), rhoXY)

    fig = figure(figsize=(4, 4))    
    ax = fig.add_subplot(111)   

    if slice == 'x = 0':
        ax.plot(x, fXY[N // 2, :])
        ax.set_xlabel('$X$')
    elif slice == 'y = 0':        
        ax.plot(y, fXY[:, N // 2])        
        ax.set_xlabel('$Y$')
    else:
        raise ValueError('Unknown slice ' + slice)

def bivariate_gaussian_demo3():
    interact(bivariate_gaussian_demo3_plot, muX=(-5, 5), sigmaX=(0.01, 5, 0.01),
             muY=(-5, 5), sigmaY=(0.01, 5, 0.01), rhoXY=(-0.95,0.95,0.05), slice=['x = 0', 'y = 0'])
