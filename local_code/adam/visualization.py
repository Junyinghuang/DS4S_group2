# For plotting and double-checking our results
from matplotlib import pyplot as plt

def plot_markov_chain(chain_in):
    plt.plot(chain_in)
    plt.legend(['o_l', 'o_m', 'H0', 'M'])
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.show()

def split_data(chain_in):
    o_ls = [datapoint[0] for datapoint in chain_in]
    o_ms = [datapoint[1] for datapoint in chain_in]
    H0s = [datapoint[2] for datapoint in chain_in]
    Ms = [datapoint[3] for datapoint in chain_in]
    return o_ls,o_ms, H0s, Ms

def pantheon_scatter(chain_in):
    o_ls, o_ms, H0s, Ms = split_data(chain_in)
    plt.scatter(o_ms,o_ls)
    plt.xlabel('Omega_m')
    plt.ylabel('Omega_Lambda')
    plt.title('oCDM Constraints For SN-only Sample')
    plt.xlim(0,1.6)
    plt.ylim(0,2.4)
    plt.show()