def f(x, y, s):
    if x+y <= 72: return s%2==0
    if s == 0: return 0
    h = [f(x-3, y, s-1), f(x//2 if x%2 == 0 else x//2+1, y, s-1), f(x, y//2 if y%2==0 else y//2+1, s-1), f(x, y-3, s-1)]
    return any(h) if (s-1)%2==0 else all(h)
print([s for s in range(23, 500) if f(50, s, 2)],
      [s for s in range(23, 500) if f(50, s, 3) and not f(50, s, 1)],
      [s for s in range(23, 500) if f(50, s, 4) and not f(50, s, 2)])