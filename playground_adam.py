from local_code.adam.new_parameters import get_new_parameters
from local_code.junying.likelihood import likelihood
from local_code.pritom.markov_chain import generate_MCMC_chain
import numpy as np
from time import time
from local_code.adam.test import test_parameter_creation

test_parameter_creation()

'''
#Generation of Markov Chain takes far longer than desired.

t0 = time()
MCData = generate_MCMC_chain(10,None,[4,4,4,4],[.1,.1,.1,.1])
print(str(time()-t0) + ' seconds elapsed.')
'''