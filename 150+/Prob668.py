from math import sqrt, ceil


def prime_generator(n):
    D = {}
    q = 2
    while q <= n:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def factors(x):
    for i in primes:
        if x % i == 0:
            yield i
            while(x % i == 0):
                x //= i


if __name__ == "__main__":
    n = 100
    primes = prime_generator(n)
    # print(primes)
    print(len(primes))

    cur = 1
    for p in primes:

        while cur < n:

            # cnt = 0
            # for i in range(1, n + 1):
            #     mx = ceil(sqrt(i))
            #     if i in primes:
            #         continue
            #     get = True
            #     # print(i, ":", end="")
            #     for x in factors(i):
            #         if x >= mx:
            #             get = False
            #             break
            #         # print(x, end=" ")
            #         if i // x in primes:
            #             if i // x >= mx:
            #                 get = False
            #                 break
            #             # print(i // x, end=" ")
            #     if get:
            #         print(i)
            #         cnt += 1
            #         # print("!", i, end=" ")
            #     # print()

            # print(cnt)
