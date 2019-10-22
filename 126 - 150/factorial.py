def fact(num, cache={0: 1, 1: 1}):
    if num in cache:
        return cache[num]
    else:
        return num * fact(num - 1)


def sumfac(num, cache={0: 0}):
    if num in cache:
        return cache[num]
    else:
        sum = 0
        for i in range(num + 1):
            sum += i
            cache[i] = sum
        return sum
