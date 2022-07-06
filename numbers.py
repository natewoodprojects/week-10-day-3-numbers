class Vector:
    def __init__(self, vals):
        self.vals = vals

    def __repr__(self):
        return f'{self.__class__.__name__}({repr(self.vals)})'

    def __add__(self, other):
        return Vector([v + other for v in self.vals])

    def __mul__(self, other):
        return Vector([v * other for v in self.vals])
    
    def __sub__(self, other):
        return Vector([v - other for v in self.vals])

    def __truediv__(self, other):
        return Vector([v / other for v in self.vals])

v = Vector([1,2,3])

v /= 10


print(v)