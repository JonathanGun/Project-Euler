from math import gcd

n = 12000
ans = 0
for j in range(1, n + 1):
    for i in range(j // 3, j // 2 + 1):
        if gcd(i, j) == 1 and 3 * i > j and 2 * i < j:
            ans += 1
print(ans)
