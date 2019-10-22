def is_pandigital(num):
    if '0' in num or len(num) != 9:
        return False
    else:
        cur = set()
        for i in range(9):
            cur.add(num[i])
        return len(cur) == 9


ans = 0
prods = []
for n1 in range(2, 100):  # 1-2 digit
    for n2 in range(10**(5 - len(str(n1))) - 1, 10**(4 - len(str(n1))), -1):  # 4-3 digit
        prod = n1 * n2
        str_num = str(n1) + str(n2) + str(prod)
        if is_pandigital(str_num) and prod not in prods:
            ans += prod
            prods.append(prod)

print(ans)
