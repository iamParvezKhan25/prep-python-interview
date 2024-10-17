class Person:
    def __init__(self):
        self.__name = ''

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @name.deleter
    def name(self):
        del self.__name


p = Person()
print('inception')
print(p.name)

print('assign value')
p.name = 'John Doe'
print(p.name)

print('delete value.')
del p.name
# print(p.name)

