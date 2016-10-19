def D(f,h=1e-3):
	""" Returns derivative of function f """

	def df(x):
		deriv=(f(x+h)-f(x))/h
		return round(deriv,3)
	
	return df

def g(x): return x*x

def I(f,h=1e-3):
	""" Returns the definite integral of function f """

	def intf(b,a=0):
		total = 0
		x = a
		while x<=b:
			total += h*(f(x+h)+f(x))/2.
			x += h
		return round(total,3)

	return intf