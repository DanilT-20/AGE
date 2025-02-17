from itertools import product
ans = []
for pos, val in enumerate(product(sorted('марксл'), repeat=6), start=1):
    val = ''.join(val)
    if 'кс' not in val and 'ск' not in val:
        u = val.count(val[0]) == 3
        u1 = val.count(val[1]) == 3
        u2 = val.count(val[2]) == 3
        u3 = val.count(val[3]) == 3
        u4 = val.count(val[4]) == 3
        u5 = val.count(val[5]) == 3
        if u+u1+u2+u3+u4+u5 == 3 and len(set(val)) + 2 == len(val):
            ans.append(pos)
print(ans[-1])

