def f(A):
    for x in range(1, 1000):
        for y in range(1, 1000):
            t = (x - y >= 39) or (y <= x) or (y >= A - 20)
            if not t:
                return 0
    return 'wdf'
ans = []
for A in range(1000):
    if f(A):
        ans.append(A)
print(max(ans))