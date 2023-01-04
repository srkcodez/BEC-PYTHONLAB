class A:
    numob=0
    def __init__(self,val):
        self.__class__.numob+=1
        self.val=val
    def display(self):
        print(self.__class__.numob)
        print(self.val)
class B(A):
    def __init__(self,val,incr):
        self.incr=incr
        A.__init__(self,val)

    def display(self):
        A.display(self)
        print(self.incr)

l1 = A(10)
l1.display()
l2 = A(20)
l2.display()

l3 = B(30,5)
l3.display()