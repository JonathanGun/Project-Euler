from Prime import is_prime

target = 8
i = 0
while True:
    i += 1

    digits = 2 + len(str(i))
    cek = [' ' for x in range(digits)]
    for j in range(digits):
        for k in range(j + 1, digits):
            for o in range(k + 1, digits):
                l = 0
                m = 0
                while l < digits:
                    if l != j and l != k and l != o:
                        cek[l] = str(i)[m]
                        m += 1
                    l += 1

                cnt = 0
                for n in range(10):
                    cek[j] = str(n)
                    cek[k] = str(n)
                    cek[o] = str(n)
                    cekint = int(''.join(cek))
                    if len(str(cekint)) == digits:
                        if not is_prime(cekint):
                            cnt += 1
                    else:
                        cnt += 1

                    if cnt > (10 - target):
                        break

                if cnt == (10 - target):
                    for x in range(digits):
                        if x == j or x == k or x == o:
                            print('1', end='')
                        else:
                            print(cek[x], end='')
                    print()
                    exit()
