class Prob4Ans():
    def __init__(self, digit=3, answer=0):
        self.digit = digit
        self.answer = max([a * b for a in range(10 ** digit, int(0.9 * (10 ** digit)), -1) for b in range(10 ** digit, int(0.9 * (10 ** digit)), -1) if len(str(a * b)) % 2 == 0 and str(a * b)[-int((len(str(a * b)) / 2)):] == (str(a * b)[:int((len(str(a * b)) / 2))])[::-1]])


if __name__ == '__main__':
    main = Prob4Ans()
    print(main.answer)
