from itertools import permutations
from time import time
# total time needed 277 hours

def T(n):
    return str(int(n * (n + 1) / 2))


def S(n):
    return str(int(n * n))


def P(n):
    return str(int(n * (3 * n - 1) / 2))


def H(n):
    return str(int(n * (2 * n - 1)))


def Hp(n):
    return str(int(n * (5 * n - 3) / 2))


def O(n):
    return str(int(n * (3 * n - 2)))


def validList(ls):
    last = ls[-1]
    for cur in ls:
        if cur[:2] != last[-2:]:
            return False
        last = cur
    return True


t1 = time()
c = 1
valT = T(c)
valS = S(c)
valP = P(c)
valH = H(c)
valHp = Hp(c)
valO = O(c)

lsT, lsTF, lsTB = [], [], []
lsS, lsSF, lsSB = [], [], []
lsP, lsPF, lsPB = [], [], []
lsH, lsHF, lsHB = [], [], []
lsHp, lsHpF, lsHpB = [], [], []
lsO, lsOF, lsOB = [], [], []

while len(valT) <= 5 or len(valS) <= 5 or len(valP) <= 5 or len(valH) <= 5 or len(valHp) <= 5 or len(valO) <= 5:
    valT = T(c)
    valS = S(c)
    valP = P(c)
    valH = H(c)
    valHp = Hp(c)
    valO = O(c)

    # while len(valT) < 4:
    #     valT = '0' + valT
    # while len(valS) < 4:
    #     valS = '0' + valS
    # while len(valP) < 4:
    #     valP = '0' + valP
    # while len(valH) < 4:
    #     valH = '0' + valH
    # while len(valHp) < 4:
    #     valHp = '0' + valHp
    # while len(valO) < 4:
    #     valO = '0' + valO

    if len(valT) == 4:
        if valT[-2] != '0':
            lsT.append(valT)
    if len(valS) == 4:
        if valS[-2] != '0':
            lsS.append(valS)
    if len(valP) == 4:
        if valP[-2] != '0':
            lsP.append(valP)
    if len(valH) == 4:
        if valH[-2] != '0':
            lsH.append(valH)
    if len(valHp) == 4:
        if valHp[-2] != '0':
            lsHp.append(valHp)
    if len(valO) == 4:
        if valO[-2] != '0':
            lsO.append(valO)

    c += 1

t2 = time()
print("Done indexing in", t2 - t1)

print('allT: ')
print(lsT)
print()
print('allS: ')
print(lsS)
print()
print('allP: ')
print(lsP)
print()
print('allH: ')
print(lsH)
print()
print('allHp: ')
print(lsHp)
print()
print('allO: ')
print(lsO)
print()
total = len(lsT) * len(lsS) * len(lsP) * len(lsH) * len(lsHp) * len(lsO)
print(total)

cnt = 0
for t in lsT:
    for s in lsS:
        for p in lsP:
            for h in lsH:
                for hp in lsHp:
                    for o in lsO:
                        nums = [t, s, p, h, hp, o]
                        if len(nums) == len(set(nums)):
                            coba = permutations(nums)
                            for c in coba:
                                if validList(c):
                                    print("FOUND")
                                    print(coba)
                                    print(sum(map(int, coba)))
                                    quit()
                        cnt += 1
                        if (cnt % 10**4) == 0:
                            print(((cnt / total) * 100), '%', time() - t1)
