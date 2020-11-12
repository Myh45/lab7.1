import math


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def square(self):
        p = self.perimeter() / 2
        return math.sqrt(p * ((p - self.a) * (p - self.b) * (p - self.c)))


class RivnobedTriangle(Triangle):
    def __init__(self, a, b, c):
        Triangle.__init__(self, a, b, a)

    def __str__(self):
        return str(self.a) + " " + str(self.b) + " " + str(self.a)

    def square(self):
        h = math.sqrt(self.b*self.b - self.a*self.a/4)
        return self.a*h/2


class RivnostorTriangle(RivnobedTriangle):
    def __init__(self,a,b,c):
        RivnobedTriangle.__init__(self, a, a, a)

    def __str__(self):
        return str(self.a) + " " + str(self.a) + " " + str(self.a)

    def square(self):
        return (self.a*self.a * math.sqrt(3))/4


tr1 = Triangle(3, 6, 4)
tr2 = RivnobedTriangle(24, 13, 24)
tr3 = RivnostorTriangle(7, 7, 7)
print("Периметр трикутника:", tr1.perimeter())
print("Площа трикутника:", tr1.square())
print("Площа рівнобедреного трикутника:", tr2.square())
print("Площа рівностороннього трикутника:", tr3.square())