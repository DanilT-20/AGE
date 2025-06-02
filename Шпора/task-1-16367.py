from itertools import permutations
matr = '246 16 57 15 347 127 356'.split()
graf =  'GB BA GA AC CF CD DF FE EB'.split()
print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x)+1) in matr[i.index(y)] for x,y in graf):
        print(*i)