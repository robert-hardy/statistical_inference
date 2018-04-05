import numpy as np
import pandas as pd


TOSSES = 20
PATHS = 20
ALPHA = 0.1
SEED = 1

def df_coinflip(nb_tosses, nb_paths, p=0.5):
    """
    Returns a pd.DataFrame (nb_paths X nb_tosses), where p is the probability
    of getting a head.
    """
    samples = np.random.rand(nb_paths, nb_tosses)
    col_idx = list(range(1+nb_tosses))
    tosses = pd.DataFrame(np.where(samples<p, 1, 0), columns=col_idx[1:])
    tosses[0] = 0
    tosses = tosses[col_idx]
    cum_tosses = tosses.cumsum(axis=1)
    return cum_tosses


def create_pngs():
    np.random.seed(SEED)
    tosses1 = df_coinflip(TOSSES, PATHS, p=0.5)
    tosses2 = df_coinflip(TOSSES, PATHS, p=0.75)
    col_idx = tosses1.columns.tolist()
    ax = tosses1.T.plot(color='blue', alpha=ALPHA, legend=None, xticks=col_idx[::5])
    ax2 = tosses2.T.plot(color='red', alpha=ALPHA, legend=None, yticks=col_idx[::5], ax=ax)
    single_path = tosses1.loc[7]
    single_path.plot(ax=ax2, color='black', lw=3)
    fig = ax2.get_figure()
    fig.savefig('tosses.png')
