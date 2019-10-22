limit = 100
high = 0
sum = 0

for a in range(1, limit):
    for b in range(1, limit):
        sum = 0
        res = a ** b
        for n in range(0, len(str(res))):
            sum += int(str(res)[n])
        if sum > high:
            high = sum
print(high)
