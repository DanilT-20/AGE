for n in range(1, 10000):
    r = bin(n)[2:]
    r = r.replace('1', 'a').replace('0', '1').replace('a', '0')
    r = '1' + r
    if r.count('1')%2==0: r = r + '0'
    else: r = r + '1'
    r = int(r, 2)
    if r > 180:
        print(n)
        break