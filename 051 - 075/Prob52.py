limit = 6
counter = 1
while True:
    num = []
    found = True
    if counter > 10**(len(str(counter))) / limit:
        counter = 10**(len(str(counter)))

    for i in range(1, limit + 1):
        next = counter * i
        if len(str(next)) != len(str(counter)):
            break
        else:
            num.append(next)

    if len(num) == limit:
        pnum = []
        for n in num:
            dig = []
            for digit in range(len(str(n))):
                dig.append(int((str(n))[digit]))
            n = set(dig)
            pnum.append(n)

        for i in range(limit - 1):
            if pnum[i] != pnum[i + 1] or len(pnum[i]) != len(str(counter)):
                found = False
                break
        if found:
            print(counter)
            exit()

    counter += 1
