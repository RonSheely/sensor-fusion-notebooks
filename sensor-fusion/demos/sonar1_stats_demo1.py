# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed
from matplotlib.pyplot import subplots, show
from .lib.signal_plot import create_axes

def sonar1_stats_demo1_plot(N=20):

    # Load data
    filename = 'data/sonar1-calibration.csv'
    data = np.loadtxt(filename, delimiter=',', skiprows=1)

    # Split into columns
    distance, sonar1 = data.T
    
    dmin = distance.min()
    dmax = distance.max()
    
    dr = (dmax - dmin) / N
    r = (np.arange(N) + 0.5) * dr
    
    error = sonar1 - distance

    means = np.zeros(N)
    stds = np.zeros(N)
    
    for n in range(N):
        r1 = r[n] - 0.5 * dr
        r2 = r[n] + 0.5 * dr    
        m = (distance > r1) & (distance < r2)

    means[n] = error[m].mean()
    stds[n] = error[m].std()

    axes, kwargs = create_axes(2)
    axes[0].plot(r, means, '.')
    axes[0].set_xlabel('Distance (m)')
    axes[0].set_ylabel('Error mean (m)')
    axes[1].plot(r, stds, '.')
    axes[1].set_xlabel('Distance (m)')
    axes[1].set_ylabel('Error std dev (m)')


def sonar1_stats_demo1():
    interact(sonar1_stats_demo1_plot, N=(1, 50),
             continuous_update=False)
