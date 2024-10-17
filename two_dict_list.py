input_a = {"a": 1, "b": 2, "c": 3}
input_b = {"b": 3, "d": 4, "c": 5}
result = {}

# Combine values from input_a
for key, value in input_a.items():
    if key in result:
        if not isinstance(result[key], list):
            result[key] = [result[key]]
        result[key].append(value)
    else:
        result[key] = value

# Combine values from input_b
for key, value in input_b.items():
    if key in result:
        if not isinstance(result[key], list):
            result[key] = [result[key]]
        result[key].append(value)
    else:
        result[key] = value

print(result)

