primes = [2, 3, 5, 7]
for x in range(1000000):
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
    if len(primes) > 10000:
        break
