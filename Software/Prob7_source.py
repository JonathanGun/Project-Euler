from Prime import is_prime


class Prob7Ans():
    def __init__(self, limit=10001, answer=0):
        self.limit = limit
        self.answer = self.count_answer()

    def count_answer(self):
        n = 1
        num = 1
        while n != self.limit:
            num += 2
            if is_prime(num):
                n += 1
        return num


if __name__ == '__main__':
    main = Prob7Ans()
    print(main.answer)
