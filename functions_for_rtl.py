import json 
from functions import get_sign as g_s
import functions

def size_dict(N, vars_list, per_dict):
    size_dict = {}
    for i in vars_list:
        size_dict[i] = N

    for k,v in per_dict.items():
        size = 0 
        sign = g_s(v)
        first = size_dict[v[0]]
        second = size_dict[v[2]]
        if sign == '+':
            size = N+1
        elif sign == '-':
            if first > second:
                size = first
            else: 
                size = second
        elif sign == '*':
            size = 2*N
    
        size_dict[k] = size

    return size_dict

def vars_declarations(inf, vars_list, levels_dict, N):
    for i in vars_list:
        s = 'reg [N-1:0] RF_' + str(i) + '0;\n'
        inf.write(s)
    for i in vars_list:
        print(i)
        max_level_of_var = levels_dict[i]
        if max_level_of_var == 0:
            max_level_of_var = 0
            a = 0
        else:
            a = 1
        print(max_level_of_var)
        while(a != max_level_of_var):
            s = 'wire [N-1:0] RF_' + str(i)+str(a) + ';\n'
            an_str = "register #(1,\"sync\",\"posedge\",0,0,"+ str(N)+"," + str(N) 
            an_str += "\'d0)register_" + str(i)+str(a) + "(.i_clk(i_clk), .i_reset(i_reset), .i_EN(1'b1), .i_d(RF_"
            an_str += str(i)+str(a-1) + "), .o_d(RF_"+ str(i)+str(a) + "));\n"
            inf.write(s)
            inf.write(an_str)
            a += 1



def name(inf, max_level_of_var, t_size, k, level_of_var):
    while(level_of_var != max_level_of_var - 1):
        level_of_var += 1 
        s_3 = 'wire ' + '[' + str(t_size - 1) + ':0] ' +k + str(level_of_var) + ';\n'
        s_4 = 'register #(1,"sync","posedge",0,0,' + str(t_size) + ',' + str(t_size) + '\'d0)register_'+ k + str(level_of_var) 
        s_4 += '(.i_clk(i_clk), .i_reset(i_reset), .i_EN(1\'b0), .i_d(' + k + str(level_of_var - 1) + '), .o_d(' + k + str(level_of_var) + '));\n'
        inf.write(s_3)
        inf.write(s_4)
        inf.write('\n')

    return level_of_var

def registers_CORRECT_NAME(inf, N, times, last_key, level_of_var):
    i = 0
    while(i < times-1):
        i += 1
        s_0 = '\nwire [N-1:0] RF_Res_'+ str(i-1) + ';\n'
        inf.write(s_0)
        adr = functions.choose_size(N, N*i - 1)
        s_5 = 'register #(1,"sync","posedge",0,0,N,'
        s_5 += str(N) + '\'d0)register_RF_Res_'+ str(i-1)+'(.i_clk(i_clk), .i_reset(i_reset), .i_EN(1\'b0), .i_d(in_'
        s_5 += str(last_key) + str(level_of_var) + str(adr) +'), .o_d(RF_Res_'+ str(i-1)+'));\n'
        inf.write(s_5)

    return i 


def end_file(inf, vars_list, amount, bit_row):
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

    return num


def RF_file(inf, amount, times, bit_row, num):
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