from math import sqrt
import time

t1 = time.time()
num = 1000
for a in range(1, num):
    for b in range(1, num):
        if a > b:
            continue
        c = sqrt(a**2 + b**2)
        if a + b + c == num:
            print(a * b * int(c))
            print(time.time() - t1)
            quit()
