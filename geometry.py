# %%
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, next):
        dx = self.x - next.x
        dy = self.y - next.y
        return math.sqrt(dx**2 + dy**2)

    def __str__(self):
        return f"Point({self.x}, {self.y})"


class Line:
    def __init__(self, start_point, end_point):
        self.start = start_point
        self.end = end_point

    def length(self):
        return self.start.distance_to(self.end)

    def __str__(self):
        return f"Line({self.start}, {self.end})"



p1 = Point(0, 0)
p2 = Point(3, 4)

line1 = Line(p1, p2)

print(p1)
print(p2)
print(line1)
print("Line length:", line1.length())


