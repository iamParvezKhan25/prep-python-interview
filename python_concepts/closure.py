def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function


clouser = outer_function(5)
result = clouser(5)
print(result)
