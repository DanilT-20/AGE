from itertools import product
ans = []
for pos, val in enumerate(product('МИНУС', repeat=4), start=1):
    val = ''.join(val)
    count_ch = 0
    count_nch = 0
    for p in val:
        if p in 'ИУ':
            count_ch += 1
        else:
            count_nch += 1
    if count_ch >= count_nch:
        ans.append(pos)
print(ans[-1])

