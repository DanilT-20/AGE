ans = []
def f(a):
    for x in range(1, 1000):
        u = (not( x % 7 == 0) and (x % 13 == 0)) <= (x > a - 40)
        if not u:
            return 0
    return 1
for a in range(1, 1000):
    if f(a):
        ans.append(a)
print(max(ans))