from z3 import *
def f(y):
	x = Int('x')
	z = Int('z')
	z = y
	y = x
	x = z
	return x*x

def g(x):
	return x*x

x = Int('x')
prove(f(x)==g(x))