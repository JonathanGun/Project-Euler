from time import time
# total time needed 1 hours 10 mins


def rev(n):
    return str(n)[::-1]


def getFirstNum(n):
    while n // 10 != 0:
        n //= 10
    return n


n = 10**9

t1 = time()
cnt = 0
i = 10
while i < n + 1:
    i += 1
    if i % 10 != 0:
        get = True
        for x in str(i + int(rev(i))):
            if int(x) % 2 == 0:
                get = False
                break
        if get:
            cnt += 1
    if i % 10**6 == 0:
        print(i / n * 100, '% :', time() - t1)
print(cnt, time() - t1)
