def digitSq(num):
    sum = 0
    num = str(num)
    for i in range(len(num)):
        sum += int(num[i])**2
    return sum


limit = 10000000
ans = 0
right = []
wrong = []
cap = 9 * 9 * len(str(limit))

for num in range(1, limit + 1):
    x = num
    if x % 10000 == 0:
        print(x)

    while x != 89 and x != 1:
        x = digitSq(x)
        if x < cap or x % 2 == 0:
            if x in right:
                x = 89
            elif x in wrong:
                x = 1

    if x == 89:
        ans += 1
        if num < cap or x % 2 == 0:
            x = num
            while x != 89:
                if x in right:
                    break
                right.append(x)
                x = digitSq(x)

    else:
        if num < cap or x % 2 == 0:
            x = num
            while x != 1:
                if x in wrong:
                    break
                wrong.append(x)
                x = digitSq(x)

print("ans", ans)
