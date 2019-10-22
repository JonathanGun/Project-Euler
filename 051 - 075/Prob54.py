def royalflush(cards):
    coll = set()
    color = cards[0][1]
    for card in cards:
        if card[1] != color:
            return False
        coll.add(card[0])
    return coll == {'T', 'J', 'Q', 'K', 'A'}


def getnums(cards):
    cardnum = []
    for card in cards:
        card = card[0]
        if card == '2':
            cardnum.append(2)
        if card == '3':
            cardnum.append(3)
        if card == '4':
            cardnum.append(4)
        if card == '5':
            cardnum.append(5)
        if card == '6':
            cardnum.append(6)
        if card == '7':
            cardnum.append(7)
        if card == '8':
            cardnum.append(8)
        if card == '9':
            cardnum.append(9)
        if card == 'T':
            cardnum.append(10)
        if card == 'J':
            cardnum.append(11)
        if card == 'Q':
            cardnum.append(12)
        if card == 'K':
            cardnum.append(13)
        if card == 'A':
            cardnum.append(14)
    return sorted(cardnum)


def flush(cards):
    color = cards[0][1]
    for card in cards:
        if card[1] != color:
            return False
    return True


def straight(cards):
    cardnum = getnums(cards)
    last = cardnum[0]
    for i in range(1, len(cardnum)):
        cur = cardnum[i]
        if cur != last + 1:
            if cur != 2 and last != 14:
                return False
        last = cur
    return True


def straightflush(cards):
    return straight(cards) and flush(cards)


def samenum(cards):
    cards = getnums(cards)
    num = cards[0]
    ans = []
    cnt = 0
    for card in cards:
        if card == num:
            cnt += 1
        else:
            ans.append(cnt)
            cnt = 1
            num = card
    ans.append(cnt)
    return sorted(ans)[::-1]


def fourofakind(cards):
    return samenum(cards)[0] == 4


def fullhouse(cards):
    return samenum(cards)[:2] == [3, 2]


def highest(cards):
    return getnums(cards)[-1]


def threeofakind(cards):
    return samenum(cards)[0] == 3


def twopairs(cards):
    return samenum(cards) == [2, 2, 1]


def pair(cards):
    return samenum(cards)[0] == 2


def score(cards):
    h = highest(cards)
    if royalflush(cards):
        # print(cards)
        return [9]
    elif straightflush(cards):
        # print(cards)
        return [8, h]
    elif fourofakind(cards):
        # print(cards)
        nums = getnums(cards)[::-1]
        if nums[0] == nums[3]:
            return [7, nums[0], nums[4]]
        return [7, nums[1], nums[0]]
    elif fullhouse(cards):
        nums = getnums(cards)[::-1]
        if nums[0] == nums[2]:
            return [6, nums[0], nums[3]]
        return [6, nums[3], nums[0]]
    elif flush(cards):
        return [5, h]
    elif straight(cards):
        return [4, h]
    elif threeofakind(cards):
        nums = getnums(cards)[::-1]
        if nums[0] == nums[2]:
            return [3, nums[0], nums[3], nums[4]]
        elif nums[1] == nums[3]:
            return [3, nums[1], nums[0], nums[4]]
        return [3, nums[2], nums[0], nums[1]]
    elif twopairs(cards):
        pairs = []
        nums = getnums(cards)[::-1]
        for i in range(len(nums)):
            c1 = nums[i]
            for j in range(i + 1, len(nums)):
                c2 = nums[j]
                if c1 == c2:
                    pairs.append(c1)
        pairs.sort()
        pairs = pairs[::-1]
        single = []
        for c in nums:
            if c not in pairs:
                single.append(c)
        return [2, pairs[1], pairs[0], single[0]]
    elif pair(cards):
        nums = getnums(cards)[::-1]
        pairs = []
        found = False
        for i in range(len(nums)):
            c1 = nums[i]
            for j in range(i + 1, len(nums)):
                c2 = nums[j]
                if c1 == c2:
                    pairs.append(c1)
                    nums.remove(c1)
                    nums.remove(c2)
                    found = True
                    break
            if found:
                break
        return [1, pairs[0], nums[0], nums[1], nums[2]]
    else:
        return [0, h]


ans = 0
f = open('p054_poker.txt', 'r')
for line in f.readlines():
    line = line if line[-1] != '\n' else line[:-1]
    tmp = list(line.split(' '))
    player1 = score(tmp[:5])
    player2 = score(tmp[5:])
    if player1 > player2:
        ans += 1
f.close()
print(ans)
