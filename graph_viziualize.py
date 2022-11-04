import json

with open('/home/paro/Desktop/project/input_to_help.txt','r')  as inf:
    prior_per_dict = json.load(inf) # {"1": ["A", "B"], "2": ["C"], "3": ["D"],
with open('/home/paro/Desktop/project/input_to_help_1.txt','r')  as inf:
    per_dict = json.load(inf)

letters = {}
list_pers = []
counter = 0
letters_list = []
colors = ['turquoise','darkolivegreen1','gold','tomato','deepskyblue','palegreen','pink','cyan', 'olive', 'mediumturquoise', 'tan', 'maroon', 'fuchsia', 'tomato']

for value in per_dict.values():
    for j in value:
        if j not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ+-*/^":
            if j not in letters.values():
                letters[counter] = j
            if j not in letters_list:
                letters_list.append(j)
                counter += 1

print(letters)
print(letters_list)
struct = 'fun [label="<f'

for tup in letters.keys():
    struct += str(tup) + '> ' + str(letters[tup]) + '|<f'

with open('/home/paro/Desktop/project/graph.gv','w') as inf:
    inf.write('digraph structs {')
    inf.write('\n')
    inf.write('node [shape=record, style="rounded,filled"];')
    inf.write('\n')

    my_str = ''
    for i in prior_per_dict.keys():
        my_str += 'level' + str(i) + '->'
    my_str = my_str[:-2] + ';\n'

    inf.write('{')
    inf.write('\n')
    inf.write('node[shape=plaintext, fillcolor=snow];')
    inf.write('\n')
    inf.write('edge[color=white];')
    inf.write('\n')
    inf.write(my_str)
    inf.write('}\n')


    inf.write(struct[:-3] + '", fillcolor=' + colors[0] +'];')
    inf.write('\n')


color_number = 0
for key in prior_per_dict.keys():
    color_number += 1
    new_list = []
    for j in prior_per_dict[key]: # j = A,B,C
        if j not in list_pers:
            list_pers.append(j)
            struct_syn = 'struct' + str(list_pers.index(j)) + ' [label="<f0> ' + str(j) + '|<f1> = ' + str(per_dict[j]) + '", fillcolor=' + colors[color_number] +'];'
            new_list.append(list_pers.index(j))
            with open('/home/paro/Desktop/project/graph.gv','a') as inf:
                inf.write(struct_syn)
                inf.write('\n')
    
    struct = ""    
    for i in new_list:
        struct += " struct" + str(i) + ';'
        
    str_struct = "{rank = same; level" + str(color_number) + '; ' + struct + '}'
    with open('/home/paro/Desktop/project/graph.gv','a') as inf:
        inf.write(str_struct)
        inf.write('\n')


#print(list_pers)

for key in prior_per_dict.keys():
    for j in prior_per_dict[key]:
        vir = ''
        expr = per_dict[j]
        if len(expr) == 3:
            if expr[0] in letters_list:
                vir += 'fun:f' + str(letters_list.index(expr[0])) + '->'
            elif expr[0] in list_pers:
                vir += 'struct' + str(list_pers.index(expr[0])) + ':f0' + '->'
            vir += 'struct' + str(list_pers.index(j)) +':f0' + ';'
            with open('/home/paro/Desktop/project/graph.gv','a') as inf:
                inf.write(vir)
                inf.write('\n')
            vir = ''
            if expr[2] in letters_list:
                vir += 'fun:f' + str(letters_list.index(expr[2])) + '->'
            elif expr[2] in list_pers:
                vir += 'struct' + str(list_pers.index(expr[2])) + ':f0' + '->'
            vir += 'struct' + str(list_pers.index(j)) +':f0' + ';'
            with open('/home/paro/Desktop/project/graph.gv','a') as inf:
                inf.write(vir)
                inf.write('\n')
        if len(expr) == 2:
            if expr[1] in letters_list:
                vir += 'fun:f' + str(letters_list.index(expr[1])) + '->'
            elif expr[1] in list_pers:
                vir += 'struct' + str(list_pers.index(expr[1])) + ':f0' + '->'
            vir += 'struct' + str(list_pers.index(j)) +':f0' + ';'
            with open('/home/paro/Desktop/project/graph.gv','a') as inf:
                inf.write(vir)
                inf.write('\n')


with open('/home/paro/Desktop/project/graph.gv','a') as inf:
        inf.write('}')



