from itertools import product
count = 0
for val in product('0123456', repeat=5):
    val = ''.join(val)
    if val[0]!='0' and val.count('6') == 1 and sum([int(i) for i in val if i in '0246']) < sum([int(i) for i in val if i in '135']):
        count += 1
print(count)