def move(x, y):
    if x == 1 and y == 1:
        return grid[0][0]
    if dp[x][y] != -1:
        return dp[x][y]

    l = True if x != 1 else False
    u = True if y != 1 else False
    dp[x][y] = grid[x - 1][y - 1]
    if l and u:
        dp[x][y] += min(move(x - 1, y), move(x, y - 1))
    elif l and not u:
        dp[x][y] += move(x - 1, y)
    elif u and not l:
        dp[x][y] += move(x, y - 1)
    return dp[x][y]


n = 5
dp = [[-1 for x in range(n + 1)] for y in range(n + 1)]
grid = [[131, 673, 234, 103, 18],
        [201, 96, 342, 965, 150],
        [630, 803, 746, 422, 111],
        [537, 699, 497, 121, 956],
        [805, 732, 524, 37, 331]]

grid = []
f = open('p081_matrix.txt', 'r')
for i in f.readlines():
    grid.append(list(map(int, i.split(','))))
f.close()
print(move(n, n))

for i in range(n):
    print(dp[i][:10])
