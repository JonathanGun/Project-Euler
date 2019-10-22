from Prime import is_prime
import time


def is_circular(num):
    for _ in range(len(str(num)) - 1):
        num = int(str(num)[-1] + str(num)[:-1])
        if not is_prime(num):
            return False
    return True


t1 = time.time()
limit = 1000000
ans = 0
for num in range(limit):
    if is_prime(num) and is_circular(num):
        ans += 1
print(ans)
t2 = time.time()

print(t2 - t1, " seconds")
