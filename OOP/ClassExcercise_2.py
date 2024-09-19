import math


class Shape:
    def __init__(self, position: int):
        self.position = position

    def move(self):
        self.position += 1

    def resize(self):
        pass

    def area(self):
        pass


class Display:
    def __init__(self, screen: int):
        self.screen = screen

    def plot2D(self):
        pass


class Rectangle(Shape, Display):
    def __init__(self, position: int, width: int, height: int, screen: int):
        Shape.__init__(self, position)
        Display.__init__(self, screen)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape, Display):
    def __init__(self, position: int, radius: float, screen: int):
        Shape.__init__(self, position)
        Display.__init__(self, screen)
        self.radius = radius

    def area(self):
        return self.radius * self.radius * math.pi


class Triangle(Shape, Display):
    def __init__(self, position: int, points: list, screen: int):
        Shape.__init__(self, position)
        Display.__init__(self, screen)
        self.points = points

    def area(self):
        return 0.5 * abs((self.points[0][0] * (self.points[1][1] - self.points[2][1]) + self.points[1][0] * (self.points[2][1] - self.points[0][1]) + self.points[2][0] * (self.points[0][1] - self.points[1][1])))





class Square(Rectangle):
    def __init__(self, position: int, width: int, screen: int):
        super().__init__(position, width, width, screen)