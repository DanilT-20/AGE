def f(num, end, count=0):
    if num == end and count<=15:
        return 1
    if num > end:
        return 0
    if num % 2==0: count += 1
    return f(num+2,end, count)+f(num+3,end, count)+f(num*2+1,end,count)
print(f(1,55))