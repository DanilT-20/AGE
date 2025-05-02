count = 0
for n in range(1, 100000):
    r = hex(n)[2:]
    if r.count('b')%2 == 0:
        r = '1' + r
    else: r = r + '1'
    r = int(r, 16)
    if len(str(r)) == 2:
        count += 1
print(count)