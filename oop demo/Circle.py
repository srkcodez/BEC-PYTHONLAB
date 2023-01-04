class Circle:
    def __init__(self):
        self.radius = 5

    def __init__(self, r):
        self.radius = r

    def area(self):
        print(self.radius ** 2 * 3.14)

    def perimeter(self):
        print(2 * self.radius * 3.14)


c1 = Circle()

c1.area()
c1.perimeter()

c2 = Circle(10)
c2.area()
c2.perimeter()
