num = 343**1515-6*49**1520+5*49**1510-3*7**1530-1550
count = 0
while num:
    if num%7==0:
        count+=1
    num//=7
print(count)