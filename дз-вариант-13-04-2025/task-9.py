with open('9_5489.txt') as file:
    data = [list(map(int, s.split())) for s in file]
def f1(i):
    return len(set(i)) == len(i)
def f2(i):
        return len([p for p in i if p%2==0]) > len([p for p in i if p%2!=0])
def f3(i):
        return sum([p for p in i if p%2==0]) < sum([p for p in i if p%2!=0])
count = 0
for i in data:
    if f1(i) and f2(i) and f3(i):
        count += 1
print(count)
