import json

with open('/home/paro/Desktop/project/input_to_help.txt','r')  as inf:
    prior_per_dict = json.load(inf) # {"1": ["A", "B"], "2": ["C"]}

print(prior_per_dict)
for k,v in prior_per_dict:
    print(type(k),'\n',type(v))