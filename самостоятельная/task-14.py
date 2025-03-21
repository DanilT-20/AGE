ans = []
for x in range(1, 2006):
    num = 4**163*5+12**62-x
    count1 = 0
    count4 = 0
    while num:
        if num % 5 == 1:
            count1+=1
        if num%5==4:
            count4+=1
        num//=5
    if count1 < count4:
        ans.append(x)
print(max(ans))