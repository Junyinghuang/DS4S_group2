# For plotting and double-checking our results
from matplotlib import pyplot as plt

def plot_markov_chain(chain_in):
    plt.plot(chain_in)
    plt.legend(['o_l', 'o_m', 'H0', 'M'])
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.show()