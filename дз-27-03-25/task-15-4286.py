from itertools import combinations
def f(x):
    p = 1 <= x <= 98
    q = 25 <= x <= 42
    a = a1 <= x <= a2
    return q <= ((not (p) or q) <= a)
ans = []
line = [x/10 for x in range(0*10, 100*10)]
for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2-a1)
print(max(ans))