ans = '73162890'
f = open('p079_keylog.txt', 'r')
for line in f.readlines():
    line = line[:-1] if line[-1] == '\n' else line
    i = 0
    for l in line:
        while i < len(ans):
            if l == ans[i]:
                break
            i += 1
        if i == len(ans):
            print(line)
f.close()
print(ans)
