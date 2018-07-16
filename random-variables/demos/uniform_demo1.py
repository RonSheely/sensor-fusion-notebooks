# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed
from matplotlib.pyplot import show
from .lib.signal_plot import signal_plot
from .lib.utils import gauss

def uniform_demo1_plot(a=-1, b=1):

    N = 401
    x = np.linspace(-10, 10, N)

    fX = 1.0 * ((x >= a) & (x <= b)) / (abs(b - a) + 1e-12)
    fig = signal_plot(x, fX)
    mu_X = 0.5 * (a + b)
    sigma_X = abs(b - a) / np.sqrt(12)
    if b < a:
        mu_X = 0
        sigma_X = 0
    fig.axes[0].set_title('$\mu_{X}$ = %.1f, $\sigma_{X}$ = %.1f' % (mu_X, sigma_X))
    show()    

def uniform_demo1():
    interact(uniform_demo1_plot, a=(-5, 5), b=(-5, 5))
    
    

    

