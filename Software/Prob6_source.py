class Prob6Ans():
    def __init__(self, limit=100, answer=0):
        self.limit = limit
        self.answer = sum(i for i in range(limit + 1))**2 - sum(i**2 for i in range(limit + 1))


if __name__ == '__main__':
    main = Prob6Ans()
    print(main.answer)
