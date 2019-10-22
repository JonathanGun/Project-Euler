def RomanEff(num):
    if num == 0:
        return 0

    if num % 10 in [1, 5]:
        return 1 + RomanEff(num // 10)
    if num % 10 in [2, 4, 6, 9]:
        return 2 + RomanEff(num // 10)
    if num % 10 in [3, 7]:
        return 3 + RomanEff(num // 10)
    if num % 10 in [8]:
        return 4 + RomanEff(num // 10)
    if num % 10 in [0]:
        return RomanEff(num // 10)


def RomanToInt(str):
    ans = 0
    i = 0
    while i < len(str):
        cur = str[i]
        nxt = '' if (i == len(str) - 1) else str[i + 1]

        if cur == 'I':
            if nxt == 'X':
                ans += 9
                i += 1
            elif nxt == 'V':
                ans += 4
                i += 1
            else:
                ans += 1
        elif cur == 'V':
            ans += 5

        elif cur == 'X':
            if nxt == 'C':
                ans += 90
                i += 1
            elif nxt == 'L':
                ans += 40
                i += 1
            else:
                ans += 10
        elif cur == 'L':
            ans += 50

        elif cur == 'C':
            if nxt == 'M':
                ans += 900
                i += 1
            elif nxt == 'D':
                ans += 400
                i += 1
            else:
                ans += 100
        elif cur == 'D':
            ans += 500

        elif cur == 'M':
            ans += 1000

        i += 1

    return ans


ans = 0
f = open('p089_roman.txt', 'r')
for line in f.readlines():
    line = line[:-1]
    num = RomanToInt(line)
    best = RomanEff(num % 1000) + num // 1000
    if len(line) - best > 0:
        print(line, num, len(line), best)
    ans += len(line) - best
f.close()
print(ans)
