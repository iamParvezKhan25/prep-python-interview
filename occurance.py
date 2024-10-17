input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 4, 6, 8]
occurance = {}

for i in input_list:
    if i in occurance:
        occurance[i] += 1
    else:
        occurance[i] = 1

print(occurance)
