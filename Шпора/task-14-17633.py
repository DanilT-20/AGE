for x in range(1, 2031):
    num = 6**260 + 6**160 + 6**60 -x
    count = 0
    while num:
        if num%6==0:
            count += 1
        num//=6
    if count == 202:
        print(x)
        break