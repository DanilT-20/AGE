from itertools import combinations
def f(x):
    P = 5 <= x <= 40
    Q = 41 <= x <= 54
    R = 6 <= x <= 53
    A = A1 <= x <= A2
    if not (((not P) <= Q) and R and not A):
        return 1
ans = []
line = [x/10 for x in range(4*10, 56*10)]
for A1, A2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)
print(min(ans))