from math import sqrt, ceil


def is_prime(num, cache=set()):
    if num in cache:
        return True
    if num == 2:
        cache.add(2)
        return True
    if num % 2 == 0 or num < 2:
        return False
    else:
        top = ceil(sqrt(num))
        for i in range(3, top + 1, 2):
            if num % i == 0:
                return False
        cache.add(num)
        return True
