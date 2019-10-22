'''
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''


def sum_of_div_by_3_and_5(limit=1000):
    return sum(x for x in range(limit) if div_by_3_and_5(x))


def div_by_3_and_5(num):
    return num % 3 == 0 or num % 5 == 0


print(sum_of_div_by_3_and_5(1000))
