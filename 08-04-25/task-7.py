from itertools import product
count = 0
for p in product('ДГИАШЭ', repeat=5):
    p = ''.join(p)
    if p[0] not in 'ИАЭ' and p[-1] not in 'ДГШ':
        count += 1
print(count)