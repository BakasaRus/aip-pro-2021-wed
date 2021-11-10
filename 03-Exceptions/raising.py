class GeometryError(ValueError):
    def __init__(self, description):
        self.description = description

    def __str__(self):
        return self.description


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        if isinstance(other, Point):
            return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        else:
            raise GeometryError("Передана не точка")


print(__name__)
p1 = Point(0, 0)
p2 = Point(3, 3)
print(p1.dist(p2))
print(p1.dist(8))
