# file: secant_method.py
# This program implements the secant method for finding
# the root of a polynomial function.

import matplotlib.pyplot as plt 
import numpy as np

def secant_method (x1, x2, function, epsilon, root):
	""" Approximates the root of a polynomial function.
	For this algorithm to work properly, P(x1) > 0 and P(x2) > 0
	or P(x1) < 0 and P(x2) < 0.
	The parameters of this algorithm are two points, a polynomial function,
	a small epsilon, and the actual root to calculate the error. """

	print("\nSecant Method: ")

	print (x1, x2)

	point_change = abs(x2 - x1)
	errors = [] # error list

	plt.figure(7)

	points = []

	# halting condition: width between points is less than epsilon
	while point_change > epsilon:
		
		# linear interpolation between points 
		slope = (function(x2) - function(x1)) / (x2 - x1) # slope of line
		slope_inv = slope**(-1) # inverse of the slope

		# intersection point of the line and the axis
		estimate = -function(x1) * slope_inv + x1 # update estimate
		points.append(estimate)
		x1 = x2 # replace x1 with previous estimate
		x2 = estimate # replace x2 with new estimate
		print (x1, x2)

		point_change = abs(x2 - x1) # update halting condition

		errors.append(abs(root - estimate)) # append new error

	f1 = [function(points[i]) for i in range(len(points))]

	plt.plot(points, f1, 'bo')

	return (estimate, errors)
