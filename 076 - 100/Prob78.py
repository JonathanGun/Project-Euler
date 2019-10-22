n = 60000
x = 6
target = 10**x
coins = range(1, n + 1)
dp = [0 for x in range(n + 1)]
dp[0] = 1

for c in coins:
    for i in range(c, n + 1):
        dp[i] += dp[i - c]
        dp[i] %= target
    if c % 500 == 0:
        print(c)
    if dp[c] % target == 0:
        print(c, dp[c])
        break
