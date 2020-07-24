# Michael P. Hayes UCECE, Copyright 2018--2019
import numpy as np
from ipywidgets import interact, interactive, fixed
from matplotlib.pyplot import subplots
from .lib.utils import gauss

steps = 10

def kf_demo2_plot(v=2.0, sigmaX0=0.1, sigmaV=0.4, sigmaW=0.4,
                  seed=1, step=1):

    np.random.seed(seed)

    dt = 1
    
    A = 1
    B = dt
    C = 1
    D = 0
    
    Nx = 801
    x = np.linspace(-10, 40, Nx)

    xrobot = 0
    Xinitialmean = 0
    Xinitialvar = sigmaX0**2
    
    fig, axes = subplots(2, figsize=(10, 6))
    axes[0].set_xlim(0, steps)
    axes[0].set_ylim(0, steps * B * v)    
    axes[0].grid(True)    
    axes[0].plot(0, xrobot, '-o', color='C0', label='actual')
    axes[0].plot(0, 0, '+', color='C1', label='measured')
    axes[0].plot(0, 0, 'x', color='C2', label='predicted')
    axes[0].plot(0, Xinitialmean, '*', color='C3', label='estimated') 
    axes[0].legend()

    axes[1].grid(True)
    
    mx = (x < round(steps * B * v)) & (x > -2)

    for m in range(1, step + 1):

        # xrobot += B * v + np.random.randn(1) * sigmaW
        # Assume robot deterministic
        xrobot += B * v

        if m > 1:
            Xinitialmean = Xpostmean
            Xinitialvar = Xpostvar

        Xpriormean = A * Xinitialmean + B * v
        Xpriorvar = (A**2) * Xinitialvar + sigmaW**2
        
        z = C * xrobot + np.random.randn(1) * sigmaV

        Xinfermean = (z - D * v) / C
        Xinfervar = (sigmaV**2) / (C**2)
        
        K = Xpriorvar / (Xpriorvar + Xinfervar)
        
        Xpostmean = K * Xinfermean + (1 - K) * Xpriormean
        Xpostvar = (Xpriorvar * Xinfervar) / (Xpriorvar + Xinfervar)

        axes[0].plot(m, xrobot, 'o', color='C0')
        axes[0].plot(m, Xinfermean, '+', color='C1')
        axes[0].plot(m, Xpriormean, 'x', color='C2')                
        axes[0].plot(m, Xpostmean, '*', color='C3')


    fXinitial = gauss(x, Xinitialmean, np.sqrt(Xinitialvar))
    fXprior = gauss(x, Xpriormean, np.sqrt(Xpriorvar))
    fXinfer = gauss(x, Xinfermean, np.sqrt(Xinfervar))
    fXpost = gauss(x, Xpostmean, np.sqrt(Xpostvar))

    axes[1].plot(x[mx], fXinitial[mx], ':', label='$X_{%d}$ initial' % (m - 1))        
    axes[1].plot(x[mx], fXprior[mx], '--', label='$X_{%d}^{-}$ prior' % m)
    axes[1].plot(x[mx], fXinfer[mx], '-.', label='$X_{%d}^{m}$ likelihood' % m)
    axes[1].plot(x[mx], fXpost[mx], label='$X_{%d}^{+}$ posterior' % m)

    axes[1].legend()
    #axes[1].text(z, max(fXpost) + 0.1, 'z=%.2f' % z)

    axes[0].set_title('z=%.2f, K=%.2f' % (z, K))
    

def kf_demo2():
    interact(kf_demo2_plot, step=(1, steps), v=(1.0, 4.0, 0.2),
             sigmaX0=(0.1, 1, 0.1),
             sigmaV=(0.1, 2, 0.1),
             sigmaW=(0.1, 1, 0.1),
             seed=(1, 100, 1),
             continuous_update=False)
