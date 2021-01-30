import numpy as np
import pandas as pd

alpha = 0.72
phi = alpha
delta = 0.034
y_z = 2.5
job_finding = 0.45
rho = 0.878**(1/3)
gamma_1 = 20
gamma_2 = 1.57
beta = 0.953**(1/12)


def my_plotter(filename=False):
    phi = np.linspace(0, 10, 1000)
    function_to_plot = \
        1/(
            1 - (1/gamma) * (rho/alpha) * (1 - beta * (1 - delta - phi *theta_q_theta)/
                                           (1 - beta * rho (1 - delta - (phi * theta_q_theta)/alpha)
                                           )
                                           )
        )
    if filename:
        plt.savefig(f'{filename}')
