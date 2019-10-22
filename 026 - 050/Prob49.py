from Prime import is_prime
from itertools import permutations


def permute(num):
    ls = set()
    num = str(num)
    for i in range(len(num)):
        ls.add(num[i])
    nums = list(permutations(num))

    ls = set()
    for n in nums[1:]:
        item = ''
        for x in n:
            item += x
        if item[0] != '0':
            ls.add(int(item))
    return ls


for num in range(1001, 9999, 2):
    if is_prime(num):
        ls = permute(num)
        for n in ls:
            diff = n - num
            if is_prime(n) and is_prime(n + diff) and (n + diff in ls) and diff > 0:
                print(str(num) + str(n) + str(n + diff))
