with open('9_12918.txt') as file:
    data = [list(map(int, s.split())) for s in file]
def f1(i):
    count = [i.count(x) for x in i]
    return count.count(2) == 4
def f2(i):
    return i.count(max(i)) == 1
def f3(i):
    return max(i)*min(i) > sum(i)-max(i)-min(i)
for x in data:
    if f1(x) and f2(x) and f3(x):
        print(sum(x))
        break















