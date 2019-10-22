def factor_generator(n=600851475143):
    i = 2
    while (i <= n):
        while (n % i == 0):
            yield i
            n /= i
        i += 1


for x in factor_generator():
    print(x)
