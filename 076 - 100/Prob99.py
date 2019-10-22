from math import log
nums = {}
with open('Prob99.txt', 'r') as f:
    data = list(f.read().replace('\n', ',').split(','))

largest = [0, 0]
for i in range(0, len(data), 2):
    c = int(data[i + 1]) * log(int(data[i]))
    if c > largest[-1]:
        largest = [int(i / 2) + 1, c]
print(largest[0])
