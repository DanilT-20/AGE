from itertools import permutations
# переписывает рёбра и значения матрицы (столбцов) и превращение их в списки
graph = 'AF AB BF FC CG GE ED AD EB'.split()
matrics = '37 367 125 56  34  247 126'.split()
# для удобства выведем номера столбцов матрицы
print(*range (1, 8))
# перебираем все возможные варианты
for i in permutations('ABCDEFG'):
#   смотрим на идекс и сравниваем
    if all(str(i.index(x) + 1) in matrics[i.index(y)] for x, y in graph):
        print(*i)