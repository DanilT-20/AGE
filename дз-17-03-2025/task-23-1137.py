def f(num, end):
    if num == end: return 1
    if int(num) > int(end): return 0
    return f(bin(int(num, 2) + 1)[2:], end)+f(num+'0',end)+f(num+'1',end)
print(f('100', '11101'))