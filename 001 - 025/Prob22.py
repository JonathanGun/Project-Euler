f = open('p022_names.txt', 'r')
names = sorted(f.readline()[1:-1].split('","'))
f.close()

ans = 0
for i in range(len(names)):
    name = names[i]
    ans += sum(((ord(x) - ord('A') + 1) * (i + 1) for x in name))
print(ans)
