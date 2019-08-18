# Michael P. Hayes UCECE, Copyright 2018--2019
import numpy as np
from ipywidgets import interact, interactive, fixed
from matplotlib.pyplot import subplots, show
from .lib.signal_plot import create_axes

def sonar1_fit_error_demo1_plot(error_max=0.1, ignore_outliers=False):

    fit_errormax = 4
    
    # Load data
    filename = 'data/sonar1-calibration.csv'
    data = np.loadtxt(filename, delimiter=',', skiprows=1)

    # Split into columns
    distance, sonar1 = data.T
    
    dmin = distance.min()
    dmax = distance.max()

    if ignore_outliers:
        m = abs(distance - sonar1) < 0.1
        distance = distance[m]
        sonar1 = sonar1[m]        

    p = np.polyfit(distance, sonar1, 1)
    error = np.polyval(p, distance) - sonar1
    
    axes, kwargs = create_axes(1)
    axes.plot(distance, error, '.', alpha=0.2)
    axes.set_xlabel('Distance (m)')
    axes.set_ylabel('Error (m)')
    axes.set_ylim(-error_max, error_max)
    axes.grid(True)    

def sonar1_fit_error_demo1():
    interact(sonar1_fit_error_demo1_plot, error_max=(0.05, 0.2, 0.05), continuous_update=False)
