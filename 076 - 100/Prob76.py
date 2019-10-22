n = 100
coins = range(1, n + 1)
dp = [0 for x in range(n + 1)]
dp[0] = 1

for c in coins:
    for i in range(c, n + 1):
        dp[i] += dp[i - c]
print(dp[n] - 1)
