with open('9_6262.txt') as file:
    data = [list(map(int, s.split())) for s in file]
def f1(n):
    return len([i for i in n if n.count(i) > 1])
def f2(n):
    count = [i for i in n if i % 2 != 0]
    return len(count) == 3
count = 0
for x in data:
    if (f1(x) and (not f2(x))) or ((not f1(x)) and f2(x)):
        count += 1
print(count)
