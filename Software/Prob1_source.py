class Prob1Ans():
    def __init__(self, limit=1000, div_by=(3, 5), answer=0):
        self.limit = limit
        self.div_by = div_by
        self.answer = sum(x for x in range(self.limit) if x % self.div_by[0] == 0 or x % self.div_by[1] == 0)


if __name__ == '__main__':
    main = Prob1Ans()
    print(main.answer)
