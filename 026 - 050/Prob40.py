s = '.'
limit = 1000002
counter = 0

while len(s) < limit:
    counter += 1
    s += str(counter)

print(int(s[1]) * int(s[10]) * int(s[100]) * int(s[1000]) * int(s[10000]) * int(s[100000]) * int(s[1000000]))
