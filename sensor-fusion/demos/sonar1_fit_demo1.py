# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed
from matplotlib.pyplot import subplots, show
from .lib.signal_plot import create_axes

def sonar1_fit_demo1_plot(ignore_outliers=False):

    fit_max = 4
    
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

    d = np.linspace(dmin, dmax)
    model = np.polyval(p, d)
    
    axes, kwargs = create_axes(1)
    axes.plot(distance, sonar1, '.', alpha=0.2)
    axes.plot(d, model)
    axes.set_xlabel('Distance (m)')
    axes.set_ylabel('Measurement (m)')
    axes.set_ylim(0, fit_max)
    axes.grid(True)

def sonar1_fit_demo1():
    interact(sonar1_fit_demo1_plot, continuous_update=False)
