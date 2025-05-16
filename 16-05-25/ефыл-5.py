for n in range(2, 10000):
    r = bin(n)[2:]
    count1 = [i for i in r[1::2] if i == '1']
    count2 = [i for i in r[::2] if i == '0']
    r = abs(len(count2)-len(count1))
    if r == 5:
        print(n)
        break
