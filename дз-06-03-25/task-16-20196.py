from functools import lru_cache
@lru_cache(None)
def f(num):
    if num < 110:
        return num
    if num >= 110:
        return num + f(num-1)
for i in range(2026):
    f(i)
print(f(2025) - f(2021))