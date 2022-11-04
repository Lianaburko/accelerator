#-------------------------------------------------------------------------------------------------------------------------------
import json
from itertools import permutations
import time

# function for getting list of variables
def get_list_of_vars(s):
    list_vars = []
    set_vars = set()
    i = 0 
    while i < len(s):
        l_s = ''
        while i < len(s) and s[i] not in '+-*/()': # Можно сделать ключи co словаря с операциями
            l_s += s[i]
            i += 1
        i += 1
        if l_s != '':
            list_vars.append(l_s)
            set_vars.add(l_s) # set with variables
     
    return list_vars

#-------------------------------------------------------------------------------------------------------------------------------
def order_of_vars(l_s):
    vars = {}
    for i in l_s:
        if i in vars.keys():
            vars[i] += 1
        else:
            vars[i] = 1
    k = 3
    order_list = []
    while(k != 0):
        for i,j in vars.items():
            if j == k:
                order_list.append(i)
        k -= 1

    return order_list
#-------------------------------------------------------------------------------------------------------------------------------

# function for getting list of signs
def get_list_of_signs(s):
    list_signs = []
    for i in s:
        if i in '+-/*()':
            list_signs.append(i)

    return list_signs

#-------------------------------------------------------------------------------------------------------------------------------

# function for getting list of both signs and numbers
def get_list_of_all_expr(s):
    list_expr = []
    i = 0 
    while i < len(s):
        l_s = ''
        while i < len(s) and s[i] not in '+-*/()': # Можно сделать ключи co словаря с операциями
            l_s += s[i]
            i += 1
        if l_s != '':
            list_expr.append(l_s)
        list_expr.append(s[i])
        i += 1
        
     
    return list_expr

#-------------------------------------------------------------------------------------------------------------------------------
# function for creating priority dict 
# reading from the file             
def import_signs():
    signs_dict = {}
    with open("/home/paro/Desktop/project/signs.txt") as file:
        for line in file:
            signs_dict[line[2]] = int(line[0])
    
    return signs_dict

#-------------------------------------------------------------------------------------------------------------------------------

def creating_per_dict():
    priority = import_signs()
    value_set = set()
    per_dict = {}
    for i in priority.values():
        value_set.add(i)
    for i in value_set:
        if i not in per_dict.keys():
            per_dict[i] = []
    unar = max(value_set)+1
    per_dict[unar] = []
    return per_dict, unar

#-------------------------------------------------------------------------------------------------------------------------------

def priority(sign):
    priority_sign = import_signs()
    if sign in priority_sign.keys():
        return priority_sign[sign]
    else: 
        return 1000

#-------------------------------------------------------------------------------------------------------------------------------
def make_string(l):
    s = ''
    for i in l:
        s += str(i)
    return s


def make_vars_string(l):
    s = ''
    for i in l:
        if i not in '"][+-*/^(), ':
            s += str(i)
    return s
#-------------------------------------------------------------------------------------------------------------------------------
def get_sign(s):
    for i in s:
        if i in '+-/*()':
            return i 
#-------------------------------------------------------------------------------------------------------------------------------
def choose_size(N,num):
    koef = 1
    while num > N*koef:
        koef += 1
    
    s = '[N*' + str(koef) + '-1:N*' + str(koef-1)+']'
    return s
#-------------------------------------------------------------------------------------------------------------------------------
def choose_size_for_per(N,num):
    koef = 1
    while num > N*koef:
        koef += 1
    
    s = '[N*' + str(koef) + '-1:0]'
    return s
#-------------------------------------------------------------------------------------------------------------------------------
def last_element(dct):
    key = 0
    value = 0
    for k,v in dct.items():
        key = k
        value = v
    return key, value
#-------------------------------------------------------------------------------------------------------------------------------
def bit_amount(amount):

    bit_row = ['0','1']
    while amount > 1:
        bit_row = bit_row + bit_row
        amount -= 1
        for i in range(len(bit_row)):
            if i < len(bit_row)/2:
                bit_row[i] = '0' + bit_row[i]
            else:    
                bit_row[i] = '1' + bit_row[i]
    
    return bit_row
#-------------------------------------------------------------------------------------------------------------------------------

def future_vars(var_dict, level_dict,level):

    r_list = []
    for i in level_dict.keys():
        if int(i) > level:
            for j in level_dict[i]:
                r_list += get_list_of_vars(var_dict[j])

    a = set()
    for i in r_list:
        #if str(i) not in '1234567890':
        a.add(i)

    print(a)
    #time.sleep(1)
    return a
#-------------------------------------------------------------------------------------------------------------------------------
def current_vars(var_dict, level_dict,level):
    r_list = []
    for i in level_dict.keys():
        if int(i) <= level:
            for j in level_dict[i]:
                r_list += get_list_of_vars(var_dict[j])

    a = set()
    for i in r_list:
        #if str(i) not in '1234567890':
        a.add(i)
    print(a)
    #time.sleep(1)
    return a
#-------------------------------------------------------------------------------------------------------------------------------
def combs():
    file = open('/home/paro/Desktop/project/vars.txt','r')
    vars = file.readline()
    print(vars)

    s = make_vars_string(vars)
    print(s)
    perm_set = permutations(s)
    return perm_set
#-------------------------------------------------------------------------------------------------------------------------------


# function for getting list of variables
def vars_without_numbers(s):
    list_vars = []
    set_vars = set()
    i = 0 
    while i < len(s):
        l_s = ''
        while i < len(s) and s[i] not in '+-*/()1234567890': # Можно сделать ключи co словаря с операциями
            l_s += s[i]
            i += 1
        i += 1
        if l_s != '':
            list_vars.append(l_s)
            set_vars.add(l_s) # set with variables
    
    return set_vars

#-------------------------------------------------------------------------------------------------------------------------------

def numbers(s):
    list_vars = []
    set_vars = set()
    i = 0 
    while i < len(s):
        l_s = ''
        while i < len(s) and s[i] in '1234567890': 
            l_s += s[i]
            i += 1
        i += 1
        if l_s != '':
            list_vars.append(l_s)
            set_vars.add(l_s) # set with variables
     
    return list_vars
#-------------------------------------------------------------------------------------------------------------------------------
def try_to_simplify(s):
    i = 0
    exp = ''
    lst_exp = []
    while(i < len(s)): 
        if s[i] in '+-':
            lst_exp.append(exp)
            exp = ''
            
        exp += s[i]
        i += 1
    lst_exp.append(exp)

    
    print(set(lst_exp[0]) & set(lst_exp[1]))

    return lst_exp
#-------------------------------------------------------------------------------------------------------------------------------
def two_pow(n):    
    i = 1
    while i < n:
        i = i * 2
    if i == n:
        return 1
    else:
        return 0

#-------------------------------------------------------------------------------------------------------------------------------
def check_number(a,b):
    if a in '1234567890':
        if two_pow(int(a)) == 1:
            return 'hello'
    if b in '1234567890':
        if two_pow(int(b)) == 1:
            return 'hello'
    
    return -1

#--------------------------------------------------------
def matrix_making():
    with open('/home/paro/Desktop/project/input_to_help_1.txt','r')  as inf:
        var_dict = json.load(inf)  # {"A": "a-b", "B": "c+d", "C": "A*B"}
    with open('/home/paro/Desktop/project/input_to_help.txt','r')  as inf:
        level_dict = json.load(inf) # {"1": ["A", "B"], "2": ["C"]}
    with open('/home/paro/Desktop/project/vars.txt','r')  as inf:
        var_list = json.load(inf) # ["a", "y", "c", "x", "b"]

    all_vars = var_list + list(var_dict.keys())

    matrix = {}
    for i in all_vars:
        matrix[i] = {}
        for j in level_dict.keys():
            print(future_vars(var_dict, level_dict, int(j)))
            #time.sleep(1)
            if i in  future_vars(var_dict, level_dict, int(j)):
                matrix[i][j] = '+'
            else:
                matrix[i][j] = '-'
    
    for i in matrix:
        print(i,'      ',matrix[i])

    dict_end = {}
    for i,j in matrix.items():            
        max = 0
        for k,v in j.items():
            if v == '+':
                max = int(k) + 1 
        
        dict_end[i] = max
    
    
    print(dict_end)
    with open('/home/paro/Desktop/project/levels.txt','w') as inf:
        json.dump(dict_end, inf)

#------------------------------------------------------------------------------
def get_level(sign):
    with open('/home/paro/Desktop/project/input_to_help.txt','r')  as inf:
        prior_per_dict = json.load(inf) # {"1": ["A", "B"], "2": ["C", "D"], "3": ["E", "F"], "4": ["G", "H"], "5": ["I", "J"], "6": ["K"], "7": ["L"]}

    for k,v in prior_per_dict.items():
        if sign in v:
            return int(k)



s = '2*a*a*b+3*a*c-4*x*x*x*y+3'
#vars = get_list_of_vars(s)
#kek = order_of_vars(vars)
#print(vars)
#print(kek)



