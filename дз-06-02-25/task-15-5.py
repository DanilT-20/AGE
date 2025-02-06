ans = []
def f(A):
    for x in range(1, 1000):
        for B in range(80, 101):
            u = (x % 17 == 0) <= ((not(str(x) in str(B))) or (A < x + 30))
            if not u:
                return 0
    return 'asd'
for A in range(1, 1000):
    if f(A):
        ans.append(A)
print(ans[-1])

