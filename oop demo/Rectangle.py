class Rectangle:
    def __init__(self,length,br):
        self.length=length
        self.br=br
    def area(self):
        print(self.length*self.br)

r1=Rectangle(10,20)

r1.area()
