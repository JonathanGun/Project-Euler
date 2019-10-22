total = 0
for pow in range(1, 31):
    base = 0
    ans = 0
    while len(str(ans)) <= pow:
        base += 1
        ans = base**pow
        if len(str(ans)) == pow:
            total += 1

print(total)
