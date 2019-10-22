from itertools import permutations
from Prime import is_prime


digit = 9
found = False
while not found:
    num = list(range(1, digit + 1))
    allnum = list(permutations(num))

    for i in range(1, len(allnum) + 1):
        x = allnum[-i]
        t = ''
        for n in range(len(x)):
            t += str(x[n])
        t = int(t)
        if is_prime(t):
            print(t)
            found = True
            break

    digit -= 1
