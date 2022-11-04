from random import randint
import json
import numexpr 

with open('/home/paro/Desktop/project/vars.txt','r')  as inf:
    vars_list = json.load(inf)  # ["a", "b", "c", "d"]


file = open('/home/paro/Desktop/project/exp.txt','r')
expr = file.readline()

int_dct = dict()

for i in vars_list:
    int_dct[i] = randint(0,100)

for k,v in int_dct.items():
    expr = expr.replace(k,str(v))

result = numexpr.evaluate(expr)

with open('/home/paro/Desktop/project/input.txt','w') as inf:
    for k,v in int_dct.items():
        s = str(v) + '\n'
        inf.write(s)

with open('/home/paro/Desktop/project/output.txt','w') as inf:
    inf.write(str(result))

print(result)
print(expr)
print(int_dct)