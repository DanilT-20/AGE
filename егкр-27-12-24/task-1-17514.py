from itertools import permutations
graph = 'AB BH AH EA EG EC FH FG FD DC'.split()
matrix = ''.split()
print(*range(1, 9))
for i in permutations('ABCDEFGH'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)