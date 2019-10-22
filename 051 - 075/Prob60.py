from Prime import is_prime
import time


def find_all_pairs(a):
    for p in primes:
        if p <= a:
            continue
        if p > a and is_prime(int(str(a) + str(p))) and is_prime(int(str(p) + str(a))):
            yield p


t1 = time.time()

upper = 10000
primes = set()
for i in range(upper):
    is_prime(i, primes)
primes = sorted(primes)

ans = upper * 5
pairs = {}
for i in range(len(primes)):
    pairs[primes[i]] = set()

for a in primes:
    if a * 5 >= ans:
        break
    if len(pairs[a]) == 0:
        pairs[a] = set(find_all_pairs(a))

    for b in primes:
        if a + b * 4 >= ans:
            break
        if b not in pairs[a]:
            continue
        if len(pairs[b]) == 0:
            pairs[b] = set(find_all_pairs(b))

        for c in primes:
            if a + b + c * 3 >= ans:
                break
            if c not in pairs[a] or c not in pairs[b]:
                continue
            if len(pairs[c]) == 0:
                pairs[c] = set(find_all_pairs(c))

            for d in primes:
                if a + b + c + d * 2 >= ans:
                    break
                if d not in pairs[a] or d not in pairs[b] or d not in pairs[c]:
                    continue
                if len(pairs[d]) == 0:
                    pairs[d] = set(find_all_pairs(d))

                for e in primes:
                    if e not in pairs[a] or e not in pairs[b] or e not in pairs[c] or e not in pairs[d]:
                        continue
                    if a + b + c + d + e < ans:
                        ans = a + b + c + d + e
                        print(a, b, c, d, e, a + b + c + d + e, time.time() - t1)
