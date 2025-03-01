m = 4503599627370517
r = 1504170715041707

ans, cur, last_coin = 0, 0, 4503599627370517
# ans, cur, last_coin = 1517926279158891, 115880182942287, 14169772

N = 50_000_000
for i in range(N):
    cur += r
    cur %= m
    if cur < last_coin:
        last_coin = cur
        ans += cur
        print("found!", ans, cur)
print(ans, cur, last_coin)

inv = pow(1504170715041707, -1, 4503599627370517)
cur_max = m
for i in range(1, last_coin):
    test = (inv * i) % m
    if test < cur_max:
        cur_max = test
        ans += i
        print("found!", ans, test)
print(ans)
