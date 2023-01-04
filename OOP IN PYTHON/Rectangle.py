class Rectangle:
    def __init__(self, len, br):
        self.len = len
        self.br = br

    def area(self):
        print(self.len * self.br)

    def perimeter(self):
        print(2 * (self.len + self.br))


r1 = Rectangle(10, 20)

r1.area()
r1.perimeter()
