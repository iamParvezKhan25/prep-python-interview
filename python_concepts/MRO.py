"""
        A
     /     \
    B       C
      \    /
        D
"""


class A:
    def show(self):
        print('class A')


class B(A):
    def show(self):
        print('class B')


class C(A):
    def show(self):
        print('class C')


class D(C, B):
    pass


obj = D()
obj.show()

print(D.__mro__)
print(D.mro())
