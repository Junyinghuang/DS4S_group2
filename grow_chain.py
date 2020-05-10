from local_code.adam.new_parameters import save_chain, load_chain
from local_code.pritom.markov_chain import generate_MCMC_chain

sigmas = [.01,.01,.01,0]

#Initial chain values:  [0.8, 0.3, 70000, -19.23]

n_new_elements = 2000

def continue_chain(chain_in,n_samples = 200):
    new_chain = generate_MCMC_chain(n_samples,None,chain_in[-1],sigmas)
    return chain_in+new_chain

#to reset the chain
'''
next_chain = [[0.8, 0.3, 70000, -19.23]]
save_chain(next_chain)
'''

current_chain = load_chain()
print(current_chain[0])
print('Initial chain length: ' + str(len(current_chain)))
print('Starting where this chain ended...')
next_chain = continue_chain(current_chain,n_new_elements)
print('Final chain length: ' + str(len(next_chain)))
save_chain(next_chain)