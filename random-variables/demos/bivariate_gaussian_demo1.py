# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed
from matplotlib.pyplot import figure
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from .lib.signal_plot import create_axes
from .lib.utils import mgauss2

def bivariate_gaussian_demo1_plot(muX=0, sigmaX=1, muY=0, sigmaY=1, rhoXY=0):

    N = 101
    x = np.linspace(-10, 10, N)
    y = np.linspace(-10, 10, N)    

    X, Y = np.meshgrid(x, y)
    
    fXY = mgauss2(x, y, (muX, muY), (sigmaX, sigmaY), rhoXY)

    fig = figure(figsize=(8, 4))    
    ax = fig.add_subplot(111, projection='3d')   

    surf = ax.plot_surface(X, Y, fXY, rstride=1, cstride=1, cmap=cm.jet,
                           linewidth=0, antialiased=False)

    ax.set_xlabel('$X$')
    ax.set_ylabel('$Y$')    


def bivariate_gaussian_demo1():
    interact(bivariate_gaussian_demo1_plot, muX=(-5, 5), sigmaX=(0.01, 5, 0.01),
             muY=(-5, 5), sigmaY=(0.01, 5, 0.01), rhoXY=(-1,1,0.1))
    
    

    

