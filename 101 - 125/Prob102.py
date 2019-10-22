from math import atan, inf, degrees, sqrt, acos, pi


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Vector2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mag(self):
        return sqrt(dot(self, self))

    def dir(self):
        return Vector2D(self.x / self.mag(), self.y / self.mag())

    def toAngle(self):
        if self.x != 0:
            return atan(self.y / self.x)
        else:
            return atan(inf * self.y)


class Triangle:

    def __init__(self, points):
        self.p1 = Point(points[0], points[1])
        self.p2 = Point(points[2], points[3])
        self.p3 = Point(points[4], points[5])

        self.s1 = Vector2D(self.p2.x - self.p1.x, self.p2.y - self.p1.y)
        self.s2 = Vector2D(self.p3.x - self.p2.x, self.p3.y - self.p2.y)
        self.s3 = Vector2D(self.p1.x - self.p3.x, self.p1.y - self.p3.y)


def to_origin(p):
    return Vector2D(p.x, p.y)


def dot(v1, v2):
    return v1.x * v2.x + v1.y * v2.y


def angle(v1, v2):
    if v1.x != 0 and v1.y != 0 and v2.x != 0 and v2.y != 0:
        return acos(dot(v1, v2) / (v1.mag() * v2.mag()))
    else:
        return 0


def contains_origin(t):
    ang1 = angle(t.s1, to_origin(t.p1))
    ang2 = angle(to_origin(t.p2), t.s2)
    ang3 = angle(t.s2, t.s3)
    ang4 = angle(t.s3, t.s1)
    # ang1 = min(ang1, pi - ang1)
    # ang2 = min(ang2, pi - ang2)
    # ang3 = min(ang3, pi - ang3)
    # ang4 = min(ang4, pi - ang4)
    print(degrees(ang1), degrees(ang2), degrees(ang3),
          degrees(ang4), degrees(ang1 + ang2 + ang3 + ang4))
    return ang1 + ang2 + ang3 + ang4 == 2 * pi


triangles = []
f = open('p102_trianglessample.txt', 'r')
for line in f.readlines():
    line = line if line[-1] != '\n' else line[:-1]
    triangles.append(Triangle(list(map(int, line.split(',')))))
f.close()

for t in triangles:
    print(t.s1.dir().x, t.s1.dir().y)
    print(degrees(t.s1.dir().toAngle()))
    print()
    print(t.s2.dir().x, t.s2.dir().y)
    print(degrees(t.s2.dir().toAngle()))
    print()
    print(t.s3.dir().x, t.s3.dir().y)
    print(degrees(t.s3.dir().toAngle()))
    print()
    # print(degrees(angle(t.s1, t.s2)))
    # print(degrees(angle(t.s2, t.s3)))
    # print(degrees(angle(t.s3, t.s1)))
    print(contains_origin(t))
