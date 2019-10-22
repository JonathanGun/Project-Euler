def T(n):
    return n * (n + 1) / 2


def P(n):
    return n * (3 * n - 1) / 2


def H(n):
    return n * (2 * n - 1)


t, p, h = 1, 1, 1
valT = T(t)
valP = P(p)
valH = H(h)

answer = 0

while answer < 50000:
    if valT == valP and valT == valH:
        answer = valT
        print(answer, t, p, h)
        print("FOUND")

    next = min(valT, valP, valH)
    if next == valT:
        t += 1
        valT = T(t)
    elif next == valP:
        p += 1
        valP = P(p)
    elif next == valH:
        h += 1
        valH = H(h)
