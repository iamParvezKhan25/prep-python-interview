arr = {'b': 35, 'a': 5, 'c': 15}
print("Before : ", arr)

result = dict(sorted(arr.items(), key=lambda item: item[1]))
print("After :", result)
