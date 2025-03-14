ans = []
def f(num, end=0):
    if end == 13 and str(num)[0] == '-':
        ans.append(num)
        return 1
    if end == 13 and num >= 0:
        return 0
    return f(num-3,end+1) + f(num*(-3), end+1)
def g(num, end=0):
    if end == 13 and str(num)[0] == '-':
        return {num}
    if end == 13 and num >= 0:
        return set()
    return g(num-3,end+1) | g(num*(-3), end+1)
print(f(333), len(set(ans)), len(g(333)))
