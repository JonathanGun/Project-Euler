from Prime import is_prime


def factor(n, cache):
    nn = n
    if cache[n] != -1:
        return cache[n]
    for i in primes:
        while n % i == 0 and n != i:
            n = n // i
        if is_prime(n):
            break
    cache[nn] = n
    return n


n = 1000000
x = int(n**0.5) + 1
primes = [2]
for i in range(3, x, 2):
    if is_prime(i):
        primes.append(i)
print(primes[:10])

cache = [-1 for x in range(n + 1)]
cache[1] = 1
cache[2] = 2
sm = 0
for i in range(2, n + 1):
    sm += factor(i, cache)
print(sm)
