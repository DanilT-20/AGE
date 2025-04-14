with open('9.txt') as file:
    data = [list(map(int, s.split())) for s in file]
def f1(i):
    cnt = [i.count(x) for x in i]
    return cnt.count(3) == 6
def f2(i):
    p = [x for x in i if i.count(x) > 1]
    np = [x for x in i if i.count(x) == 1]
    if len(np) == 1:
        return max(p) > np[0]
    return 0
count = 0
for i in data:
    if f1(i) and f2(i):
        count += 1
print(count)