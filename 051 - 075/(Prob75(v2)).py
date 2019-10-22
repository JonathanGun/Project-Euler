from math import sqrt, ceil
import time


def single_pytha(limit):
    single = []
    double = []
    for num in range(12, limit + 1, 2):
        top = ceil(num / sqrt(2))
        is_double = False

        for x in double:
            if num % x == 0:
                is_double = True
                break

        for a in range(3, top):
            if is_double:
                print(num, "double")
                break
            c = num - 2 * a
            aa = a * a
            for b in range(a + 1, top):
                c -= 1
                if c * c == aa + b * b:
                    if num in single:
                        single.remove(num)
                        double.append(num)
                        is_double = True
                    else:
                        single.append(num)
                    break
    return len(single)


t1 = time.time()
print(single_pytha(400))
print(time.time() - t1)
