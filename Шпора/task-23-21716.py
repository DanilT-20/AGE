def f(num, end):
    if num == end: return 1
    if num > end or num == 56: return 0
    return f(num+3, end) + f(num+7, end) + f(num*3, end)
print(f(12, 40)*f(40, 72)*f(72, 89))