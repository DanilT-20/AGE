ans = []
for x in range(1, 111):
    num = x*111**3 + 3*111**2 + 2*111+1 + 211**3+7*211**2+x*211+4
    if num % 111 == 0:
        ans.append([x, num//111])
print(max(ans))
