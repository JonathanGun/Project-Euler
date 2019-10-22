n = 28433
pow = 7830457
digits = 10
for _ in range(pow):
    n = int(n)
    n *= 2
    n = str(n)
    if len(n) > digits:
        n = n[-digits:]
print(int(n) + 1)
