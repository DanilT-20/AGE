from itertools import product
ans = []
for pos, val in enumerate(product(sorted('аргумент'), repeat=4), start=1):
    val = ''.join(val)
    if len(set(val)) == len(val) and val == ''.join(sorted(val)):
        ans.append(pos)
print(max(ans))