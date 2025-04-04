with open('09_9778.txt') as file:
    data = [list(map(int, s.split())) for s in file]
def f1(n):
    cnt = [n.count(i) for i in n]
    return cnt.count(2) == 2 and cnt.count(1) == 4
def f2(n):
    pov = [i for i in n if n.count(i) > 1]
    cnt = [n.count(i) for i in n]
    if cnt.count(2) == 2 and cnt.count(1)== 4:
        return pov[0] >= (sum(n) - pov[0]*2) / (len(n) - 2)
ans = []
for pos, i in enumerate(data):
    if f1(i) and f2(i):
        ans.append(pos)
print(min(ans))

