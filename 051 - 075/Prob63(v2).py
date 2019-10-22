ans = 0
for pow in range(1, 25):
    base = 1
    while base**pow < 10**pow:
        if len(str(base**pow)) == pow:
            ans += 1
        base += 1
print(ans)
