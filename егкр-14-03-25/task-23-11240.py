def f(num, end, a=False):
    if num == end:
        return 1
    if num > end:
        return 0
    if a:
        return f(num+2, end) + f(num*3,end)
    return f(num+2, end)+ f(num**2, end, True)+f(num*3,end)
print(f(2, 64))
