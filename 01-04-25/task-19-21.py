def f(x, y, s):
    if x+y >= 127: return s%2==0
    if s == 0: return 0
    h = [f(x +2, y, s-1), f(x, y+2, s-1), f(x*3, y, s-1), f(x, y*3, s-1)]
    return any(h) if (s-1)%2==0 else all(h)
print([s for s in range(1, 123) if f(s, 2, 2)],\
      [s for s in range(1, 123) if f(s, 2, 3) and not f(s, 2, 1)],\
      [s for s in range(1, 123) if f(s, 2, 4) and not f(s, 2, 2)])