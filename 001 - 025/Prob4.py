largest = 0
for b in range(1000, 900, -1):
    for a in range(1000, 900, -1):
        c = a * b
        if len(str(c)) % 2 == 0:
            firsthalf = str(c)[:int((len(str(c)) // 2))]
            secondhalf = str(c)[-int((len(str(c)) // 2)):]
            if firsthalf == secondhalf[::-1] and c > largest:
                largest = c
print(largest)
