def f1(x, y, A):
    return x * y > A
def f(A):
    for x in range(1, 1000):
        for y in range(1, 1000):
            f = (not f1(x, y, A+13)) <= f1(28, y, 520) or f1(x, 25, 800)
            if not f:
                return 0
    return 1
ans = []
for A in range(1, 1000):
    if f(A):
        ans.append(A)
print(max(ans))
