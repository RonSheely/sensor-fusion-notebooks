# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed
from .lib.signal_plot import signal_plot3
from .lib.utils import gauss

def multiple_hypothesis_demo1_plot(muX1=0, sigmaX1=1, w1=0.5, muX2=1,
                                   sigmaX2=1, w2=0.5):

    N = 401
    x = np.linspace(-8, 8, N)

    fX1 = gauss(x, muX1, sigmaX1)
    fX2 = gauss(x, muX2, sigmaX2)
    fX = w1 * fX1 + w2 * fX2

    fig = signal_plot3(x, fX1, x, fX2, x, fX)
    fig.axes[0].set_xlabel('$x$')

def multiple_hypothesis_demo1():
    interact(multiple_hypothesis_demo1_plot, muX1=(-5, 5), muX2=(-5, 5),
             sigmaX1=(0.01, 5, 0.01), sigmaX2=(0.01, 5, 0.01),
             w1=(0, 1, 0.1), w2=(0, 1, 0.1))
    

    
    

    

