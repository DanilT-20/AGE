def f1(n):
    return max(n) < sum(n)-max(n)
def f2(n):
    return n[0]+n[1]!=n[2]+n[3] and n[0]+n[2]!= n[1]+n[3] and n[1]+n[2]!=n[0]+n[3]
with open('9_6897.txt') as file:
    data = [list(map(int, s.split())) for s in file]
count = 0
for i in data:
    if f1(i) and f2(i):
        count += 1
print(count)
