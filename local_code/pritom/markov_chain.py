# For producing markov chains
import numpy as np
from local_code.adam.new_parameters import get_new_parameters
from local_code.junying.likelihood import likelihood

def generate_MCMC_chain(sample_number, data,
                        initial_proposal, sigmas):
    '''
    This function generates and return a MCMC chain

    Parameters
    -----------
    sample_number: int
        Number of samples one wants to draw

    data: list
        The data to help evaluating the likelihood.

    initial_proposal: float
        The initial proposed point from where the chain can
        start.

    Returns
    --------
    posterior_chain: list
        A list of samples drawm from MCMC chain
    '''

    posterior_chain = []
    #data =  data
    current_proposal = initial_proposal

    for i in range(sample_number):

        next_proposal = get_new_parameters(sigmas,current_proposal)
        print('check1')
        current_proposal_likelihood = likelihood(*current_proposal)
        print('check2')
        next_proposal_likelihood = likelihood(*next_proposal)
        print('check3')
        likelihood_ratio = (next_proposal_likelihood
                           / current_proposal_likelihood)
        print('check4')
        acceptance_probabilty = min(1.0, likelihood_ratio)
        print('check5')
        acceptance = np.random.uniform() <= acceptance_probabilty
        if acceptance:
            current_proposal = next_proposal
            posterior_chain = np.append(posterior_chain, next_proposal)
        else:
            current_proposal = current_proposal
            posterior_chain = np.append(posterior_chain, current_proposal)
        print('check6')
    return posterior_chain

