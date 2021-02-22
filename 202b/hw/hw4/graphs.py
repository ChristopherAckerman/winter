import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"]})

def my_plotter(filename='offer_curve.pdf'):
    fix, ax = plt.subplots(1, 1)
    x = np.linspace(-10, 10)
    feasibility = -1*x  
    feasibility_epsilon = -1*x + 2
    feasible_allocations = ax.plot(x, feasibility, label='feasible allocations')
    feasible_allocations_epsilon = ax.plot(x, feasibility_epsilon, label=r'feasible allocations $\varepsilon > 0$')
    my_x = np.linspace(-10, 3)
    offer_curve = ax.plot(my_x, ((my_x - 3)**2)/8 - 5, color='red', label='offer curve')
    offer_curve_2 = ax.plot(np.linspace(3, 10), np.linspace(0, -1) - 5, color='red')
    # x_axis = ax.plot(np.linspace(-10, 10), np.linspace(0, 0), color='gray')
    # y_axis = ax.plot(np.linspace(0, 0), np.linspace(-10, 10), color='gray')
    ax.legend(loc='upper right', frameon=False)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    # Eliminate upper and right axes
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    # Show ticks in the left and lower axes only
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    plt.savefig(filename)
my_plotter()
