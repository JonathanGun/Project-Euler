from Prime import is_prime

r = 0
a = 1
n = 1
limit = 10
while r <= 10**limit:
    found = False
    while not found or n % 2 == 0:
        a += 2
        if is_prime(a):
            n += 1
            if n > 21000:
                found = True
    r = ((a - 1)**n + (a + 1)**n) % (a * a)

print("Done! Answer:", n)
