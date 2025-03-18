def f(num, end, count=0):
    if num == end and count == 51:
        return 1
    if num > end:
        return 0
    return f(num*4,end,count+1) + f(num+1,end,count+1) + f(num*3,end,count+1)
print(f(2, 404))