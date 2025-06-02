from itertools import product
count1 = 0
for p in product('0123456', repeat=5):
    p = ''.join(p)
    fl1 = True
    for i in range(len(p)-2):
        u = p[i:i+3]
        if not(len([1 for i in u if int(i) % 2 != 0])>0):
            fl1 = False
    count3 = 0
    for n in range(len(p)-1):
        u = p[n:n+2]
        if len([i for i in u if i in '0246']) == 2:
            count3 += 1
    if count3 >= 2 and fl1 and p[0] != '0':
        count1 += 1
print(count1)



