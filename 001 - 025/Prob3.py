import math
num = 600851475143
lim = math.floor(math.sqrt(num))
print(lim)
f = []
primes = [2, 3, 5, 7]
for x in range(lim):
    tempPrime = False
    for i in primes:
        if x > primes[-1] and x % i != 0:
            tempPrime = True
        else:
            tempPrime = False
            break
    if tempPrime:
        primes.append(x)
        print(primes[-1])
for i in primes:
    while num % i == 0:
        f.append(i)
        num = num / i
        print(f)
