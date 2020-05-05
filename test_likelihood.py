from local_code.adam.new_parameters import save_chain, load_chain
from local_code.junying.likelihood import likelihood

my_chain = load_chain()
print('here')
print(my_chain)
likelihoods = [float(likelihood(*chainboi)) for chainboi in my_chain[0:10]]
print(likelihoods)