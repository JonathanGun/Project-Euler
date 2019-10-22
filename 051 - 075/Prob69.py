# largest = [0, 0]
# for n in range(2, 1000001, 2):
#     relative_prime = list(range(1, n))
#     for num in range(1, n + 1):
#         if n % num == 0 and num != 1:
#             for x in range(num, relative_prime[-1], num):
#                 try:
#                     relative_prime.remove(x)
#                 except ValueError:
#                     pass
#     if n / len(relative_prime) > largest[-1]:
#         largest = [n, n / len(relative_prime)]
#         print(largest)

# I found out that the solution must be multiples of first few prime numbers, so I made this instead:

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
result = 1
for i in range(len(primes)):
    result *= primes[i]
    if result > 1000000:
        result /= primes[i]
        print('last num: ' + str(primes[i]))
        break
print(int(result))
