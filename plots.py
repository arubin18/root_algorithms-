# file: plots.py
# --------------
# This program uses the pyplot library to plot the polynomial 
# and its root using different root finding algorithms. The actual error for each algorithm
# will also be plotted on separate figures. 

from root_algs import *  # Importing polynomial root approximation functions 
import matplotlib.pyplot as plt 
import numpy as np
import math
from common_functions.calculus import *

def P(x):
	""" polynomial function """
	return x**2 - 4

dP = D(P)  # calls on calculus module

root = 2  # actual root used for error plots

x1 = 1 # P(x1) < 0
x2 = 4 # P(x2) > 0
x3 = 5 # P(x3) > 0

epsilon = 1e-4 # small error
print ("Epsilon is " + str(epsilon))

# Calls on the bisection method
a_root, e_list = bisection_method(x1, x2, P, epsilon, root)

# Calls on the false position function
fal_root, e2_list = false_position(x1, x2, P, epsilon, root)

# Calls on the newton method
new_root, e3_list = newton_method(x2, P, dP, epsilon, root)

# Calls on the secant method
sec_root, e4_list = secant_method(x2, x3, P, epsilon, root)

def E(x1, x2, t):
	""" Error function for Bisection Method """
	return abs(x2 - x1) / 2**t

if x2 > x1:
	d1 = np.arange(x1, x2, 0.1) # domain list for polynomial plot
else:
	d1 = np.arange(x2, x1, 0.1)

# Bisection Method error domain
t1 = np.arange(0, len(e_list), 0.1) # domain list for maximum error plot
t2 = np.arange(0, len(e_list)) # domain list for actual error plot

# False Position error domain
tf1 = np.arange(0, len(e2_list)) # domain list for actual error plot

# Newton Method error domain 
tn1 = np.arange(0, len(e3_list)) # domain list for actual error plot

# Secant Method error domain 
ts1 = np.arange(0, len(e4_list)) # domain list for actual error plot

# zero array
null = []
for i in range(len(d1)):
    null.append(0)

# Bisection Method Root Approximation
plt.figure(1)
plt.plot(d1, P(d1), 'k', d1, null, 'k', a_root, P(a_root), 'ro')
plt.title('Bisection Method Root Approximation Plot')
plt.xlabel('x')
plt.ylabel('P(x)')

# Maximum and Actual Error Plot for Bisection Method
plt.figure(2)
plt.plot(t1, E(x1, x2, t1), 'b', t2, e_list, 'r')
plt.title('Maximum and Actual Error Plot for Bisection Method')
plt.xlabel('Iterations (n)')
plt.ylabel('E(n)')

# False Position Root Approximation
plt.figure(3)
plt.plot(d1, P(d1), 'k', d1, null, 'k', fal_root, P(fal_root), 'ro')
plt.title('False Position Root Approximation Plot')
plt.xlabel('x')
plt.ylabel('P(x)')

# Error Plot for False Position Method
plt.figure(4)
plt.plot(tf1, e2_list, 'r')
plt.title('Error Plot for False Position')
plt.xlabel('Iterations (n)')
plt.ylabel('E(n)')

# Newton Method Root Approximation
plt.figure(5)
plt.plot(d1, P(d1), 'k', d1, null, 'k', new_root, P(new_root), 'ro')
plt.title('Newton Method Root Approximation Plot')
plt.xlabel('x')
plt.ylabel('P(x)')

# Error Plot for Newton Method
plt.figure(6)
plt.plot(tn1, e3_list, 'r')
plt.title('Error Plot for Newton Method')
plt.xlabel('Iterations (n)')
plt.ylabel('E(n)')

# Secant Method Root Approximation
plt.figure(7)
plt.plot(d1, P(d1), 'k', d1, null, 'k', sec_root, P(sec_root), 'ro')
plt.title('Secant Method Root Approximation Plot')
plt.xlabel('x')
plt.ylabel('P(x)')

# Error Plot for Secant Method
plt.figure(8)
plt.plot(ts1, e4_list, 'r')
plt.title('Error Plot for Secant Method')
plt.xlabel('Iterations (n)')
plt.ylabel('E(n)')

plt.show()
