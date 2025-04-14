with open('9_9740.txt') as file:
    data = [list(map(int, s.split())) for s in file]


def f1(n):
    cnt = [n.count(i) for i in n]
    return cnt.count(3) == 3 and cnt.count(1) == 4


def f2(n):
    np = [m for m in n if n.count(m) == 1]
    p = [m for m in n if n.count(m) > 1]
    if p:
        return sum(np) / len(np) <= sum(p) / len(p)
    return 0


count = 0
for i in data:
    if f1(i) and f2(i):
        count += 1
print(count)
