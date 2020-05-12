from local_code.adam.new_parameters import get_new_parameters

def test_parameter_creation():
    '''
    Test to make sure I don't get any wonky results from my parameter adjustor
    '''
    sigmas = [1,2,3,4]
    initial_guesses = [0,0,0,0]
    new_guesses = get_new_parameters(sigmas,initial_guesses)
    #It would be surprising if any of these were more than, say, 4 sigma away from the initial guess.
    is_more_than_four_sigma_away = [int(abs(guess)>(4*sigma)) for guess, sigma in zip(new_guesses,sigmas)]
    assert sum(is_more_than_four_sigma_away)==0,"get_new_parameters yields surprising results."
    print('Test of parameter creation complete.')



# I've written no other tests, as all the "visualization" code I've written can be tested simply by 
# whether or not a plot shows up.