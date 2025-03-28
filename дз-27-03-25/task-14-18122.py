for x in range(1, 5555)[::-1]:
    count = 0
    num = 5**150+5**135-x
    while num:
        if num % 5 == 4:
            count += 1
        num //= 5
    if count == 134:
        print(x)
        break