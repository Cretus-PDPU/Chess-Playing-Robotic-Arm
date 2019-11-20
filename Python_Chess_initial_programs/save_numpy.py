import numpy as np 

a = np.ones((7,7,2),dtype=int)
np.savez("Python_Chess_initial_programs/temp1.npz",points = a)
b = np.load('Python_Chess_initial_programs/temp1.npz')
# b = np.fromfile("temp.dat",dtype=int)
print(b['points'])
# print(b)
print(b['points'].shape)