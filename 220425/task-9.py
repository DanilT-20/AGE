

with open('9_18174 (2).txt') as file:
    data = [list(map(int, s.split())) for s in file]
def f1(n):
    count = [n.count(i) for i in n]
    return count.count(1) == 4
def f2(n):
    p = sum([i for i in n if i > 0])
    np = abs(sum([i for i in n if i < 0]))
    return np > p
count1 = 0
for i in data:
    if f1(i) and f2(i):
        count1 += 1
print(count1)