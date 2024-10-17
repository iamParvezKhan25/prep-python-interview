input_list = [2.5, 3.4, 6.5]


def add_euro_prefix(number):
    return f'EURO {number}'


output_list = list(map(add_euro_prefix, input_list))


print(output_list)
