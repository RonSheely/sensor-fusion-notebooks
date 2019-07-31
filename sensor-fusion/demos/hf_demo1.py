# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed, Checkbox
from scipy.interpolate import interp1d
from matplotlib.pyplot import figure
from .lib.utils import gauss

distributions = ['uniform', 'gaussian']

def pdf(x, muX, sigmaX, distribution):

    if distribution == 'gaussian':
        return gauss(x, muX, sigmaX)
    elif distribution == 'uniform':
        xmin = muX - np.sqrt(12) * sigmaX / 2
        xmax = muX + np.sqrt(12) * sigmaX / 2
        return 1.0 * ((x >= xmin) & (x <= xmax)) / (xmax - xmin)
    raise ValueError('Unknown distribution %s' % distribution)


def hf_demo1_plot(distX0='gaussian', sigmaX0=0.4, sigmaV=0.1, sigmaW=0.1,
                  seed=1, M=100):

    np.random.seed(seed)

    v = 2
    step = 1
    
    dt = 1    
    A = 1
    B = dt
    C = 1
    D = 0

    Nx = 1000
    x = np.linspace(-10, 40, Nx)
    hx = np.linspace(-2, 4, M)
    dhx = hx[1] - hx[0]
    
    fXh_initial = pdf(hx, 0, sigmaX0, distX0)
    fXh_prior = np.zeros(M)

    for m in range(1, step + 1):

        if m > 1:
            fXh_initial = fXh_posterior

        # Convolve initial histogram with process model
        for i in range(len(hx)):
            total = 0
            for j in range(len(hx)):
                total += fXh_initial[j] * gauss(hx[i] - hx[j] - v * dt, 0, sigmaW)
            fXh_prior[i] = total * dhx
            
        z = C * m * dt * v + np.random.randn(1) * sigmaV

        fXh_posterior = fXh_prior * gauss(hx, z, sigmaV)
        fXh_posterior /= np.trapz(fXh_posterior, hx)
        

    fig = figure(figsize=(10, 5))
    ax = fig.add_subplot(111)
    ax.grid(True)

    ax.bar(hx, fXh_initial, label='$X_{%d}$ initial' % (m - 1), edgecolor='black', width=dhx)

    ax.bar(hx, fXh_prior, label='$X_{%d}^{-}$ prior' % m, edgecolor='black', width=dhx)

    ax.bar(hx, fXh_posterior, label='$X_{%d}^{+}$ posterior' % m, edgecolor='black', width=dhx)

    ax.set_xlim(-1, 3)
    ax.set_xlabel('Position')    
    ax.set_ylabel('Prob. density')
    ax.legend()

def hf_demo1():
    interact(hf_demo1_plot, step=(1, 5), M=(10, 200, 10),
             v=(1.0, 4.0, 0.2),
             distX0=distributions,
             sigmaX0=(0.1, 1, 0.1),
             sigmaV=(0.1, 1, 0.1),
             sigmaW=(0.1, 1, 0.1),
             seed=(1, 100, 1),
             continuous_update=False)
