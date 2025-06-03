def f1(i):
    cnt = [i.count(n) for n in i]
    return cnt.count(3)==3 and cnt.count(1)==3
def f2(i):
    pov = [n for n in i if i.count(n)>1]
    npov = [n for n in i if i.count(n)==1]
    return sum(pov)**2 > sum(npov)**2
with open('09_17550.txt') as file:
    data = [list(map(int, s.split())) for s in file]
count = 0
for i in data:
    if f1(i) and f2(i):
        count+=1
print(count)
