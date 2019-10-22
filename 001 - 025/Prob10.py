primes = [2, 3, 5, 7]
sum = 2 + 3 + 5 + 7
for x in range(2000000):
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
        sum += primes[-1]
print(sum)
