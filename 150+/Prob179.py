from math import sqrt


def countDivisors(n):
    cnt = 0
    for i in range(1, (int)(sqrt(n)) + 1):
        if (n % i == 0):
            if (n / i == i):
                cnt = cnt + 1
            else:
                cnt = cnt + 2
    return cnt


n = 10**7
cnt = 0
last = 0
for i in range(1, n + 1):
    if i % 10**5 == 0:
        print(i)
    cur = countDivisors(i)
    if (cur == last):
        cnt += 1
        # print(i)
    last = cur
print(cnt)
