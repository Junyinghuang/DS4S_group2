from local_code.adam.new_parameters import save_chain, load_chain
from local_code.junying.likelihood import likelihood
from local_code.junying.likelihood import mu
from local_code.junying.likelihood import gause
import numpy as np
import gmpy2
import matplotlib.pyplot as plt

'''
test likelihood
'''
my_chain = load_chain()
print('here')
print(my_chain)
likelihoods = [float(likelihood(*chainboi)) for chainboi in my_chain[0:10]]
print(likelihoods)
'''
it gives reasonable likelihood
'''

'''
test E, dL, mu
'''
x=np.linspace(0.01,1,100)
y=mu(x,0.3,0.69,70000)
plt.xscale("log")
plt.plot(x,y)
plt.xlabel('z')
plt.ylabel('mu')
plt.grid()
plt.show()
'''
the plot matches figure 11 in the paper, the three functions work
'''

'''
test gaus
'''
x=np.linspace(0.01,100,1000)
y=gaus(40,10,x)
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('gaus')
plt.grid()
plt.show()
'''
the plot is a gaussian function, so this function works
'''
