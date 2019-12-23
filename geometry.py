from abc import ABC, abstractmethod, abstractproperty
from exceptions import (InvalidGeometry,
                        InvalidOperation)


class Point(ABC):
    def __init__(self, *coords, dim):
        if len(coords) not in [0, dim]:
            raise InvalidGeometry("Insert ({}) coordinates or none".format(dim))
        for coord in coords:
            if not isinstance(coord, int) and \
               not isinstance(coord, float) and \
               not coord == None:
                raise InvalidGeometry("Insert only numeric values or none")
        self.dim = dim

    @abstractproperty
    def coords(self):
        pass

    def __str__(self):
        values = [str(v) for v in self.coords]
        geom = ", ".join(values)
        return "POINT({})".format(geom)

    def is_null(self):
        for coord in self.coords:
            if coord == None:
                return True
        return False

    def check_operation(self, other):
        if self.is_null() or other.is_null():
            raise InvalidOperation("Either of the points is null")
        if self.dim != other.dim:
            raise InvalidOperation("The point dimensions are not equal")

    def add(self, other):
        self.check_operation(other)
        return [sc + oc for sc, oc in zip(self.coords, other.coords)]

    @abstractmethod
    def __add__(self, other):
        pass

    def sub(self, other):
        self.check_operation(other)
        return [sc - oc for sc, oc in zip(self.coords, other.coords)]

    @abstractmethod
    def __sub__(self, other):
        pass

    def translate(self, *dv):
        pass


class Point2D(Point):
    def __init__(self, *coords):
        super().__init__(*coords, dim=2)
        x, y = None, None
        if len(coords) == 2:
            x, y = coords[0], coords[1]
        self.x = x
        self.y = y

    @property
    def coords(self):
        return self.x, self.y

    def __add__(self, other):
        return Point2D(*self.add(other))

    def __sub__(self, other):
        return Point2D(*self.sub(other))


class Point3D(Point):
    def __init__(self, *coords):
        super().__init__(*coords, dim=3)
        x, y, z = None, None, None
        if len(coords) == 3:
            x, y, z = coords[0], coords[1], coords[2]
        self.x = x
        self.y = y
        self.z = z

    @property
    def coords(self):
        return self.x, self.y, self.z

    def __add__(self, other):
        return Point3D(*self.add(other))

    def __sub__(self, other):
        return Point3D(*self.sub(other))
