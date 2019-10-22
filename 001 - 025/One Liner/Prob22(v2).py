f = open('p022_names.txt', 'r')
names = sorted(f.readline()[1:-1].split('","'))
f.close()

print(sum(sum(((ord(c) - ord('A') + 1) * (i + 1)
               for c in names[i])) for i in range(len(names))))
