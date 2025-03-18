ans = []
def f(num, end=0, a=False, b=False, c=False):
    if end == 24: return ans.append(num)
    if num > end: return 0
    if a: return f(num+7,end+1,a=False,b=True,c=False)+f(num*4,end+1,a=False,b=False,c=True)
    if b: return f(num+1,end+1,a=True,b=False,c=False)+f(num*4,end+1,a=False,b=False,c=True)
    if c: return f(num+7,end+1,a=False,b=True,c=False)+f(num+1,end+1,a=True,b=False,c=False)
    return f(num+1,end+1,a=True,b=False,c=False)+f(num+7,end+1,a=False,b=True,c=False)+f(num*4,end+1,a=False,b=False,c=True)
print(len(set(ans)))


