class Shape:
    def area(self):
        raise NotImplementedError("Subclasses should implement this method")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius**2)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


shapes = []
r = float(input("Enter the radius of the circle: "))
shapes.append(Circle(r))

w = float(input("Enter the width of the rectangle: "))
h = float(input("Enter the height of the rectangle: "))
shapes.append(Rectangle(w, h))

for shape in shapes:
    print(f"The area of the shape is: {shape.area()}")
