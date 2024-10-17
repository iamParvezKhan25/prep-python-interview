d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'a': 5, 'b': 10, 'c': 20}

print("d1 : ", d1)
print("d2 : ", d2)

result = {**d1, **d2}

for key, val in result.items():
    if key in d1 and key in d2:
        result[key] += d1[key]

print("result : ", result)


