def penta(n):
    return n * (3 * n - 1) / 2


limit = 3000
lst = set()
for i in range(1, limit + 1):
    lst.add(penta(i))

i = 1
current = penta(i)
next = penta(i + 1)
while True:
    i += 1
    current, next = next, penta(i + 1)
    diff = next - current
    for test in lst:
        if next - test in lst and next + test in lst:
            print(next - test)
            quit()
