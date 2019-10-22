from operator import mul
from itertools import combinations
from functools import reduce


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


def how_many_times_divides(n, div):
    """
    >>> list(how_many_times_divides(40, 2))
    [2, 2, 2]
    """
    while n > 1:
        if n % div != 0:
            break
        n //= div
        yield div


def factorize(n):
    """
    >>> list(factorize(480))
    [2, 2, 2, 2, 2, 3, 5]
    """
    for item in primes:
        if item > n:
            break
        yield from how_many_times_divides(n, item)


def calculate_divisors(n):
    prime_multiples_list = list(factorize(n))

    """
    construct unique combinations
    A, B, B, C --> A, B, C, AB, AC, BB, BC, ABC, ABB, BBC
    """
    unique_combinations = set()
    for i in range(1, len(prime_multiples_list)):
        unique_combinations.update(
            set(combinations(prime_multiples_list, i)))

    # multiply elements of each unique combination
    return sorted(reduce(mul, i)
                  for i in unique_combinations)


def B(n):
    ans = 1
    for k in range(1, n + 1):
        ans *= k**(2 * k - 1 - n)
    return int(ans)


if __name__ == "__main__":
    n = 1000000
    primes = list(prime_generator(n))
    sm = 1
    x = 10
    for i in range(2, x + 1):
        y = B(i)
        tmp = 1 + y + sum(calculate_divisors(y))
        sm += tmp
    print(sm)
