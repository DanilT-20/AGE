from string import digits, ascii_uppercase
from itertools import product
alph = digits + ascii_uppercase
count = 0
for v in product(alph[:20], repeat=5):
    v = ''.join(v)
    if v[0] in alph[::2] and v[1] in alph[1::2] and v[2] in alph[::2] and v[3] in alph[1::2] and v[4] in alph[::2] or v[0] in alph[1::2] and v[1] in alph[::2] and v[2] in alph[1::2] and v[3] in alph[::2] and v[4] in alph[1::2]:
        if int(v[0], 20) + int(v[-1], 20) == 26 and v[0] != 0:
            count += 1
print(count)

