with open('') as file:
    data = [list(map(int, s.split())) for s in file]
def f1(n):
    return [i for i in n if n.count(i) >= 3]
def f2(n):
    return [i for i in n if n.count(i) == 1]
def f3(n):
    pov = [[i, n.count(i)] for i in n if n.count(i)>1]
    npov = [i for i in n if n.count(i)!=1]
    return sum([i[0]*i[1] for i in pov])//6 > sum(npov)//6
count = 0
for i in data:
    if f1(i) and f2(i) and f3(i):
        count += 1
print(count)

