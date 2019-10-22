def is_pandigital(num):
    if len(num) != 9 or '0' in num:
        return False
    else:
        for i in range(len(num) - 1):
            for i_ in range(i + 1, len(num)):
                if num[i] == num[i_]:
                    return False
        return True


high = 0
highi = 0
highn = 0
limit = 10000
for i in range(limit):
    num = ''
    n = 0
    while len(num) < 9:
        n += 1
        num += str(i * n)
    if is_pandigital(num):
        if int(num) > int(high):
            high = num
            highi = i
            highn = n

print(high, " = ", highi, " x ", list(range(highn)))
