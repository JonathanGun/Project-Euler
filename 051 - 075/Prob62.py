n = 5

i = 1
data = {}
found = False
while not found:
    tmp = ''.join(sorted(str(i**3)))
    try:
        data[tmp].append(i)
        if len(data[tmp]) == n:
            found = True
            print(data[tmp][0]**3, data[tmp])
    except KeyError:
        data[tmp] = [i]
    i += 1
