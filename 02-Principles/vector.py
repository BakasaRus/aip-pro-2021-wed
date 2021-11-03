class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        if isinstance(other, Point):
            return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


class Vector(Point):
    def length(self):
        return self.dist(Point(0, 0))

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    def __rmul__(self, other):
        return self * other

    def __str__(self):
        return f'Vector<x={self.x}, y={self.y}>'


p1 = Point(5, 7)
p2 = Point(6, 6)
print(p1.dist(p2))

v1 = Vector(3, 3)
v2 = Vector(7, -1)
print(v1.length())
print(v1 + v2)
print(v1 - v2)
print(v1 * 2)
print(v2 * 1.5)
print(3 * v1)
print(4.5 * v2)
print(v1 * v2)
