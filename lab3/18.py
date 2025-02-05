from math import sqrt
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates: {self.x} and {self.y}")

    def move(self, a, b):
        self.x += a
        self.y += b

    def dist(self, q, w):
        return sqrt((q - self.x) ** 2 + (w - self.y) ** 2)

x, y = int(input()), int(input())
ok = Point(x, y)
ok.show()

a, b = int(input()), int(input())
ok.move(a, b)
ok.show()

q, w = int(input()), int(input())
print(ok.dist(q, w))
