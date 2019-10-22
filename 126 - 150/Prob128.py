# Prob128, idea:
# divide nums into layers
# each layer has 6*(n-1) members
# e.g. 2nd layer: 6*1 = 6, 3rd = 6*3 = 18
# except 1st layer has 1 member
#
# every number has: (hexagon side)
#   2 neighbor from n-1 layer
#   2 neighbor from n layer
#   2 neighbor from n+1 layer
# except number 1, 2-8 (1 jump), 8-20 (every 2), 20 - 38 (3 jump), etc has: (hexagon corner)
#   1 neighbor from n-1 layer
#   3 neighbor from n layer
#   2 neighbor from n+1 layer
#
# substract those numbers from origin tile,
# count how many primes
# if count == 3 add to result list
# list[9] should be 271
# when found 2000 nums, stop, peint last num
#
# how to improve:
# sides is max 2 PD
# corners is max 2 PD too
# only check start and end of ring, bcs left and right diff != 1


from Prime import is_prime
from factorial import sumfac
import time


def check(num):
    global count
    if is_prime(abs(n - num)):
        count += 1


t1 = time.time()
num = [[1], []]

layer = 1
limit = 10000
for n in range(2, limit + 1):
    x = sumfac(layer) * 6 + 1
    if n <= x:
        if n == sumfac(layer - 1) * 6 + 2 or n == sumfac(layer - 1) * 6 + 3 or n == sumfac(layer) * 6 or n == sumfac(layer) * 6 + 1:
            num[layer].append(n)
    else:
        layer += 1
        num.append([])
        num[layer].append(n)

# print(num)
print("done indexing {} layers in".format(layer), time.time() - t1)

lastlayer = layer
layer = 0
result = [1]
for lyr in num:
    if layer % 100 == 0:
        print("layer", layer)
    if layer >= lastlayer - 1:
        break

    for n in lyr:
        count = 0
        if n == lyr[-1]:
            # 2 n (1 is 1 diff)
            check(lyr[0])
            # 2 n-1
            check(num[layer - 1][0])
            check(num[layer - 1][-1])
            # 2 n+1 (only odd diff)
            check(num[layer + 1][-2])
        elif n == lyr[0]:
            check(lyr[-1])
            check(num[layer - 1][0])
            check(num[layer + 1][1])
            check(num[layer + 1][-1])

        if count == 3:
            result.append(n)

    layer += 1

print()
print("found", len(result))
print(result)
print()
print("in", time.time() - t1, "seconds")
