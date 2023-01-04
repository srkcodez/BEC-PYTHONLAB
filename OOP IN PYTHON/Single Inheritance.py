class A:
    def __init__(self, a):
        self.a = a

    def disp(self):
        print(self.a)


class B(A):
    def __init__(self, a, b):
        self.b = b
        A.__init__(self, a)

    def disp(self):
        print(self.a)
        print(self.b)


t = B(10, 20)

t.disp()
