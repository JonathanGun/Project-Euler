n = 10**7
phi = [0 for x in range(n)]
phi[1] = 1

mn = 10
ans = 0

i = 2
while i < n:
    if phi[i] == 0:
        phi[i] = i - 1
        j = 2
        while j * i < n:
            if phi[j] != 0:
                q = j
                f = i - 1

                while q % i == 0:
                    f *= i
                    q //= i

                phi[i * j] = f * phi[q]
            j += 1
    i += 1

for i in range(2, n):
    if ((i / phi[i]) < mn) and (sorted(str(i)) == sorted(str(phi[i]))):
        mn = i / phi[i]
        ans = i

print(ans, phi[ans], ans / phi[ans])
