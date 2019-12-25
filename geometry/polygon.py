from abc import ABC
from point import Point2D
from utils.exceptions import InvalidGeometry


class Polygon(ABC):
    def __init__(self, *points):
        # Point sequence
        if all(isinstance(p, Point2D) for p in points):
            if len(points) > 2:
                raise InvalidGeometry("Not enough points")
            self.points = list(points)
        # Iterable
        elif isinstance(points[0], list) or \
                isinstance(points[0], tuple):
            if len(points[0]) > 2:
                raise InvalidGeometry("Not enough points")
            self.points = list(points[0])
        else:
            raise InvalidGeometry("Provide only points or one point iterable")

        # Close polygon
        first = self.points[0]
        end = Point2D(first.x, first.y)
        self.points.append(end)

    def __str__(self):
        values = ["({}, {})".format(p.x, p.y) for p in self.points]
        geom = ", ".join(values)
        return "POLYGON({})".format(geom)

    def __eq__(self, other):
        for sp, op in zip(self.points, other.points):
            if sp != op:
                return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def area(self):
        area, pts = 0.0, self.points
        for i in range(len(pts) - 1):
            area += pts[i].x * pts[i + 1].y - pts[i + 1].x * pts[i].y
        return abs(area) / 2.0

    def is_convex(self):
        pass

    def is_concave(self):
        return not self.is_convex()


p = Point2D(1, 1)
q = Point2D(2, 2)
r = Point2D(1, 2)
l = (p, q, r)
pol1 = Polygon([])
print(pol1.area())
