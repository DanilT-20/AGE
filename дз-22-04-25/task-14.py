ans = []
for x in range(2, 2026):
    num = 5**2025 + 5**200 - x
    count = 0
    while num:
        if num%5==4:
            count+=1
        num //= 5
    ans.append([count, x])
print(max(ans))