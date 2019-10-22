print('--------- Collatz Conjectures ---------')
print('This machine calculates which starting number has the longest steps under a certain limit.')
while True:
    limit = ''
    while type(limit) is not int:
        limit = input('Enter a limit number: ')
        try:
            limit = int(limit)
        except ValueError:
            print('Please enter a valid number!')

    nmaks = 0
    imaks = 0
    for i in range(1, limit):
        n = 0
        temp = i
        while i != 1:
            if i % 2 == 0:
                i /= 2
                i = int(i)
            else:
                i = 3 * i + 1
            n += 1
        if n > nmaks:
            nmaks = n
            imaks = temp
    print(str(imaks) + ' is the longest collatz under ' + str(limit) + ' with ' + str(nmaks) + ' steps.\n')
