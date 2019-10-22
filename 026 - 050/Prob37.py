from Prime import is_prime

result = []
num = 13
while len(result) < 11:
    truncprime = True
    if num % 10 == 1:
        num += 2
    for i in range(len(str(num))):
        num1, num2 = num, num
        if i > 0:
            num1 = int(str(num)[:-i])
            num2 = int(str(num)[i:])
        if (not is_prime(num1)) or (not is_prime(num2)):
            truncprime = False
            break
    if truncprime:
        result.append(num)
    num += 4

print(sum(result))
