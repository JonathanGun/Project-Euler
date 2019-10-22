sum = 0
for i in range(2, 500000):
    res = 0
    i = str(i)
    for num in i:
        res += int(num) ** 5
    if int(i) == res:
        sum += res
print(sum)
