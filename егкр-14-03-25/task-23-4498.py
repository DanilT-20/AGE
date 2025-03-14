def f(num, end, counta=0, countb=0, countc=0):
    if num == end and counta <= 4 and countb >= 2 and countc == 5:
        return 1
    if num >end:
        return 0
    return f(num*5, end, counta+1, countb, countc) + f(num*3, end, counta, countb+1, countc) + f(num+45, end, counta, countb, countc+1)
print(f(1, 2970))