import math

radius = float(input("Enter the radius of a circle: "))

# area = pi * radius²
area = math.pi * pow(radius, 2)

print(f"The area of the circle is: {round(area, 2)}cm²")