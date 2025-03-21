ans = []
from string import ascii_uppercase, digits
alph = digits+ascii_uppercase
def f(num, sys):
    res = ''
    while num:
        res += alph[num%sys]
        num//=sys
    return res[::-1]
for n in range(1, 10000):
    r = f(n, 12)
    if n%3==0:
        r = '1' + r + 'B'
    else:
        r = '2' + r + '0'
    r = int(r,12)
    if r < 1996:
        ans.append(r)
print(max(ans))