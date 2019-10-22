from decimal import Decimal, getcontext

n = 100
getcontext().prec = n + 5
ans = 0
for i in range(1, n + 1):
    if int(Decimal(i).sqrt())**2 != i:
        x = str(Decimal(i).sqrt())
        x = x[:1] + x[2:n + 1]
        ans += sum(map(int, x))
print(ans)
