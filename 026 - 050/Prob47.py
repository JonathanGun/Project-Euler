from Prime import is_prime


def factorize(num):
    ans = set()
    for i in primes:
        tmp = 1
        while num % i == 0:
            tmp *= i
            num = num // i
        if tmp > 1:
            ans.add(tmp)
        if num < i:
            break
    return ans


def equallen(ls, n):
    for i in range(len(ls)):
        if len(ls[i]) != n:
            return False
    return True


def isecall(ls):
    if len(ls) == 1:
        return set()
    return ls[0].intersection(isecall(ls[1:]))


n = 4

primes = []
for i in range(10**(n + 1)):
    if is_prime(i):
        primes.append(i)
print(primes[-10:])

facs = []
for i in range(1, n + 1):
    facs.append(factorize(i))

cur = n
while True:
    # print(cur, facs)
    if len(isecall(facs)) == 0 and equallen(facs, n):
        print(cur - n)
        break
    facs[cur % n] = factorize(cur)
    cur += 1
