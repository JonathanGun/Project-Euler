from math import inf, sqrt


def or_(a, b):
    return a or b


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def out(self):
        print("(" + str(self.x) + ", " + str(self.y) + ")", end="")


class Vector2D:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        if (self.p2.x - self.p1.x == 0):
            self.m = inf
        else:
            self.m = (self.p2.y - self.p1.y) / (self.p2.x - self.p1.x)

    def mag(self):
        return sqrt(self.p1.x * self.p2.x + self.p1.y * self.p2.y)

    def out(self):
        self.p1.out()
        print("", end="")
        self.p2.out()
        print()

    def intersectY(self):
        x1 = self.p1.x
        x2 = self.p2.x
        y1 = self.p1.y
        y2 = self.p2.y
        if (self.m != inf):
            intersectAt = self.m * (-x1) + y1
            if min(y1, y2) <= intersectAt <= max(y1, y2):
                if intersectAt > 0:
                    return [0, 1, 0, 0]
                elif intersectAt == 0:
                    return [0, 1, 0, 1]
                else:
                    return [0, 0, 0, 1]
            else:
                return [0, 0, 0, 0]
        else:
            if y1 == 0:
                return [0, 1, 0, 1]
            else:
                return [0, 0, 0, 0]

    def intersectX(self):
        x1 = self.p1.x
        x2 = self.p2.x
        y1 = self.p1.y
        y2 = self.p2.y
        if (self.m != 0):
            intersectAt = 1 / self.m * (-y1) + x1
            if min(x1, x2) <= intersectAt <= max(x1, x2):
                if intersectAt > 0:
                    return [1, 0, 0, 0]
                elif intersectAt == 0:
                    return [1, 0, 1, 0]
                else:
                    return [0, 0, 1, 0]
            else:
                return [0, 0, 0, 0]
        else:
            if x1 == 0:
                return [1, 0, 1, 0]
            else:
                return [0, 0, 0, 0]


class Triangle:
    def __init__(self, points):
        self.p1 = Point(points[0], points[1])
        self.p2 = Point(points[2], points[3])
        self.p3 = Point(points[4], points[5])
        self.line1 = Vector2D(self.p1, self.p2)
        self.line2 = Vector2D(self.p2, self.p3)
        self.line3 = Vector2D(self.p3, self.p1)

    def intersectAll(self):
        cnt = [0, 0, 0, 0]
        cnt = list(map(or_, cnt, self.line1.intersectX()))
        cnt = list(map(or_, cnt, self.line1.intersectY()))
        cnt = list(map(or_, cnt, self.line2.intersectX()))
        cnt = list(map(or_, cnt, self.line2.intersectY()))
        cnt = list(map(or_, cnt, self.line3.intersectX()))
        cnt = list(map(or_, cnt, self.line3.intersectY()))
        return sum(cnt) == 4


triangles = []
f = open('p102_triangles.txt', 'r')
for line in f.readlines():
    line = line if line[-1] != '\n' else line[:-1]
    triangles.append(Triangle(list(map(int, line.split(',')))))

f.close()

cnt = 0
for t in triangles:
    if t.intersectAll():
        cnt += 1
print(cnt)
