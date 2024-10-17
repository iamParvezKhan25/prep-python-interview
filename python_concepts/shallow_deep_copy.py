import copy

"""
Shallow copy
"""
print('shallow copy')
orignal_list = [1, 2, [3, 4]]
print(orignal_list)

shallow_copy = orignal_list.copy()
shallow_copy[2][0] = 25

print(orignal_list)
print(shallow_copy)


"""
deep copy
"""
# orignal_list = orignal_list
print('deep copy')
orignal_list = [1, 2, [3, 4]]
print(orignal_list)

deep_copy = copy.deepcopy(orignal_list)
deep_copy[2][0] = 50

print(orignal_list)
print(deep_copy)
