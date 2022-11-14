import json
from math import log2
import time
import functions 
from functions import get_sign as g_s
from functions import get_level as lvl
from math import ceil
import functions_for_rtl 


with open('/home/paro/Desktop/project/input_to_help.txt','r')  as inf:
    prior_per_dict = json.load(inf) # "1": ["A", "B"], "2": ["C", "D"]
with open('/home/paro/Desktop/project/input_to_help_1.txt','r')  as inf:
    per_dict = json.load(inf)  # "A": "2*a", "B": "3*a",
with open('/home/paro/Desktop/project/vars.txt','r')  as inf:
    vars_list = json.load(inf)  # "a", "y", "c", "x", "b"
with open('/home/paro/Desktop/project/levels.txt','r')  as inf:
    levels_dict = json.load(inf) # "a": 2, "y": 5, "c": 2, "x": 3, "b": 
#--------------------------------------

N = 32

ln = len(levels_dict)
lst_key = list(levels_dict.keys())[ln-1]
lst_value = list(levels_dict.values())[ln-2] + 1
levels_dict[lst_key] = lst_value


size_dict = functions_for_rtl.size_dict(N, vars_list, per_dict)
size_dict['3'] = 2  #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
last_key, last_value = functions.last_element(size_dict)
times = ceil(last_value/N)
amount = int(log2(len(vars_list)+times)) + 1 
bit_row = functions.bit_amount(amount)
#------------------------------------------------

with open('/home/paro/Desktop/project/rtl.v','w') as inf:

    functions_for_rtl.declaration(inf, amount, N)
    functions_for_rtl.vars_declarations(inf, vars_list, levels_dict, N)


    for k,v in per_dict.items():
        # k = name of var f.e. A B C 
        # v = description of vars, 2*a, 3*a, A*a

        level_of_var = lvl(k)
        max_level_of_var = levels_dict[k]
        #level_of_var = 0

        s_2 = functions_for_rtl.making_s_2(k, v, level_of_var, vars_list, per_dict) #
        t_size = size_dict[k]
        adr = functions.choose_size_for_per(N, t_size)
        functions_for_rtl.CHANGE_NAME(inf, k, level_of_var, s_2, t_size) #
        lvl_v = level_of_var
        level_of_var = functions_for_rtl.wire_register(inf, max_level_of_var, t_size, k, lvl_v) #

    i = functions_for_rtl.registers_RF_res(inf, N, times, last_key, level_of_var)
    i += 1

    s_0 = '\nwire [N-1:0] RF_Res_'+ str(i-1) + ';\n'
    inf.write(s_0)
    adr = functions.choose_size(N, N*i - 1)
    koef = adr[-2]

    ostatok = (int(koef)+1)*N - last_value
    print(ostatok)

    print('adr1 =======       ',adr)
    adr = adr[6:] #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    s_5 = 'register #(1,"sync","posedge",0,0,N,'
    s_5 += str(N) + '\'d0)register_RF_Res_'+ str(i-1)+'(.i_clk(i_clk), .i_reset(i_reset), .i_EN(1\'b0), .i_d({{' + str(ostatok) + "{in_"
    s_5 += str(last_key) + str(level_of_var) + "["+ str(last_value) + "]}},in_" + str(last_key)
    s_5 += str(level_of_var) + "["+ str(last_value) +  adr + '}), .o_d(RF_Res_'+ str(i-1)+'));\n'
    inf.write(s_5)
    print('print adr2 ======      ',adr)

    num = functions_for_rtl.end_file(inf, vars_list, amount, bit_row)
    functions_for_rtl.RF_file(inf, amount, times, bit_row, num)
