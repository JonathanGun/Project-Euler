mx = 0
ans = 0
x = 1000
for d in range(2, x):
    n = 10
    rems = []
    for i in range(d):
        if n % d in rems:
            if i - rems.index(n % d) > mx:
                mx = i - rems.index(n % d)
                ans = d
            break
        else:
            rems.append(n % d)

        n = (n * 10) % d
print(ans)
