class A:
    def __init__(self):
        print('a')
    def fun1(self):
        print('fun1')
    def fun1(self,x):
        print(x)


class B(A):
    def __init__(self):
        print('b')
    def fun1(self):
        print("b fun1")

class C(B):
    def __init__(self):
        print('c')


t = C()

l= B()
l.fun1()
k=A()
k.fun1(10)