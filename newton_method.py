# file: newton_method.py
# This program implements the newton method algorithm for finding
# the root of a polynomial function.

import matplotlib.pyplot as plt 
import numpy as np

def newton_method (x0, function, dfunction, epsilon, root):
	""" Approximates the root of a polynomial function. 
	The parameters of this algorithm are a point, a polynomial function,
	the derivative of that function, a small epsilon, and the actual root
	to calculate the error. """

	print("\nNewton Method: ")
	
	x1 = -function(x0) / dfunction(x0) + x0 # Calculates a new point x1

	error_range = abs(root - x1)
	errors = [error_range] # append initial error

	print(x1, x0)

	point_change = abs(x1 - x0)

	plt.figure(5) # Approximation plot

	x1_list = [x1]

	while point_change > epsilon:

		# Division by zero will fail
		if (dfunction(x0) == 0):
			break

		x0 = x1 # assign previous x1 to x0

		# intersection point of the line tangent to the curve at P(x0) and the axis
		x1 = -function(x0) / dfunction(x0) + x0 # update x1
		x1_list.append(x1)

		point_change = abs(x1 - x0) # update halting variable

		error_range = abs(root - x1)
		errors.append(error_range) # last error < epsilon

		print (x1, x0)

	# function values for x1 points
	f1 = [function(x1_list[i]) for i in range(len(x1_list))]

	plt.plot(x1_list, f1, 'bo')

	return (x1, errors)
