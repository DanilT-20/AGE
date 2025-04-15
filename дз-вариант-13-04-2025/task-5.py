def convert(n, s):
    res = ''
    while n:
        res += str(n%s)
        n//=s
    return res[::-1]
for n in range(1, 10000)[::-1]:
    r = convert(n, 3)
    if n % 5 == 0: r = r+ r[-3:]
    else: r = r + convert((n%5)*5, 3)
    r = int(r, 3)
    if r < 5496:
        print(n)
        break
