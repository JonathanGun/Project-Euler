from math import floor, sqrt

n = 0
maxn = 0
maxdiv = 0

for i in range(1, 100000):
    n += i
    totaldiv = 0
    for x in range(1, floor(sqrt(n)) + 1):
        if n % x == 0:
            totaldiv += 2
        if totaldiv > maxdiv:
            maxn = n
            maxdiv = totaldiv
    if maxdiv > 500:
        break
print(str(maxn) + ' is the first number with more than 500 divisors (' + str(maxdiv) + ').')
