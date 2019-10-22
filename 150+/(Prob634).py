n = int(input())
ans = 0
x = int((n // 8 + 1)**0.5) + 1
print(n**0.2)

sudah = {}
for i in range(2, x + 1):
    for j in range(2, x + 1):
        cur = i**2 * j**3
        if cur <= n:  # and cur not in sudah:
            try:
                sudah[cur] += 1
            except KeyError:
                sudah[cur] = 1
                ans += 1
        elif cur > n:
            break
print(ans)
