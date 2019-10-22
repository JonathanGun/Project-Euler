from itertools import permutations
import time

t1 = time.time()
lst = list(range(10))
nums = list(permutations(lst))

print("Done listing", len(nums), "pandigital nums(", time.time() - t1, "s ).")

ans = 0
count = 0
for num in nums:
    count += 1
    d1 = str(num[0])
    d2 = str(num[1])
    d3 = str(num[2])
    d4 = str(num[3])
    d5 = str(num[4])
    d6 = str(num[5])
    d7 = str(num[6])
    d8 = str(num[7])
    d9 = str(num[8])
    d10 = str(num[9])
    if int(d1) != 0:
        if int(d2 + d3 + d4) % 2 == 0:
            if int(d3 + d4 + d5) % 3 == 0:
                if int(d4 + d5 + d6) % 5 == 0:
                    if int(d5 + d6 + d7) % 7 == 0:
                        if int(d6 + d7 + d8) % 11 == 0:
                            if int(d7 + d8 + d9) % 13 == 0:
                                if int(d8 + d9 + d10) % 17 == 0:
                                    ans += int(d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9 + d10)
                                    print(num)
    if count % 100000 == 0:
        print(count, "/", len(nums), ";", int(count / len(nums) * 100), "% completed!")

print("Total sums:", ans)
t2 = time.time()

print("Done in", t2 - t1, "seconds.")
