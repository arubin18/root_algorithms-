# file: false_position.py
# This program implements the false position algorithm for finding
# the root of a polynomial function.

import matplotlib.pyplot as plt 
import numpy as np

def false_position (x1, x2, function, epsilon, root):
	""" Approximates the root of a polynomial function.
	For this algorithm to work properly, P(x1) < 0 and P(x2) > 0. 
	The parameters of this algorithm are two points, a polynomial function,
	and a small epsilon, and the actual root to calculate the error. """

	print("\nFalse Position Algorithm:")

	point_change = abs(x2 - x1) # initial maximum error
	errors = [point_change] # error list

	plt.figure(3) # Approximation plot

	points = []

	# halting condition: width between points is less than epsilon
	while point_change > epsilon:

		slope = (function(x2) - function(x1)) / (x2 - x1) # slope of the tangent line
		slope_inv = slope**(-1) # inverse of the slope

		# defines a new point by approximating a linear function between two points
		# using interpolation
		estimate = -function(x1) * slope_inv + x1
		
		if function(estimate) > 0:
			point_change = abs(estimate - x2) # update halting variable
			x2 = estimate

		elif function(estimate) == 0:
			return (estimate, errors)

		else: # Value is negative
			point_change = abs(estimate - x1) # update halting variable
			x1 = estimate

		points.append(estimate)
		print (estimate)

		errors.append(abs(root - estimate))

	f1 = [function(points[i]) for i in range(len(points))]

	plt.plot(points, f1, 'bo')

	return (estimate, errors)
