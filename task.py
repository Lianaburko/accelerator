import functions
from functions import get_list_of_vars, make_string, order_of_vars, priority as pr
import json

# sdvigoviy register na multiplexorax 

#inp_s = input()
#inp_s = 'a+b*c/d+l/2'
inp_s = 'x*a*b+3*a*b+c'

signs_string = '*/+-()^'
alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
unknowns = []
signs = []
level = 0
n = 0 #number of peremennay
level_dict = {} 
per_dict = {}

prior_dict = functions.creating_per_dict()[0]
unar_sign = functions.creating_per_dict()[1]

prior_per_dict = {} 
 
#+++++++++++++++++++++++++
amount_of_entries = 2 # here we enter amount of entries 
amount_of_ends = 2 
#vars_order = order_of_vars(get_list_of_vars(inp_s)) 
vars_order = ['3', 'c', '4', 'x', 'y','2', 'a', 'b']
print('----------')
#print(vars_order)
print('----------')
order_string = make_string(vars_order)

order_level = 0
max_order = len(order_string)/amount_of_entries
#+++++++++++++++++++++++++

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

        #+++++++++++++++++++++++++
        amount_of_available_vars = level*amount_of_entries
        if amount_of_available_vars > len(order_string):
            av_vars = order_string + make_string(prior_per_dict.values())
        else: 
            av_vars = order_string[0:amount_of_available_vars] + make_string(prior_per_dict.values())
        print(av_vars)
        #+++++++++++++++++++++++++


# -------------- nado menyat' tut ------------------------------------------
        for i in range(len(s)-1):
            if i > 0 and i < len(s) - 1 and s[i] in '+-*/^':
                if (s[i-2]) not in '()' and (s[i+2]) not in '()':
                    if (pr(s[i-2]) <= pr(s[i])) and (pr(s[i+2]) <= pr(s[i])):
                        if s[i-1:i+2] != '' and ('(' not in s[i-1:i+2]) and (')' not in s[i-1:i+2]):
                            if s[i-1] in av_vars and s[i+1] in av_vars: ####################################################
                                prior_dict[pr(s[i])].append(s[i-1:i+2])
                
                if (s[i] == '-') and (s[i-1] in "+-*/^") and (s[i+2] in "+-*/^"):
                    if s[i-1] in av_vars and s[i+1] in av_vars: ###########################################################
                        prior_dict[unar_sign].append(s[i:i+2])

        
# -----------------------------brackets_code--------------------------------
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

        print('prior_dict_current is         ', prior_dict)
# --------------------------------------------------------------------------
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
        print(vars_order)
        
        with open('/home/paro/Desktop/project/input_to_help.txt','w')  as inf:
            json.dump(prior_per_dict, inf)
        with open('/home/paro/Desktop/project/input_to_help_1.txt','w') as inf:
            json.dump(per_dict, inf)
        
    return s
   
recurs(inp_s)       

