from math import floor, ceil
from decimal import Decimal as d

limit = 1000000
dict = {}
for x in range(1, ceil(3 * limit / 7)):
    for y in range(floor(x / 0.4285713), ceil((x / 0.4285715) + 1)):
        if y == 0:
            continue
        if d(x) / d(y) > 3 / 7:
            break
        if d(x) / d(y) >= 42857128 / 10000000:
            val = d(x) / d(y)
            dict[str(x) + '/' + str(y)] = str(val)
    if x % 1000 == 0:
        print(x)

ans = sorted(dict.items(), key=lambda x: x[1])
print(ans)
