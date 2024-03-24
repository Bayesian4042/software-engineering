class AreaCalculator:
    """ This class violates the Open/Closed Principle because we need to modify the area method every time we add a new shape."""
    
    def area(self, shape):
        if isinstance(shape, Rectangle):
            return shape.width * shape.height
        
        elif isinstance(shape, Circle):
            return 3.14 * shape.radius ** 2
        
        elif isinstance(shape, Square):
            return shape.side ** 2
        
        else:
            raise TypeError("Shape not supported")
        
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
class Circle:
    def __init__(self, radius):
        self.radius = radius


class Square:
    def __init__(self, side):
        self.side = side