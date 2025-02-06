ans = []
def t(p, m):
    return p % m == 0
def f(A):
    for z in range(1, 100):
        for x in range(1, 100):
            for y in range(1, 100):
                u = (t(z, 115) or t(y, 78) or t(x, 51)) <= t(x, A)
                if not u:
                    return 0
    return 'igorek'
for A in range(1, 100):
    if f(A):
        ans.append(A)
print(max(ans))
