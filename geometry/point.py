from abc import (ABC,
                 abstractmethod,
                 abstractproperty)
from utils.exceptions import (InvalidGeometry,
                              InvalidOperation)


class Point(ABC):
    '''Point Class Base Implementation'''

    def __init__(self, *coords, dim):
        if len(coords) not in [0, dim]:
            raise InvalidGeometry(
                "Insert ({}) coordinates or none".format(dim))
        for coord in coords:
            if not isinstance(coord, int) and \
               not isinstance(coord, float) and \
               not coord == None:
                raise InvalidGeometry("Insert only numeric values or none")
        self.dim = dim

    def __str__(self):
        values = [str(v) for v in self.coords]
        geom = ", ".join(values)
        return "POINT({})".format(geom)

    def is_null(self):
        for coord in self.coords:
            if coord == None:
                return True
        return False

    def __eq__(self, other):
        for sc, oc in zip(self.coords, other.coords):
            if sc != oc:
                return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def check_operation(self, other):
        if self.is_null() or other.is_null():
            raise InvalidOperation("Either of the points is null")
        if self.dim != other.dim:
            raise InvalidOperation("The point dimensions are not equal")

    '''Overrides'''

    @abstractproperty
    def coords(self):
        pass

    @abstractmethod
    def __add__(self, other):
        self.check_operation(other)
        return [sc + oc for sc, oc in zip(self.coords, other.coords)]

    @abstractmethod
    def __sub__(self, other):
        self.check_operation(other)
        return [sc - oc for sc, oc in zip(self.coords, other.coords)]

    @abstractmethod
    def translate(self, *translation):
        '''Translate point'''
        if len(translation) != self.dim:
            raise InvalidOperation("Invalid translation")
        return [sc + tc for sc, tc in zip(self.coords, translation)]


class Point2D(Point):
    '''2D Point Implemenation'''

    def __init__(self, *coords):
        '''
        Initialize 2D point
        i.e. p = Point2D(1, 2)
        Access point coordinates by p.x, p.y
        '''
        super().__init__(*coords, dim=2)
        x, y = None, None
        if len(coords) == self.dim:
            x, y = coords
        self.x = x
        self.y = y

    @property
    def coords(self):
        return self.x, self.y

    def __add__(self, other):
        return Point2D(*super().__add__(other))

    def __sub__(self, other):
        return Point2D(*super().__sub__(other))

    def translate(self, *translation):
        return Point2D(*super().translate(*translation))

    def to3D(self):
        '''Convert to 3D point'''
        return Point3D(self.x, self.y, 0)


class Point3D(Point):
    '''3D Point Implementation'''

    def __init__(self, *coords):
        '''
        Initialize 2D point
        i.e. p = Point3D(1, 2, 3)
        Access point coordinates by p.x, p.y, p.z
        '''
        super().__init__(*coords, dim=3)
        x, y, z = None, None, None
        if len(coords) == self.dim:
            x, y, z = coords
        self.x = x
        self.y = y
        self.z = z

    @property
    def coords(self):
        return self.x, self.y, self.z

    def __add__(self, other):
        return Point3D(*super().__add__(other))

    def __sub__(self, other):
        return Point3D(*super().__sub__(other))

    def translate(self, *translation):
        return Point3D(*super().translate(*translation))

    def to2D(self):
        '''Convert to 2D point'''
        return Point2D(self.x, self.y)
