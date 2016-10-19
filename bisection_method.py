# file: bisection_method.py
# This program implements the bisection method for finding
# the root of a polynomial function.

import matplotlib.pyplot as plt 
import numpy as np

def bisection_method (x1, x2, function, epsilon, root):
	""" Approximates the root of a polynomial function.
	For this algorithm to work properly, P(x1) < 0 and P(x2) > 0. 
	The parameters of this algorithm are two points, a polynomial function,
	a small epsilon, and the actual root. """

	print("\nBisection Method: ")

	print (x1, x2)

	point_change = abs(x2 - x1) # difference of the two points

	average = float(x1 + x2) / 2 # average of the two points
	
	errors = [abs(average - root)] # append initial error

	plt.figure(1) # Approximation plot

	x1_list = [x1]
	x2_list = [x2]
 
     # Finds the average of two points and assigns this average to 
     # one of the points depending on certain conditions.
     # Performs this operation until the error between the points
     # is less than epsilon.
	while point_change > epsilon:

		if function(average) > 0:
			x2 = average
			x2_list.append(x2)

		elif function(average) == 0:
			print (average)
			return (average, errors)
		
		else: # Value is negative
			x1 = average
			x1_list.append(x1)

		print (x1, x2)

		point_change = abs(x2 - x1) # new error and halt condition

		average = float(x1 + x2) / 2
		errors.append(abs(average - root)) # append new error

	# function values for x1 points and x2 points
	f1 = [function(x1_list[i]) for i in range(len(x1_list))]
	f2 = [function(x2_list[i]) for i in range(len(x2_list))]

	plt.plot(x1_list, f1, 'bo', x2_list, f2, 'bo')

	return (average, errors)
