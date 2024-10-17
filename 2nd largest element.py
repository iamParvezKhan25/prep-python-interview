arr = [25, 11, 95, 15, 12, 96]

max1 = float('-inf')
max2 = float('-inf')

for i in arr:
    if i > max1:
        max2 = max1
        max1 = i
    elif i > max2 and i != max1:
        max2 = i

print(max2)
