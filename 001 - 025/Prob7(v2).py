from Prime import is_prime

n = 1
num = 1
while n != 10001:
    num += 2
    if is_prime(num):
        n += 1
print(num)
