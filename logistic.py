# DATE: 9/Aug/2016
#
# this code will solve the logistic map problem
#
# AUTHOR: Sebastian Lozada Ramirez


import numpy as np
import matplotlib.pyplot as plt

x0 = 0.1
r = 0.9
Nmax = 13

n = np.zeros(Nmax + 1)
x : np.zeros(Nmax + 1)


n[0] = 0
x[0] = x0



for i in range(1, Nmax +1):
	
	y = r * x0 * (1 - x0)
	x0 = y

	n[i] = i
	x[i] = y

plt.plot(n, x)
plt.show()
