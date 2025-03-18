def f(num, end, a=False):
    if num == end:
        return 1
    if num > end+1:
        return 0
    if a:
        return f(num*2,end)+f(num*3,end)
    return f(num-1,end, True)+f(num*2,end)+f(num*3,end)
print(f(3, 15))