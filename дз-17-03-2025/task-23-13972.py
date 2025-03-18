def f(num, end, count=0):
    if num == end: return 1
    if num > end: return 0
    if count == 0 and num != 23:
        return f(num+2,end,count=1)+f(num*2,end,count=1)
    return f(num+2,end,count)+f(num*2,end,count)+f(num+5,end,count)
print(f(7,23)*f(23,35))
