def f1(i):
    cnt = [i.count(n) for n in i]
    return cnt.count(2) == 2 and cnt.count(1) == 4
def f2(i):
    pov = [n for n in i if i.count(n)>1]
    npov = [n for n in i if i.count(n)==1]
    return pov[0]>=sum(npov)/4
with open('09_9778.txt') as file:
    data = [list(map(int, s.split())) for s in file]
count = 0
for i in data:
    count += 1
    if f1(i) and f2(i):
        print(count)
        break