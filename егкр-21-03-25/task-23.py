def f(num, end):
    if num == end:
        return 1
    if num > end or num == 9:
        return 0
    return f(num+1, end)+f(num*2,end)
print(f(2,12)*f(12, 42))