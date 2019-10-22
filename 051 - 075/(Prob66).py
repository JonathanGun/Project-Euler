# x*x - d*y*y = 1
# y = sqrt(x*x - 1/d)
# x = sqrt(1+d*y*y)

from math import sqrt
from Prime import is_prime

limit = 100
max = 0
ans = []

for d in range(1, limit + 1, 2):
    y = 1
    if int(sqrt(d)) == sqrt(d) or not is_prime(d):
        continue
    found = False
    while not found:
        # y = sqrt((x*x - 1)/d)
        x = sqrt(1 + d * y * y)

        if int(x) == x:
            found = True
            if x > max:
                max = x

        y += 1
    print(d, x)

print(max)
