from Prime import is_prime


def mult(ls):
    ans = 1
    for item in ls:
        ans *= item
    return ans


limit = 20
primes = list(n for n in range(limit) if is_prime(n))
jump = mult(primes)

num = 0
found = False
while not found:
    found = True
    num += jump
    for i in range(2, limit + 1):
        if int(num / i) != num / i:
            found = False
            break
print("Done! Answer:", num)
