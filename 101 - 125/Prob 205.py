from itertools import product
dice1 = list(product([1, 2, 3, 4], repeat=9))
chance1 = [0 for x in range(37)]
for d in dice1:
    chance1[sum(d)] += 1
print(chance1)
dice2 = list(product([1, 2, 3, 4, 5, 6], repeat=6))
chance2 = [0 for x in range(37)]
for d in dice2:
    chance2[sum(d)] += 1
print(chance2)

tmp = sum(chance1) * sum(chance2)
wins = 0
for i in range(1, 37):
    wins += sum(chance2[:i]) * chance1[i]
print(round(wins / tmp, 7))
