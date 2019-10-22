class Prob3Ans():
    def __init__(self, num=600851475143, answer=[]):
        self.i = 2
        self.num = num
        self.answer = answer
        while (self.i <= self.num):
            while (self.num % self.i == 0):
                self.answer.append(self.i)
                self.num /= self.i
            self.i += 1
        self.answer = self.answer[-1]


if __name__ == "__main__":
    main = Prob3Ans()
    print(main.answer)
