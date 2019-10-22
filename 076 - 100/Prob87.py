from math import ceil
from Prime import is_prime

limit = 50000000
cand = set()

for x4 in range(2, ceil(limit**(1 / 4))):
    if not is_prime(x4):
        continue
    x4pow = x4**4
    for x3 in range(2, ceil((limit - x4pow)**(1 / 3))):
        if not is_prime(x3):
            continue
        x3pow = x3**3
        for x2 in range(2, ceil((limit - x4pow - x3pow)**(1 / 2))):
            if not is_prime(x2):
                continue
            x2pow = x2**2
            cand.add(x2pow + x3pow + x4pow)

print(len(cand))
