b = 0
for i in range(1000):
    if i % 3 == 0:
        a = i
    elif i % 5 == 0:
        a = i
    else:
        a = 0
    b += a
print(b)
