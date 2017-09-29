# -*- coding: utf-8 -*-
#find the integral of a function f(x) from a to b i.e.

# ∫from a to b f(x)dx

#In python we use numerical quadrature to achieve this with the
# scipy.integrate.quad command. As a specific example, lets integrate

# y=x(squared)

#from x=0 to x=1.
#You should be able to work out that the answer is 1/3.

from scipy.integrate import quad

def integrand(x):
    return x**2

ans, err = quad(integrand, 0, 1)
print ans
