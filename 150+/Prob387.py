from Prime import is_prime


def sum_of_digits(num):
    return sum(map(int, str(num)))


def is_harshad(num):
    return num % sum_of_digits(num) == 0


def right_truncatable_harshad(num):
    while num != 0:
        if not is_harshad(num):
            return False
        num //= 10
    return True


def strong_harshad(num):
    if is_harshad(num):
        return is_prime(num // sum_of_digits(num))


def strong_right_truncatable_harshard(num):
    return is_prime(num) and strong_harshad(num // 10) and right_truncatable_harshad(num // 10)


n = 10**6
sm = 0
for i in range(10, n + 1):
    if (strong_right_truncatable_harshard(i)):
        sm += i
        # print(i)
print(sm)
