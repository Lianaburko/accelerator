import time
import functions
from functions import get_list_of_vars, order_of_vars, priority as pr, two_pow
import json
from sympy import symbols, Symbol, simplify
from sympy import *

file = open('/home/paro/Desktop/project/exp.txt','r')
inp_s = file.readline()
signs_string = '*/+-()^'
vars_order = order_of_vars(get_list_of_vars(inp_s))

print('inp_s = ',inp_s)
print('vars_order = ',vars_order)

a = Symbol('a')
b = Symbol('b')
x = Symbol('x')
c = Symbol('c')

x = symbols('x')
ex = 2+2*x
ex.factor()
print(ex)

inp_s.factor()
#print(inp_s)