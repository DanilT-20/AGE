for n in range(5, 10000):
    r = bin(n)[2:]
    if r.count('1') > r.count('0'):
        r = r + '0'
    else: r = r + '1'
    if len(r)%2 == 0:
        r = r[:len(r)//2-1] + r[len(r)//2 + 1:]
    else: r = r[:len(r)//2-1] + r[len(r)//2+2:]
    r = int(r, 2)
    if r == 55:
        print(n)
        break
