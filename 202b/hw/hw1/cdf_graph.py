import matplotlib.pyplot as plt
import numpy as np
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

def plot_cdf(thetas=[2], m=5, filename=False):
    fig, ax = plt.subplots()
    for theta in thetas:
        min_w = (theta - 1)/(theta)*m
        w = np.linspace(min_w, 10, 1000)
        cdf = 1 - (w / min_w)**(-1 * theta)
        ax.plot(np.linspace(0, min_w, 1000), np.linspace(0, 0, 1000),
                color='green',
                alpha= 1 - (thetas.index(theta) + 1)/len(thetas),
                label=f'$\\theta = {theta}$'
                )
        ax.plot(w, cdf,
                color='green',
                alpha= 1 - (thetas.index(theta) + 1)/len(thetas)
                )
    ax.vlines(m, ymin=0, ymax=.98, color='red')
    ax.annotate(r'$m$', (4.7, 1), fontsize=22)
    ax.get_xaxis().set_visible(False)
    plt.legend(loc='lower right', frameon=False)
    plt.savefig(f'{filename}.pdf')


plot_cdf(thetas=[i for i in range(4, 30, 3)], m=5, filename='cdf_graph')
