from local_code.adam.new_parameters import save_chain, load_chain
from local_code.pritom.markov_chain import generate_MCMC_chain

sigmas = [.01,.01,.1,.1]

def continue_chain(chain_in,n_samples = 20):
    new_chain = generate_MCMC_chain(n_samples,None,chain_in[-1],sigmas)
    return chain_in+new_chain

current_chain = load_chain()
print(len(current_chain))
next_chain = continue_chain(current_chain,10)
save_chain(next_chain)