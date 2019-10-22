n = 10
target = 2 * 10**6

grid = [[0]]
ans = 0
r = 1
jawab = 0
while grid[r - 1][r - 1] < target:
    c = r
    while True:
        if r == c:
            if r == 1:
                grid = [[0, 0], [0, 1]]
            else:
                grid.append([0] * c)
                grid[r].append(grid[r - 1][c - 1] + r**3)
        else:
            if r == 1:
                grid[0].append(0)
            grid[r].append(grid[r - 1][c] + int((1 + c) * c * r / 2))
        if abs(grid[r][c] - target) < abs(ans - target):
            ans = grid[r][c]
            jawab = r * c

        if grid[r][c] > target:
            break
        c += 1
    c = 0
    if grid[r][c] > target:
        break
    r += 1
print(jawab)
