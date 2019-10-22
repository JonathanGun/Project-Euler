from Prime import is_prime
# n = 500
# cache = set()
# for i in range(1, n // 2 + 1):
#     is_prime(i, cache)
# print(cache)
# print(len(cache))

cnt = 0
for i in range(1, 10**8):
    cnt += i
print(cnt)
