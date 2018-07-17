# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed
from matplotlib.pyplot import subplots, show
from .lib.signal_plot import create_axes

def sonar1_hist_demo1_plot(distance=1.0, width=0.5, error_max=0.2):

    # Load data
    filename = 'data/sonar1-calibration.csv'
    data = np.loadtxt(filename, delimiter=',', skiprows=1)

    # Split into columns
    distance1, sonar1 = data.T
    
    error = sonar1 - distance1

    m = (distance1 < (distance + 0.5 * width)) & (distance1 > (distance - 0.5 * width))

    bins = np.linspace(-error_max, error_max, 100)
    
    axes, kwargs = create_axes(1)
    axes.hist(error[m], bins=bins)
    axes.set_xlabel('Error (m)')
    axes.set_xlim(-error_max, error_max)    

def sonar1_hist_demo1():
    interact(sonar1_hist_demo1_plot, distance=(0, 3.5, 0.2),
             width=(0.1, 1, 0.1), error_max=(0.05, 0.5, 0.05),
             continuous_update=False)
