from itertools import product
for pos, val in enumerate(product(sorted(set('калейдоскоп'))[::-1], repeat=6), start=0):
    val = ''.join(val)
    if pos % 2 == 0 and val[0] == 'к' and val.count('й') == 2 and 'с' not in val and 'е' not in val:
        print(pos)
        break

