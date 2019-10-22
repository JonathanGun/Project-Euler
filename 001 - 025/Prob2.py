a, b, answer, limit = 0, 1, 0, 4000000
while b < limit:
    if b % 2 == 0:
        answer += b
    a, b = b, a + b
print(answer)
