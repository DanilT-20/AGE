def f(x, s):
    if 36<=x<=85:return s%2==0
    if x >85: return s%2!=0
    if s == 0: return 0
    h = [f(x+2, s-1), f(x*3, s-1)]
    return any(h) if (s-1)%2==0 else all(h)
print([f(6, 16)])
