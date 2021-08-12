# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed
from matplotlib.pyplot import figure
from matplotlib import cm
from .lib.signal_plot import create_axes
from .lib.utils import mgauss2

def bivariate_gaussian_demo2_plot(muX=0, sigmaX=1, muY=0, sigmaY=1, rhoXY=0):

    N = 101
    x = np.linspace(-10, 10, N)
    y = np.linspace(-10, 10, N)    

    if sigmaX < 0.01:
        sigmaX = 0.001
    if sigmaY < 0.01:
        sigmaY = 0.001        
    
    X, Y = np.meshgrid(x, y)
    
    fXY = mgauss2(x, y, (muX, muY), (sigmaX, sigmaY), rhoXY)

    fig = figure(figsize=(4, 4))    
    ax = fig.add_subplot(111)   

    ax.contour(X, Y, fXY)
    ax.axis('equal')

    ax.set_xlabel('$X$')
    ax.set_ylabel('$Y$')    


def bivariate_gaussian_demo2():
    interact(bivariate_gaussian_demo2_plot, muX=(-5, 5), sigmaX=(0, 5, 0.1),
             muY=(-5, 5), sigmaY=(0, 5, 0.1), rhoXY=(-0.95,0.99,0.05))
    
    

    

