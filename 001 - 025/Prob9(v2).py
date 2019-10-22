from math import sqrt, floor

num = 1000
top = floor(num / sqrt(2))
for a in range(1, top + 1):
    for b in range(a + 1, num - 2 * a):
        c = sqrt(a**2 + b**2)
        if a + b + c == num:
            print(a * b * int(c))
            quit()
