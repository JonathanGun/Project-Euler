from copy import deepcopy
from itertools import combinations


def showGrid(grid):
    for i in range(len(grid)):
        print(i + 1, grid[i])
    i = 0
    finished = True
    for gr in grid:
        j = 0
        if i % 3 == 0:
            print(".-----------------------.")
        for g in gr:
            if j % 3 == 0:
                print("|", end=" ")
            if len(g) > 1:
                print(0, end=" ")
                finished = False
            else:
                print(list(g)[0], end=" ")
            j += 1
        i += 1
        print("|")
    print("'-----------------------'")
    if not finished:
        quit()


def solve(grid):
    solution = []
    for g in grid:
        solution.append(list(map(lambda x: set([x]) if x != 0 else set(range(1, 10)), g)))

    last = None
    while last != solution:
        last = deepcopy(solution)

        for i in range(9):
            sol = solution[i]
            for j in range(9):
                s = sol[j]
                ii = i // 3
                jj = j // 3

                # elmt in 1 row
                cnt = 0
                for k in range(9):
                    if s == sol[k]:
                        cnt += 1

                if len(s) == cnt:
                    for k in range(9):
                        if s != sol[k]:
                            sol[k] -= s

                for x in range(1, 10):
                    cntx = [x in sol[k] for k in range(9)]
                    if sum(cntx) == 1:
                        for k in range(9):
                            if cntx[k]:
                                sol[k] = set([x])
                    else:
                        for r in range(3):
                            if sum(cntx[r * 3:r * 3 + 3]) == sum(cntx):
                                for k in range(ii * 3, ii * 3 + 3):
                                    if k == i:
                                        continue
                                    for l in range(r * 3, r * 3 + 3):
                                        solution[k][l] -= set([x])

                # elmt in 1 col
                cnt = 0
                for k in range(9):
                    if s == solution[k][j]:
                        cnt += 1

                if len(s) == cnt:
                    for k in range(9):
                        if s != solution[k][j]:
                            solution[k][j] -= s

                for x in range(1, 10):
                    cntx = [x in solution[k][j] for k in range(9)]
                    if sum(cntx) == 1:
                        for k in range(9):
                            if cntx[k]:
                                solution[k][j] = set([x])
                    else:
                        for c in range(3):
                            if sum(cntx[c * 3:c * 3 + 3]) == sum(cntx):
                                for k in range(c * 3, c * 3 + 3):
                                    for l in range(jj * 3, jj * 3 + 3):
                                        if l == j:
                                            continue
                                        solution[k][l] -= set([x])

                # elmt in 1 box
                cnt = 0
                for k in range(ii * 3, ii * 3 + 3):
                    for l in range(jj * 3, jj * 3 + 3):
                        if s == solution[k][l]:
                            cnt += 1

                if len(s) == cnt:
                    for k in range(ii * 3, ii * 3 + 3):
                        for l in range(jj * 3, jj * 3 + 3):
                            if solution[k][l] != s:
                                solution[k][l] -= s

                for x in range(1, 10):
                    cntx = []
                    for k in range(ii * 3, ii * 3 + 3):
                        for l in range(jj * 3, jj * 3 + 3):
                            cntx.append(x in solution[k][l])
                    if sum(cntx) == 1:
                        for k in range(9):
                            if cntx[k]:
                                solution[ii * 3 + k // 3][jj * 3 + k % 3] = set([x])
                    elif sum(cntx) <= 3:
                        for r in range(3):
                            if (cntx[r * 3] + cntx[r * 3 + 1] + cntx[r * 3 + 2]) == sum(cntx):
                                for k in range(9):
                                    if (k < jj * 3) or (k >= jj * 3 + 3):
                                        solution[ii * 3 + r][k] -= set([x])

                        for c in range(3):
                            if (cntx[c] + cntx[c + 3] + cntx[c + 6]) == sum(cntx):
                                for k in range(9):
                                    if (k < ii * 3) or (k >= ii * 3 + 3):
                                        solution[k][jj * 3 + c] -= set([x])

        # hidden double
        if last == solution:
            for i in range(9):
                sol = solution[i]
                for j in range(9):
                    s = sol[j]
                    ii = i // 3
                    jj = j // 3

                    for subset in list(combinations(s, 2)):
                        cntsubs = []
                        for k in range(9):
                            if subset[0] in solution[i][k] or subset[1] in solution[i][k]:
                                cntsubs.append(k)
                        if len(cntsubs) == 2:
                            if solution[i][cntsubs[0]] != set(subset):
                                solution[i][cntsubs[0]] = set(subset)
                                solution[i][cntsubs[1]] = set(subset)

                        cntsubs = []
                        for k in range(9):
                            if subset[0] in solution[k][j] or subset[1] in solution[k][j]:
                                cntsubs.append(k)
                        if len(cntsubs) == 2:
                            if solution[cntsubs[0]][j] != set(subset):
                                solution[cntsubs[0]][j] = set(subset)
                                solution[cntsubs[1]][j] = set(subset)

        # x-wing
        if last == solution:
            for i in range(9):
                sol = solution[i]
                for j in range(9):
                    s = sol[j]
                    ii = i // 3
                    jj = j // 3

                    for k in range(9):
                        for kk in range(k + 1, 9):
                            for x in range(1, 10):
                                cntxk = [x in solution[k][l] for l in range(9)]
                                cntxkk = [x in solution[kk][l] for l in range(9)]
                                if sum(cntxk) == 2 and cntxk == cntxkk:
                                    l1 = cntxk.index(True)
                                    l2 = 8 - cntxk[::-1].index(True)
                                    for r in range(9):
                                        if r != k and r != kk:
                                            solution[r][l1] -= set([x])
                                            solution[r][l2] -= set([x])

    showGrid(solution)
    ans = 0
    for i in range(3):
        ans *= 10
        ans += list(solution[0][i])[0]
    return ans


grid = None
ans = 0
f = open('p96_sudoku.txt', 'r')
for i in f.readlines():
    if i.split()[0] == "Grid":
        if grid:
            ans += solve(grid)
        grid = []
        print(i)
    else:
        grid.append(list(map(int, i[:-1] if i[-1] == '\n' else i)))
f.close()
ans += solve(grid)

print(ans)
