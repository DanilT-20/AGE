ans = []
for x in range(1, 2031):
    num = 3**100 - x
    count = 0
    while num:
        if num % 3 == 0:
            count += 1
        num //= 3
    if count == 1:
        ans.append(x)
print(max(ans))