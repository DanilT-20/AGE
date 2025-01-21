def f(A):
    for x in range(7, 22):
        for y in range(1, 22):
            f = (x + y <= 22) or (y <= x - 6) or (y >= A)
            if not f:
                return 0
    return 1
ans = []
for A in range(1, 100):
    if f(A):
        ans.append(A)
print(max(ans))