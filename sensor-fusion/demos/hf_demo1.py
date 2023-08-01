# Michael P. Hayes UCECE, Copyright 2018--2023
import numpy as np
from ipywidgets import interact
from matplotlib.pyplot import subplots
from .lib.utils import gauss


def hf_demo1_plot(sigmaX0=0.4, sigmaV=0.1, sigmaW=0.1,
                  seed=1, M=50):

    np.random.seed(seed)

    v = 2
    dt = 1

    # Tweak number of bins so that user has expected number of
    # bins spanning the plotted range for x.
    M = int(M * (4 - -2) / (3 - -1))

    xp = np.linspace(-2, 4, M)
    dxp = xp[1] - xp[0]

    fXh_initial = gauss(xp, 0, sigmaX0)
    fXh_prior = np.zeros(M)

    # Simulate measurement
    z = v * dt + np.random.randn(1) * sigmaV

    # Predict step: Convolve initial belief histogram with conditional
    # PDF for process model
    for i in range(len(xp)):
        total = 0
        for j in range(len(xp)):
            total += fXh_initial[j] * \
                gauss(xp[i] - xp[j] - v * dt, 0, sigmaW)
        fXh_prior[i] = total * dxp

    # Update step: Apply Bayes' theorem
    fXh_posterior = fXh_prior * gauss(z - xp, 0, sigmaV)
    eta = 1 / np.trapz(fXh_posterior, xp)
    fXh_posterior *= eta

    fig, ax = subplots(figsize=(10, 5))
    ax.grid(True)

    ax.bar(xp, fXh_initial, label='$X_0$ initial',
           edgecolor='black', width=dxp)

    ax.bar(xp, fXh_prior, label='$X_1^{-}$ prior',
           edgecolor='black', width=dxp)

    ax.bar(xp, fXh_posterior,
           label='$X_1^{+}$ posterior', edgecolor='black', width=dxp)

    ax.set_xlim(-1, 3)
    ax.set_xlabel('Position')
    ax.set_ylabel('Prob. density')
    ax.legend()


def hf_demo1():
    interact(hf_demo1_plot, step=(1, 5), M=(10, 200, 10),
             v=(1.0, 4.0, 0.2),
             sigmaX0=(0.1, 1, 0.1),
             sigmaV=(0.1, 1, 0.1),
             sigmaW=(0.1, 1, 0.1),
             seed=(1, 100, 1),
             continuous_update=False)
