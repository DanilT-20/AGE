from itertools import product
from string import ascii_uppercase, digits
alph = digits + ascii_uppercase
ans = []
for v in product(alph[:25], repeat=4):
    v = ''.join(v)
    count_ch = 0
    for c in alph[1::2]:
        count_ch += v.count(c)
    count = 0
    for x in alph[:6]:
        count += v.count(x)
    if count_ch == 1 and count <= 2 and v[0] != '0':
        ans.append(v)
print(len(ans))
