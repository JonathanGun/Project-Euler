def tri(n, cache={}):
    return n * (n + 1) / 2


trilist = []
x = 0
n = 1
while x <= 192:
    x = tri(n)
    n += 1
    trilist.append(x)

with open("p042_words.txt") as f:
    for item in f:
        items = item[1:-1].split('","')

ans = 0
for item in items:
    score = 0
    for i in range(len(item)):
        score += ord(item[i]) - 64
    if score in trilist:
        ans += 1
print(ans)
