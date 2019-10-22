from math import floor, sqrt

amic_candidate = []
amic_numbers = []

for i in range(2, 10000):        # start from 2, because we know 1 is divisible by only 1, that's against the rule
    divisible = [1]             # every number always divisible by 1, and to remove n from divisible list
    for n in range(2, floor(sqrt(i)) + 1):
        if i % n == 0:
            divisible.append(n)
            if n != int(i / n):
                divisible.append(int(i / n))
    amicsum = sum(divisible)
    amic_candidate.append((i, amicsum))
    if i != amicsum:
        if (amicsum, i) in amic_candidate:
            amic_numbers.append((i, amicsum))

print(sum(sum(x) for x in amic_numbers))
