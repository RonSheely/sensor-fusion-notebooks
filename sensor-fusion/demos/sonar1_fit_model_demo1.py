# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed
from matplotlib.pyplot import subplots, show
from .lib.signal_plot import create_axes

def sonar1_fit_model_demo1_plot(N=20, order=2, ignore_outliers=True):

    # Load data
    filename = 'data/sonar1-calibration.csv'
    data = np.loadtxt(filename, delimiter=',', skiprows=1)

    # Split into columns
    distance1, sonar1 = data.T
    
    dmin = distance1.min()
    dmax = distance1.max()
    
    dr = (dmax - dmin) / N
    r = (np.arange(N) + 0.5) * dr

    if ignore_outliers:
        m = abs(distance1 - sonar1) < 0.1
        distance1 = distance1[m]
        sonar1 = sonar1[m]                

    p = np.polyfit(distance1, sonar1, 1)
    error = np.polyval(p, distance1) - sonar1            

    means = np.zeros(N)
    stds = np.zeros(N)
    
    for n in range(N):
        dmin = r[n] - 0.5 * dr
        dmax = r[n] + 0.5 * dr
        m = (distance1 > dmin) & (distance1 < dmax)

        means[n] = error[m].mean()
        stds[n] = error[m].std()

    mean_fit_model = np.polyval(np.polyfit(r, means, order), r)
    std_fit_model = np.polyval(np.polyfit(r, stds, order), r)        
        
    axes, kwargs = create_axes(2)
    axes[0].plot(r, means, '.')
    axes[0].plot(r, mean_fit_model)
    axes[0].set_xlabel('Distance (m)')
    axes[0].set_ylabel('Error mean (m)')
    axes[1].plot(r, stds, '.')
    axes[1].plot(r, std_fit_model)    
    axes[1].set_xlabel('Distance (m)')
    axes[1].set_ylabel('Error std dev (m)')
    show()

def sonar1_fit_model_demo1():
    interact(sonar1_fit_model_demo1_plot, N=(1, 50), order=(1, 5),
             continuous_update=False)
