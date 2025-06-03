def f1(i):
    cnt = [i.count(n) for n in i]
    return cnt.count(2)==4 and cnt.count(1)==3
def f2(i):
    return i.count(max(i)) == 1
with open('9_9832.txt') as file:
    data = [list(map(int, s.split())) for s in file]
for i in data:
    if f1(i) and f2(i):
        print(sum(i))
        break
