# f = n*n + a*n + b
# a > -1000 and a < 1000
# b >= -1000 and b<= 1000
# for n in range(x), f(n) = prime
# find largest x

from Prime import is_prime

limit = 1000
high = 0

for a in range(-limit + 1, limit):
    for b in range(-limit, limit + 1):
        n = 0
        f = n * n + a * n + b
        while is_prime(f):
            n += 1
            f = n * n + a * n + b
        if n > high:
            high = n
            ans = a * b

print(ans)
