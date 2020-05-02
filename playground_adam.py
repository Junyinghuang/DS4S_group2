from local_code.adam.new_parameters import get_new_parameters
from local_code.junying.likelihood import likelihood
from local_code.pritom.markov_chain import generate_MCMC_chain

print(generate_MCMC_chain(10,None,[4,4,4,4],[.1,.1,.1,.1]))