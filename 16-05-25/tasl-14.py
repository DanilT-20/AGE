for x in range(1, 10001)[::-1]:
    num = 6**900+6**10-x
    count3 = 0
    count5 = 0
    while num:
        if num%6 == 3:
            count3+=1
        if num%6==5:
            count5 +=1
        num//=6
    if count3 == count5:
        print(x)
        break