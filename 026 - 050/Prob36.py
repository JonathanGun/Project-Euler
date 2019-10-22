def dec_to_bin(num):
    maxpower = 0
    result = ''
    temp = num
    while temp >= 2:
        temp /= 2
        maxpower += 1
    for power in range(maxpower, -1, -1):
        num -= 2**power
        if num < 0:
            num += 2**power
            result += '0'
        else:
            result += '1'
    return int(result)


def is_palindrome(num):
    firsthalf = str(num)[:int((len(str(num)) // 2))]
    secondhalf = str(num)[-int((len(str(num)) // 2)):]
    return firsthalf == secondhalf[::-1] or len(str(num)) == 1


print(sum(num for num in range(1, 1000000, 2) if is_palindrome(num) and is_palindrome(dec_to_bin(num))))
