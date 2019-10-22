class Prob2Ans():
    a, b = 0, 1

    def __init__(self, limit=4000000, answer=0):
        self.limit = limit
        self.answer = answer
        while self.b < self.limit:
            if self.b % 2 == 0:
                self.answer += self.b
            self.a, self.b = self.b, self.a + self.b


if __name__ == '__main__':
    main = Prob2Ans()
    print(main.answer)
