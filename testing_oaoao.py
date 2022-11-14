from sympy import factor
from sympy.abc import a
from sympy.abc import b 
from sympy.abc import x 
from sympy.abc import c 

expr = 3*a*b+x*a*b+c
ne = factor(expr)

print(ne)
