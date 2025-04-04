with open('9_4614.txt') as file:
    data = [list(map(int, s.split())) for s in file]
def f1(n):
    return max(n) < sum(n) - max(n)
def f2(n):
    count = 0
    for i in n:
        if n.count(i) > 1:
            count += 1
    return count == 2
count = 0
for m in data:
    if f1(m) and f2(m):
        count += 1
print(count)