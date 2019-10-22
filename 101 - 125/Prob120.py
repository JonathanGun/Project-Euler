sum = 0
for a in range(3, 1001):
    n = 0
    rmax = -1
    while True:
        r = ((a - 1)**n + (a + 1)**n) % (a * a)
        if r == rmax:
            sum += rmax
            break
        elif r > rmax:
            rmax = r
        n += 1
    if a % 100 == 0:
        print(a, "/ 1000", a / 10, "% completed!")
print("Done! Answer:", sum)
