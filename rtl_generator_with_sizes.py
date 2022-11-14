import json
from math import log2
import time
import functions 
from functions import get_sign as g_s
from functions import get_level as lvl
from math import ceil
import functions_for_rtl

# pri slozheniii

with open('/home/paro/Desktop/project/input_to_help.txt','r')  as inf:
    prior_per_dict = json.load(inf) # "1": ["A", "B"], "2": ["C", "D"]
with open('/home/paro/Desktop/project/input_to_help_1.txt','r')  as inf:
    per_dict = json.load(inf)  # "A": "2*a", "B": "3*a",
with open('/home/paro/Desktop/project/vars.txt','r')  as inf:
    vars_list = json.load(inf)  # "a", "y", "c", "x", "b"
with open('/home/paro/Desktop/project/levels.txt','r')  as inf:
    levels_dict = json.load(inf) # "a": 2, "y": 5, "c": 2, "x": 3, "b": 


#-------------------------------------------------------
N = 32

ln = len(levels_dict)
lst_key = list(levels_dict.keys())[ln-1]
lst_value = list(levels_dict.values())[ln-2] + 1
levels_dict[lst_key] = lst_value

print(levels_dict)
#time.sleep(10)

size_dict = functions_for_rtl.size_dict(N, vars_list, per_dict)

size_dict['3'] = 2 # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


last_key, last_value = functions.last_element(size_dict)
times = ceil(last_value/N)
amount = int(log2(len(vars_list)+times)) + 1 

bit_row = functions.bit_amount(amount)
#------------------------------------------------

with open('/home/paro/Desktop/project/rtl.v','w') as inf:
################## declaration  ################## 
    functions_for_rtl.declaration(inf, amount, N)


################# peremennie  ##################
    for i in vars_list:
        s = 'reg [N-1:0] RF_' + str(i) + '0;\n'
        inf.write(s)
    for i in vars_list:
        level_of_var = 0
        print(i)
        #time.sleep(2)
        max_level_of_var = levels_dict[i]
        if max_level_of_var == 0:
            max_level_of_var = 0
            a = 0
        else:
            a = 1
        print(max_level_of_var)
        #time.sleep(3)
        while(a != max_level_of_var):
            s = 'wire [N-1:0] RF_' + str(i)+str(a) + ';\n'
            an_str = "register #(1,\"sync\",\"posedge\",0,0,32,16\'d0)register_" + str(i)+str(a) + "(.i_clk(i_clk), .i_reset(i_reset), .i_EN(1'b1), .i_d(RF_"+ str(i)+str(a-1) + "), .o_d(RF_"+ str(i)+str(a) + "));\n"
            inf.write(s)
            inf.write(an_str)
            a += 1


    for k,v in per_dict.items():

        # k = name of var f.e. A B C 
        # v = description of vars, 2*a, 3*a, A*a

        level_of_var = lvl(k)
        max_level_of_var = levels_dict[k]

        print('k = ', k , 'v = ', v, 'level_of_var = ', level_of_var, 'max_level_of_var = ', max_level_of_var)
        
        s_2 = 'assign in_' + k + str(level_of_var) + ' = '
        if str(v[0]) in vars_list: 
            print(v[0])
            #time.sleep(1)
            s_2 += ' RF_'
        s_2 += str(v[0])+ str(level_of_var -1) +str(v[1])

        if str(v[2]) in vars_list:
            print(v[2])
            #time.sleep(1) 
            s_2 += ' RF_'
        s_2 += str(v[2])+ str(level_of_var -1) + ';\n' 

        print(s_2)

        t_size = size_dict[k]
        adr = functions.choose_size_for_per(N, t_size)

        s_1 = 'wire ' + '[' + str(t_size - 1) + ':0] in_' + k + str(level_of_var)  +';\n'
        s_3 = 'wire ' + '[' + str(t_size - 1) + ':0] ' +k + str(level_of_var) + ';\n'


        s_4 = 'register #(1,"sync","posedge",0,0,' + str(t_size) + ',' + str(N) +'\'d0)register_'+ k + str(level_of_var) 
        s_4 += '(.i_clk(i_clk), .i_reset(i_reset), .i_EN(1\'b0), .i_d(in_'+k+ str(level_of_var) + '), .o_d('+k+ str(level_of_var) +'));\n'
        
        inf.write(s_1)
        inf.write(s_2)
        inf.write(s_3)
        inf.write(s_4)
        inf.write('\n')

        while(level_of_var != max_level_of_var - 1):
            level_of_var += 1 
            s_3 = 'wire ' + '[' + str(t_size - 1) + ':0] ' +k + str(level_of_var) + ';\n'
            s_4 = 'register #(1,"sync","posedge",0,0,' + str(t_size) + ',' + str(N) +'\'d0)register_'+ k + str(level_of_var) 
            s_4 += '(.i_clk(i_clk), .i_reset(i_reset), .i_EN(1\'b0), .i_d('+k+ str(level_of_var - 1)+ '), .o_d('+k+ str(level_of_var) +'));\n'
            inf.write(s_3)
            inf.write(s_4)
            inf.write('\n')

    i = 0
    print('the times is',times)
    while(i < times):
        i += 1
        s_0 = '\nwire [N-1:0] RF_Res_'+ str(i-1) + ';\n'
        inf.write(s_0)
        adr = functions.choose_size(N, N*i - 1)
        s_5 = 'register #(1,"sync","posedge",0,0,N,'
        s_5 += str(N) + '\'d0)register_RF_Res_'+ str(i-1)+'(.i_clk(i_clk), .i_reset(i_reset), .i_EN(1\'b0), .i_d(in_'
        s_5 += str(last_key) + str(level_of_var) + str(adr) +'), .o_d(RF_Res_'+ str(i-1)+'));\n'
        inf.write(s_5)
    
    inf.write('\n')

    inf.write('always@(posedge i_clk) begin\n')
    inf.write(' case(i_addr)')


    num = 0
    for i in vars_list:
        s_1 = str(amount) + '\'b' + bit_row[num] + ': begin\n'
        s_2 = 'o_data <= RF_'+ i +'0;\n'
        s_3 = 'if(i_RF_WE == 1\'b1) begin\n'
        s_4 = 'RF_'+ i + '0 <= i_data;\n'
        s_5 = 'end\n'
        inf.write(s_1)
        inf.write(s_2)
        inf.write(s_3)
        inf.write(s_4)
        inf.write(s_5)
        inf.write(s_5)
        inf.write('\n')
        num += 1
    
    for i in range(0,times,1):
        s_1 = str(amount) + '\'b' + bit_row[num] + ': begin\n'
        s_2 = 'o_data <= RF_Res_' + str(i) + ';\n'
        s_3 = 'end\n'
        inf.write(s_1)
        inf.write(s_2)
        inf.write(s_3)
        num += 1

    inf.write('endcase\n')
    inf.write('end\n')
    inf.write('endmodule\n')
