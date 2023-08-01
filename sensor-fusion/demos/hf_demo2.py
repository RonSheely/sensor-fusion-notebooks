# Michael P. Hayes UCECE, Copyright 2018--2023
import numpy as np
from ipywidgets import interact
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


def hf_demo2_plot(distX0='gaussian', sigmaX0=0.4, sigmaV=0.1, sigmaW=0.1,
                  seed=1, M=50, step=1):

    np.random.seed(seed)

    v = 2
    dt = 1

    # Tweak number of bins so that user has expected number of
    # bins spanning the plotted range for x.
    M = int(M * (4 - -2) / (3 - -1))

    xp = np.linspace(-2, 4, M)
    dxp = xp[1] - xp[0]

    fXh_initial = pdf(xp, 0, sigmaX0, distX0)
    fXh_prior = np.zeros(M)
    fXh_posterior = np.zeros(M)

    for m in range(1, step + 1):

        if m > 1:
            fXh_initial = fXh_posterior

        # Convolve initial histogram with process model
        for i in range(len(xp)):
            total = 0
            for j in range(len(xp)):
                total += fXh_initial[j] * \
                    gauss(xp[i] - xp[j] - v * dt, 0, sigmaW)
            fXh_prior[i] = total * dxp

        z = m * dt * v + np.random.randn(1) * sigmaV

        fXh_posterior = fXh_prior * gauss(z - xp, 0, sigmaV)
        fXh_posterior /= np.trapz(fXh_posterior, xp)

    fig = figure(figsize=(10, 5))
    ax = fig.add_subplot(111)
    ax.grid(True)

    ax.bar(xp, fXh_initial, label='$X_{%d}$ initial' % (
        m - 1), edgecolor='black', width=dxp)

    ax.bar(xp, fXh_prior, label='$X_{%d}^{-}$ prior' %
           m, edgecolor='black', width=dxp)

    ax.bar(xp, fXh_posterior,
           label='$X_{%d}^{+}$ posterior' % m, edgecolor='black', width=dxp)

    ax.set_xlim(-1, 3)
    ax.set_xlabel('Position')
    ax.set_ylabel('Prob. density')
    ax.legend()


def hf_demo2():
    interact(hf_demo2_plot, step=(1, 5), M=(10, 200, 10),
             v=(1.0, 4.0, 0.2),
             distX0=distributions,
             sigmaX0=(0.1, 1, 0.1),
             sigmaV=(0.1, 1, 0.1),
             sigmaW=(0.1, 1, 0.1),
             seed=(1, 100, 1),
             continuous_update=False)
