class MyIterarator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            value = self.start
            self.start += 1
            return value
        else:
            raise StopIteration()


def my_generator(start, end):
    value = start
    while value < end:
        yield value
        value += 1


obj = MyIterarator(1, 5)
for i in obj:
    print(i)

obj_gen = my_generator(6, 10)
for j in obj_gen:
    print(j)