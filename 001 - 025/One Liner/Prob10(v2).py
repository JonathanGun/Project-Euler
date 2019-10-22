from Prime import is_prime
print(sum(i for i in range(3, 2000000, 2) if is_prime(i)) + 2)
