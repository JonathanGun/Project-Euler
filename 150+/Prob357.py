from Prime import is_prime
from math import sqrt, ceil

x = 8

cnt = 1 + 4
for i in range(2, 10**x, 2):
    if i % 100000 == 0:
        print(i)
    if is_prime(i + 1) and is_prime(i // 2 + 2):
        jago = True
        for j in range(2, ceil(sqrt(i))):
            if i % j == 0 and not is_prime(i // j + j):
                jago = False
                break
        if jago:
            # print(i)
            cnt += i
print(cnt)
