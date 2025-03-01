from functools import lru_cache

@lru_cache(100_000)
def expr(target: int, digits: int) -> bool: # can you express target t with digits d, only adding +'s
    if target > digits:
        return False
    if target == digits:
        return True
    left_part = digits // 10
    right_part = digits % 10
    n = 1
    while left_part > 0:
        if expr(target - left_part, right_part):
            # print("found", target, digits, left_part, right_part)
            return True
        right_part = (left_part % 10) * 10**n + right_part
        left_part //= 10
        digits //= 10
        n += 1
    return False

# def aupto(limit):
#     alst, k, k2 = [], 0, 0
#     while k2 <= limit:
#         if expr(k, str(k2)):
#             alst.append(k2)
#         k, k2 = k+1, k2 + 2*k + 1
#     return alst

def aupto(limit) -> int:
    k, k_sq = 0, 0
    ans = 0
    while k_sq <= limit:
        # check if k is power of 10, i.e: 10, 100, 1000, 1000 (without calling log10 or using power **)
        tmp = k
        while tmp % 10 == 0 and tmp > 0:
            tmp //= 10
        if tmp == 1:
            print("case", k, k_sq)
            ans += k_sq
        elif expr(k, k_sq):
            ans += k_sq
        k, k_sq = k+1, k_sq + 2*k + 1
    return ans - 1


n = int(input())
N = 10**n
print(aupto(N))
