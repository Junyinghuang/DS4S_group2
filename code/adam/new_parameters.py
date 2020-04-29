# For making jumps in parameter space

import numpy as np

def get_new_parameters(list_of_sigmas,list_of_recent_guesses):
    '''
    Ex:
    old_guesses = [2,3]
    sigmas = [1,1]
    get_new_parameters(sigmas,old_guesses)
    '''
    new_guesses = [np.random.normal(point,sigma) for point,sigma in zip(list_of_recent_guesses,list_of_sigmas)]
    return new_guesses
