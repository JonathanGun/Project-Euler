ans = 0
nums = []
for a in range(1, 4):
    for b in range(1, a + 1):
        for c in range(1, b + 1):
            for d in range(1, c + 1):
                for e in range(1, d + 1):
                    for f in range(1, e + 1):
                        n = 2**a * 3**b * 5**c * 7**d * 11**e * 13**f
                        if n > 1000 and n < 1000000:
                            nums.append(n)
nums.sort()

i = 0
while ans <= 1000:
    ans = 0
    n = nums[i]
    for x in range(2 * n, n, -1):
        if (x * n) % (x - n) == 0:
            ans += 1
    i += 1
print(n, ans)
