print(max([a * b for a in range(1000, 900, -1) for b in range(1000, 900, -1) if len(str(a * b)) % 2 == 0 and str(a * b)[-int((len(str(a * b)) / 2)):] == (str(a * b)[:int((len(str(a * b)) / 2))])[::-1]]))