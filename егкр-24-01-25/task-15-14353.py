def tr(A, y, x):
    f = (A + x > y) and (A + y > x) and (x + y > A)
    return f
def f(A):
    for x in range(1, 1000):
        f = tr(A, 7, x) <= ((max(x+5, 14) <= 27) == (not tr(36, 21, x)))
        if not f:
            return 0
    return 1
ans = []
for A in range(1, 1000):
    if f(A):
        ans.append(A)
print(max(ans))