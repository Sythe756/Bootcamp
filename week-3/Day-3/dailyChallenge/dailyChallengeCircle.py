import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
            self.diameter = 2 * radius
        elif diameter is not None:
            self.diameter = diameter
            self.radius = diameter / 2
        else:
            raise ValueError("Please specify either the radius or the diameter of the circle.")

    def area(self):
        return math.pi * (self.radius ** 2)

    def __str__(self):
        return f"Circle with radius: {self.radius}, diameter: {self.diameter}, and area: {self.area()}"

    def __add__(self, other_circle):
        new_radius = self.radius + other_circle.radius
        return Circle(radius=new_radius)

    def __lt__(self, other_circle):
        return self.radius < other_circle.radius

    def __eq__(self, other_circle):
        return self.radius == other_circle.radius

if __name__ == "__main__":
    circle1 = Circle(radius=5)
    circle2 = Circle(diameter=10)
    
    print(circle1)
    print(circle2)
    
    print("Area of circle1:", circle1.area())
    print("Area of circle2:", circle2.area())
    
    circle3 = circle1 + circle2
    print("Circle3 (circle1 + circle2):", circle3)

    circles = [Circle(radius=10), Circle(radius=5), Circle(radius=15)]
    circles.sort()

    for circle in circles:
        print(circle)

if circle3 > circle2:
    print(f"circle3 is bigger")
else:
    print("circle2 is bigger")

if circle1 == circle3:
    print("they are equal")
else:
    print("they are not equal")
