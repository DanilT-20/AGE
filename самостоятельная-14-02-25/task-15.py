ans = []
def f(a):
    for x in range(1,300):
        u = (not(x % a == 0)) <= ((x % 14 == 0) <= (not(x % 4 == 0)))
        if not u:
            return 0
    return 'privet'
for a in range(1, 300):
    if f(a):
        ans.append(a)
print(max(ans))