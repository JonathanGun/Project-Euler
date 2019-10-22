from math import gcd

ans = [1, 1]
for n in range(1, 10):
    for d in range(1, 10):
        for pad in range(1, 10):
            for pos in range(4):
                if pos == 0:
                    nn, dd = n * 10 + pad, d * 10 + pad
                elif pos == 1:
                    nn, dd = pad * 10 + n, d * 10 + pad
                elif pos == 2:
                    nn, dd = n * 10 + pad, pad * 10 + d
                elif pos == 3:
                    nn, dd = pad * 10 + n, pad * 10 + d

                if nn / dd == n / d and nn // dd == 0:
                    ans[0] *= n
                    ans[1] *= d
                    print(n, '/', d, '=', nn, '/', dd)
print(ans[1] // gcd(ans[0], ans[1]))
