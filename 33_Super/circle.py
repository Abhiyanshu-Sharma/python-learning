class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

# Method overriding
    def describe(self):
        print(f"It is a Circle with an area of {3.14 * self.radius * self.radius}")
        super().describe()

class Sqaure(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
            print(f"It is a Sqaure with an area of {self.width * self.width}")
            super().describe()
    

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
            print(f"It is a Triangle with an area of {self.width * self.height / 2}")
            super().describe()
    

circle = Circle(color="red", is_filled=True, radius=5)
sqaure = Sqaure(color="red", is_filled=False, width=6)
triangle = Triangle(color="blue", is_filled=True, width=7, height=8)

print(circle.color)
print(circle.is_filled)
print(circle.radius)


circle.describe()
sqaure.describe()
triangle.describe()
