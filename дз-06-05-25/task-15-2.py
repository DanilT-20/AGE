from itertools import combinations
def f(x):
    p = 257<=x<=1000
    q = 5<=x<=100
    r = 99<=x<=258
    a = a1<=x<=a2
    return (a <= r) and (not((a<=p)<=q))
ans = []
line = [x/10 for x in range(4*10, 1000*10)]
for a1,a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2-a1)
print(min(ans))