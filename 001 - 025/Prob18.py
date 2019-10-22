def makan(i, j):
	global cache
	if cache[i][j]:
		return cache[i][j]
	else:
		ans = grid[i][j]
		if i == 0:
			pass
		elif j == 0:
			ans += makan(i-1, j)
			cache[i][j] = ans
		elif j == i:
			ans += makan(i-1, j-1)
			cache[i][j] = ans
		else:
			ans += max(makan(i-1, j-1),makan(i-1, j))
			cache[i][j] = ans
		#print(i, j, ans)
		return ans

#$n = 4
#grid = [[0]*(n) for x in range(n)]
#grid = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]

grid = []
grid.append(list(map(int, "75".split())))
grid.append(list(map(int, "95 64".split())))
grid.append(list(map(int, "17 47 82".split())))
grid.append(list(map(int, "18 35 87 10".split())))
grid.append(list(map(int, "20 04 82 47 65".split())))
grid.append(list(map(int, "19 01 23 75 03 34".split())))
grid.append(list(map(int, "88 02 77 73 07 63 67".split())))
grid.append(list(map(int, "99 65 04 28 06 16 70 92".split())))
grid.append(list(map(int, "41 41 26 56 83 40 80 70 33".split())))
grid.append(list(map(int, "41 48 72 33 47 32 37 16 94 29".split())))
grid.append(list(map(int, "53 71 44 65 25 43 91 52 97 51 14".split())))
grid.append(list(map(int, "70 11 33 28 77 73 17 78 39 68 17 57".split())))
grid.append(list(map(int, "91 71 52 38 17 14 91 43 58 50 27 29 48".split())))
grid.append(list(map(int, "63 66 04 68 89 53 67 30 73 16 69 87 40 31".split())))
grid.append(list(map(int, "04 62 98 27 23 09 70 98 73 93 38 53 60 04 23".split())))

for i in range(len(grid)):
	print(grid[i])

n = len(grid)

cache = [[0]*(n) for x in range(n)]

ans = 0
for i in range(n):
	ans = max(ans, makan(n-1, i))
print(ans)