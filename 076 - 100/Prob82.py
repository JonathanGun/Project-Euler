def pisang(i, j):
    print(i, j)
    if dp[i][j] != 0:
        return dp[i][j]

    if j == 0 and i == 0:
        return dp[i][j]

    ans = grid[i][j]
    if j > 0:
        ans = pisang(i, j - 1) + grid[i][j - 1]
    if i < n - 1:
        ans = min(ans, pisang(i + 1, j) + grid[i + 1][j])
    # if i > 0:
    #     ans = min(ans, pisang(i - 1, j) + grid[i - 1][j])
    dp[i][j] = ans + grid[i][j]
    return ans


n = 5
MAX = 10**8
dp = [[0 for x in range(n)] for y in range(n)]
grid = []

f = open('p082_matrix_sample.txt', 'r')
for line in f.readlines():
    line = line[:-1] if line[-1] == '\n' else line
    grid.append(list(map(int, line.split(","))))
f.close()

# for g in grid:
#     print(g)

print(pisang(0, n - 1))
print(sum(grid[2]))
for d in dp:
    print(d)
