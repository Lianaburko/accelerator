import time
import functions
from functions import get_list_of_vars, order_of_vars, priority as pr, two_pow
import json

#---------------------------- meeooooowww -----------------------------------------
file = open('/home/paro/Desktop/project/exp.txt','r')
inp_s = file.readline()

print('inp is ',inp_s)

inp_s = 'a*b*(3+x)+c'
signs_string = '*/+-()^'
alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
unknowns = []
signs = []
level = 0
n = 0 #number of var 
level_dict = {} 
per_dict = {}

prior_dict = functions.creating_per_dict()[0]
unar_sign = functions.creating_per_dict()[1]

prior_per_dict = {} 

vars_order = order_of_vars(get_list_of_vars(inp_s))

with open('/home/paro/Desktop/project/vars.txt','w') as inf:
    json.dump(vars_order, inf)

#------------------------------------------------------------------------------------

def recurs(s):

    global n
    s = '+' + s + '+' 
    level = 0
    signs = functions.get_list_of_signs(s)
    unknowns = functions.get_list_of_vars(s)


    while(len(unknowns) > 1):
        level += 1
        level_permens = []
# -------------- nado menyat' tut ------------------------------------------
        for i in range(len(s)-1):
            if i > 0 and i < len(s) - 1 and s[i] in '+-*/^':
                if (s[i-2]) not in '()' and (s[i+2]) not in '()':
                    if (pr(s[i-2]) <= pr(s[i])) and (pr(s[i+2]) <= pr(s[i])):
                        if s[i-1:i+2] != '' and ('(' not in s[i-1:i+2]) and (')' not in s[i-1:i+2]):
                            if s[i] == '*' and (functions.check_number(s[i-1],s[i+1]) == 'hello'):
                                s[i] == '<'
                                s_old = s
                                s = s_old[0:i] + '<' + s_old[i+1:] 
                            prior_dict[pr(s[i])].append(s[i-1:i+2])
                
                    #prior_dict[unar_sign].append(s[i:i+2])

# --------------------------------------------------------------------------
            if i > 0 and i < len(s) - 1 and s[i] == '(':
                prev_i = i
                k = i
                l = str()
                
                bracker_counter = 1
                check = '00'
                while(check != ')0'):
                    k += 1
                    l += s[k]
                    if s[k] == '(':
                        bracker_counter += 1
                    if s[k] == ')':
                        bracker_counter -= 1
                    check = s[k] + str(bracker_counter)
                rec = recurs(l[:-1]) 
                l = '(' + l
                s = s.replace(l,rec[1])
                
                i = prev_i


            print('\n',prior_dict, '\n')
            #time.sleep(2)
        global list_per
        for i in range(unar_sign, 0,-1):
            for k in prior_dict[i]:
                if k in s:
                    list_per = []
                    for j in range(level,len(prior_per_dict)+1,1):  
                        for g in prior_per_dict[j]:                                    
                            list_per.append(g)

                    if (len(k) > 2 and k[0] not in list_per and k[2] not in list_per) or (len(k) == 2 and k[1] not in list_per):
                        s = s.replace(k, alf[n])
                        level_permens.append(k)

                        if k not in per_dict.values():
                            per_dict[alf[n]] = k
                            if level not in prior_per_dict.keys():
                                prior_per_dict[level] = []
                            prior_per_dict[level].append(alf[n])                      
                        n += 1
        
###################################################
        signs = functions.get_list_of_signs(s)
        unknowns = functions.get_list_of_vars(s)
###################################################

        if len(unknowns) == 1:
            if signs == ['+','-','+']:
                if unknowns[0] in list_per:
                    level += 1
                k = '-' + str(unknowns[0])
                s = s.replace(k, alf[n])
                level_permens.append(k)

                if k not in per_dict.values():
                    per_dict[alf[n]] = k 
                    if level not in prior_per_dict.keys():
                        prior_per_dict[level] = []
                    prior_per_dict[level].append(alf[n])                       
                n += 1
        
        print('the level is: ',level)
        print('prior_per_dict =', prior_per_dict)
        print('per_dict =', per_dict)
        print('current s is ', s[1:(len(s)-1)])
        print()
        
        with open('/home/paro/Desktop/project/input_to_help.txt','w')  as inf:
            json.dump(prior_per_dict, inf)
        with open('/home/paro/Desktop/project/input_to_help_1.txt','w') as inf:
            json.dump(per_dict, inf)

            
    return s
   
recurs(inp_s)       
functions.matrix_making()
