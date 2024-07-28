# Michael P. Hayes UCECE, Copyright 2018--2019
import numpy as np
from ipywidgets import interact
from matplotlib.pyplot import subplots
from .lib.utils import gauss


def bayes_motion_model_plot(sigmaW=0.2, deltax=2):

    Nx = 801
    x = np.linspace(0, 5, Nx)
    xp = np.linspace(0, 5, Nx)

    fig, axes = subplots(1, figsize=(5, 5))
    fig.tight_layout()

    X, Xp = np.meshgrid(x, xp)

    foo = gauss(X - Xp - deltax, 0, sigmaW)

    axes.imshow(foo.T, origin='lower', extent=(xp[0], xp[-1], x[0], x[-1]))
    axes.axis('tight')
    axes.set_xlabel('$x_{n-1}$')
    axes.set_ylabel('$x_{n}$')


def bayes_motion_model_demo1():
    interact(bayes_motion_model_plot, sigmaW=(0.01, 0.5, 0.01),
             deltax=(0, 4, 0.4))
