# A simple file to produce the results we'll present on 05/07/20

#List of parameters should look like 'o_l, o_m, H0, M'

import numpy as np
import gmpy2
from local_code.pritom.markov_chain import generate_MCMC_chain
from local_code.adam.visualization import plot_markov_chain, split_data, pantheon_scatter

def reproduce_pantheon_constraints():
    my_chain = generate_MCMC_chain(1000,None,[.8,.3,70,19.23],[.01,.01,.1,.1])
    plot_markov_chain(my_chain)
    pantheon_scatter(my_chain)

def plot_posterior_of_h0():
    pass

def residual_plot_binned_data():
    pass

def chi_squared_and_PTE():
    pass

def noise_and_best_fit():
    pass

def histogram_of_cov_squared_residuals():
    pass

def h0_stability_test():
    pass

#Part 1
reproduce_pantheon_constraints()


#Part 2
plot_posterior_of_h0()

#Part 3, tests
residual_plot_binned_data()

chi_squared_and_PTE()

noise_and_best_fit()

histogram_of_cov_squared_residuals()

h0_stability_test()

