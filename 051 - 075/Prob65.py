e = [2]
counter = 0
while len(e) < 100:
    counter += 1
    e.append(1)
    e.append(2 * counter)
    e.append(1)

result = [1, 1]
for i in range(len(e) - 2, -1, -1):
    numer = e[i] * result[0] + result[1]
    denom = result[0]
    result = [numer, denom]

sum = 0
for digit in str(result[0]):
    sum += int(digit)
print(sum)
