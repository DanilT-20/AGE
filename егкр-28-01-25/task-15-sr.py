def d(x, a):
    s = x % a == 0
    return s
def f(A):
    for x in range(1, 1000):
        N = (d(x, 10) and d(x, 26) and (x >= 300)) <= (A <= x)
        if not N:
            return 0
    return 1
ans = []
for A in range(-1000, 1000):
    if f(A):
        ans.append(A)
print(max(ans))

