# For producing markov chains
import numpy as np


def generate_MCMC_chain(sample_number, data,
                        initial_proposal):
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
    data =  data
    current_proposal = initial_proposal

    for i in range(sample_number):

        next_proposal = proposal(current_proposal)

        current_proposal_likelihood = likelihood(current_proposal,
                                                 data)
        next_proposal_likelihood = likelihood(next_proposal,
                                                 data)
        likelihood_ratio = (next_proposal_likelihood
                           / current_proposal_likelihood)

        acceptance_probabilty = min(1.0, likelihood_ratio)

        acceptance = np.random.uniform() <= acceptance_probabilty
        if acceptance:
            current_proposal = next_proposal
            posterior_chain = np.append(posterior_chain, next_proposal)
        else:
            current_proposal = current_proposal
            posterior_chain = np.append(posterior_chain, current_proposal)

    return posterior_chain

