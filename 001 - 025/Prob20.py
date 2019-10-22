def fact(num, cache=set()):
    if num > 1:
        return num * fact(num - 1)
    elif num == 1:
        return 1


num = fact(100)
ans = 0
for i in range(len(str(num))):
    ans += int(str(num)[i])
print(ans)
