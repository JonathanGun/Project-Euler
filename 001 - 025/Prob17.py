check = {1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9,
         18: 8, 19: 8, 20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6}

one_to_nine = (sum(check.get(i) for i in range(1, 10)))
one_to_nineteen = one_to_nine + (sum(check.get(i) for i in range(10, 20)))
twenty_to_ninetynine = (sum(check.get(i) for i in range(20, 100, 10))) * 10 + one_to_nine * 8
sumall = one_to_nineteen + twenty_to_ninetynine
for i in range(1, 10):
    sumall += (check.get(i) + len('hundred')) + (check.get(i) + len('hundred') + len('and')) * 99 + one_to_nineteen + twenty_to_ninetynine
sumall += check.get(1) + 8
print(sumall)
