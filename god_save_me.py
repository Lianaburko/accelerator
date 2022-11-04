import json 

with open('/home/paro/Desktop/project/input_to_help.txt','r')  as inf:
    prior_per_dict = json.load(inf) # {"1": ["A", "B"], "2": ["C", "D"], "3": ["E", "F"], "4": ["G", "H"], "5": ["I", "J"], "6": ["K"], "7": ["L"]}
with open('/home/paro/Desktop/project/input_to_help_1.txt','r')  as inf:
    per_dict = json.load(inf)  # {"A": "2*a", "B": "3*a", "C": "A*a", "D": "B*c", "E": "4*x", "F": "x*x", "G": "C*b", "H": "E*F", "I": "H*y", "J": "G+D", "K": "J-I", "L": "K+3"}
with open('/home/paro/Desktop/project/vars.txt','r')  as inf:
    vars_list = json.load(inf)  # ["a", "y", "c", "x", "b"]
with open('/home/paro/Desktop/project/levels.txt','r')  as inf:
    levels_dict = json.load(inf) # {"a": 2, "y": 5, "c": 2, "x": 3, "b": 4, "A": 2, "B": 2, "C": 4, "D": 5, "E": 4, "F": 4, "G": 5, "H": 5, "I": 6, "J": 6, "K": 7, "L": 100}


print(levels_dict)
ln = len(levels_dict)
lst_key = list(levels_dict.keys())[ln-1]
lst_value = list(levels_dict.values())[ln-2] + 1
levels_dict[lst_key] = lst_value
print(lst_key)
print(lst_value)
print(levels_dict)