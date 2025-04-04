from itertools import permutations, combinations
with open('9_4589.txt') as file:
    data = [list(map(int, s.split())) for s in file]
def f1(i):
    return max(i) < sum(i) - max(i)
def f2(i):
    for n in permutations(i):
        if sum(n[:2]) == sum(n[2:]):
            return 1
    return 0
def f3(i):
    for n in combinations(i, 2):
        if sum(n) == sum(i)-sum(n):
            return 1
    return 0
def f4(i):
    return max(i)+min(i) == sum(i) - min(i)-max(i)
count = 0
for num in data:
    if f1(num) and f2(num):
        count += 1
print(count)