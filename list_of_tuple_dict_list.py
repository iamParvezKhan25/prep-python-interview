
input_list = [("A", 10), ("B", 20), ("C", 30), ("A", 20)]
output_dict = {}

'''
for key, value in input
output_dict -> key hai 
so append value
output_dict ->key ko list

nahi hai so add kara do key, value
 '''

for key, value in input_list:
    if key in output_dict:
        if isinstance(output_dict[key], list):
            output_dict[key].append(value)
        else:
            output_dict[key] = [output_dict[key], value]
    else:
        output_dict[key] = value

print(input_list)
print(output_dict)
