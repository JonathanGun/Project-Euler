def fact(n):
    try:
        ans = fd[n]
    except KeyError:
        if n == 0:
            ans = 1
        else:
            ans = n * fact(n - 1)
        fd[n] = ans
    finally:
        return ans


limit = 100
ans = 0
fd = {}
for n in range(1, limit + 1):
    for r in range(1, n + 1):
        com = fact(n) / (fact(r) * fact(n - r))
        if com > 1000000:
            ans += 1

print(ans)
