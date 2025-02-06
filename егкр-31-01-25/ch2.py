from itertools import product
count = 0
for val in product('012345678', repeat=7):
    val = ''.join(val)
    if val[0] not in '2046' and val[-1] != val[-2] or val[-1] != val[-3] or val[-2] != val[-3]:
        count += 1
print(count)