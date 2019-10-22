n = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
dp = [0 for x in range(n + 1)]
dp[0] = 1

for c in coins:
    for i in range(c, n + 1):
        dp[i] += dp[i - c]
print(dp[n])
