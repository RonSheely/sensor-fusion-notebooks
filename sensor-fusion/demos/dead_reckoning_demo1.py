# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_plot2
from .lib.utils import gauss


def dead_reckoning_demo1_plot(w1, w2):

    steps = 10
    
    N = 401
    x = np.linspace(-10, 10, N)

    muY = a * muX
    sigmaY = abs(a) * sigmaX
    
    fX = gauss(x, muX, sigmaX)
    fY = gauss(x, muY, sigmaY)
    
    fig = figure(figsize=(10, 5))
    ax = fig.add_subplot(111)
    ax.set_xlim(-10, 10)
    ax.set_ylim(0, 10)
    ax.grid(True)

    for m in range(steps):

        # Do transitions here
        ax.plot(x, y, label='%d' % m)

    ax.legend()

def dead_reckoning_demo1():
    interact(dead_reckoning_demo1_plot, continuous_update=False)
    
    

    

