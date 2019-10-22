from Prime import is_prime


class Prob5Ans():
    def __init__(self, limit=20, answer=0):
        self.limit = limit
        self.primes = list(n for n in range(self.limit) if is_prime(n))
        self.jump = self.mult(self.primes)
        self.answer = self.count_answer()

    def count_answer(self):
        num = 0
        found = False
        while not found:
            found = True
            num += self.jump
            for i in range(2, self.limit + 1):
                if int(num / i) != num / i:
                    found = False
                    break
        return num

    def mult(self, ls):
        ans = 1
        for item in ls:
            ans *= item
        return ans


if __name__ == '__main__':
    main = Prob5Ans()
    print(main.answer)
