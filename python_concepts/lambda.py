"""
single use function
"""

addition = lambda x, y: x + y
print(addition(2, 3))


"""
pass function as an argument
"""


def applying_function(func, numbers):
    response = []
    for i in numbers:
        response.append(func(i))
    return response


result = applying_function(lambda x: x * x, [1, 2, 3, 4, 5])
print(result)
