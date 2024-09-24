from sympy import *

x = symbols('x')
res = integrate(3 * x ** 4 * exp(-2 * x), (x, 0, oo))

print(res)
