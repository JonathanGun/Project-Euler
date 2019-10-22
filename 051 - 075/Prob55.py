def is_palindrome(num):
    s = str(num)
    r = s[::-1]
    return s == r and len(s) != 1


limit = 10000
iters = 50
total = 0
for num in range(1, limit + 1):
    for i in range(iters):
        num1 = str(num)
        num2 = str(num)[::-1]
        res = int(num1) + int(num2)
        if is_palindrome(res):
            total += 1
            break
        num = res

print(limit - total)
