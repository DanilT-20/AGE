for x in range(1, 150)[::-1]:
    num = 5*150**4 + 1*150**3 + x*150**2 + 2*150 + 9 + x*150**3 + 0 + 2*150 + 3
    if num%149==0:
        print(num//149)
        break