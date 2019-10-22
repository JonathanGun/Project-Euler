a = 0
for i in range(1, 101):
    i = i ** 2
    a += i

b = 0
for i in range(1, 101):
    b += i
b *= b

print(b - a)
