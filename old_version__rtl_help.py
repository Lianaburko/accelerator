import json
from math import log2
from functions import get_sign as g_s

# pri slozheniii

with open('/home/paro/Desktop/project/input_to_help.txt','r')  as inf:
    prior_per_dict = json.load(inf) # {"1": ["A", "B"], "2": ["C"]}
with open('/home/paro/Desktop/project/input_to_help_1.txt','r')  as inf:
    per_dict = json.load(inf)  # {"A": "a-b", "B": "c+d", "C": "A*B"}
with open('/home/paro/Desktop/project/vars.txt','r')  as inf:
    vars_list = json.load(inf)  # ["a", "b", "c", "d"]


#-------------------------------------------------------
size_dict = {}
for i in vars_list:
    size_dict[i] = 16

for k,v in per_dict.items():
    size = 0 
    sign = g_s(v)
    first = size_dict[v[0]]
    second = size_dict[v[2]]
    if sign == '+':
        if first > second:
            size = first
        elif first == second:
            size = first + 1
        else: 
            size = second
    elif sign == '-':
        if first > second:
            size = first
        else: 
            size = second
    elif sign == '*':
        size = first + second
    
    size_dict[k] = size
    

#------ why -----
N = 16
amount = int(log2(len(vars_list))) + 1
bit_row = ['000','001','010','011','100','101','110','111']
#------------------------------------------------




with open('/home/paro/Desktop/project/rtl.v','w') as inf:
################## declaration  ################## 
    inf.write('`timescale 1ns/100ps\n\n')
    inf.write('module top #(\n')
    inf.write('parameter N = '+ str(N) +',\n') 
    inf.write('parameter RF_Addr_BITNES = '+ str(amount) +'\n') 
    inf.write(')(\n') 
    inf.write('input wire i_clk, i_reset,\n') 
    inf.write('input wire [RF_Addr_BITNES-1:0] i_addr,\n') 
    inf.write('input wire [N-1:0] i_data,\n') 
    inf.write('output reg [N-1:0] o_data,\n') 
    inf.write('input wire i_RF_WE\n') 
    inf.write(');\n\n') 
################# peremennie  ##################

    for i in vars_list:
        s = 'reg [N-1:0] RF_' + str(i) + ';\n'
        inf.write(s)

    inf.write('\nwire [N-1:0] RF_Res_0;\n')
    inf.write('wire [N-1:0] RF_Res_1;\n\n')

    for k,v in per_dict.items():
        s_2 = 'assign in_' + k + ' = '
        if str(v[0]) in vars_list: 
            s_2 += ' RF_'
        s_2 += str(v[0])+str(v[1])
        if str(v[2]) in vars_list: 
            s_2 += ' RF_'
        s_2 += str(v[2])+';\n' 


        if v[1] in '+-':
            s_1 = 'wire [N-1:0] in_' + k +';\n'
            s_3 = 'wire [N-1:0] ' + k + ';\n'
        elif v[1] in '*/':
            s_1 = 'wire [N*2-1:0] in_'  + k +';\n'
            s_3 = 'wire [N*2-1:0] ' + k + ';\n'
        else: 
            'i dont know'

        s_4 = 'register #(1,"sync","posedge",0,0,N,'+str(N)+'\'d0)register_'+ k 
        s_4 += '(.i_clk(i_clk), .i_reset(i_reset), .i_EN(1\'b0), .i_d(in_'+k+'), .o_d('+k+'));\n'
        
        inf.write(s_1)
        inf.write(s_2)
        inf.write(s_3)
        inf.write(s_4)
        inf.write('\n')

## in_C  replace 
## razryadnoct 
## height restriction in adders 

    inf.write('register #(1,"sync","posedge",0,0,N,'+str(N)+'\'d0)register_RF_Res_0(.i_clk(i_clk), .i_reset(i_reset), .i_EN(1\'b0), .i_d(in_C[N-1:0]), .o_d(RF_Res_0));\n')
    inf.write('register #(1,"sync","posedge",0,0,N,'+str(N)+'\'d0)register_RF_Res_1(.i_clk(i_clk), .i_reset(i_reset), .i_EN(1\'b0), .i_d(in_C[2*N-1:N]), .o_d(RF_Res_1));\n')
    inf.write('\n')

    inf.write('always@(posedge i_clk) begin\n')
    inf.write(' case(i_addr)')


    num = 0
    for i in vars_list:
        s_1 = str(amount) + '\'b' + bit_row[num] + ': begin\n'
        s_2 = 'o_data <= RF_'+ i +';\n'
        s_3 = 'if(i_RF_WE == 1\'b1) begin\n'
        s_4 = 'RF_'+ i +' <= i_data;\n'
        s_5 = 'end\n'
        inf.write(s_1)
        inf.write(s_2)
        inf.write(s_3)
        inf.write(s_4)
        inf.write(s_5)
        inf.write(s_5)
        inf.write('\n')
        num += 1
    
    for i in range(0,2,1):
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
