def f(A):
    for x in range(1000):
        for y in range(1000):
            if not((2*x + y != 70) or (x < y) or (A < x)):
                return False
    return True
ans = []
for A in range(1000):
    if f(A):
        ans.append(A)
print(max(ans))