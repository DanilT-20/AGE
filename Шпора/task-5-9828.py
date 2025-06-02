def f(num, sys):
    res = ''
    while num:
        res += str(num%sys)
        num//=sys
    return res[::-1]
ans = []
for n in range(1, 100000):
    r = f(n, 3)
    if n%3 == 0:
        r = '02' + r + '1'
    else: r = r + f((n%3)*4, 3)
    r = int(r, 3)
    if r<199:
        ans.append(n)
print(max(ans))