class Calculator:
    def add(self, x, y):
        print('actual addition.')
        return x + y


def psudo_add(self, p, q):
    print('psudo addition')
    return p * q


obj = Calculator()
print(obj.add(2, 3))

Calculator.add = psudo_add
print(obj.add(2, 3))
