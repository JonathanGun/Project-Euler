# https://oeis.org/A055401

max_iter = 100000
ans = 0
N = 10**2
cnt = 0

cubes = []
i = 1
while True:
    x = i**3
    if x > N:
        break
    cubes.append(x)
    i += 1
print(cubes)

adds = []
last = len(cubes) - 1
for n in range(1, N):
    i = last
    # print(n, end=" ")
    cur = 0
    while n != 0 and cnt < max_iter:
        cur += n // cubes[i]
        n %= cubes[i]
        i -= 1
        cnt += 1
    if cubes[i] == n:
        last = i - 1
    ans += cur
    adds.append(cur)
    print(cur, end=", ")
    # print(ans, end=", ")
print(ans)

for n in cubes[1:]:
    print(n)
    for i in range(len(adds)):
        print(adds[i], end=" ")
        if (i + 1) % (n - 1) == 0:
            print()
    print()
