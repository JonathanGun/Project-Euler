from Prime import is_prime
from math import sqrt


def is_composite(num):
    return num > 1 and not is_prime(num, cache)


def is_glc(num):
    for prime in cache:
        glc = sqrt((num - prime) / 2)
        if glc == int(glc):
            return True
    return False


cache = set()
for num in range(1, 10000, 2):
    if is_composite(num) and not is_glc(num):
        print(num)
        break
