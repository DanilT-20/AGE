from string import digits, ascii_uppercase
alph = digits + ascii_uppercase
ans = []
for x in alph[:22]:
    num1 = int(f'A23{x}AC0', 22)
    num2 = int(f'GB{x}21670', 22)
    num = num1 + num2
    if num % 21 == 0:
        ans.append([x, num // 22])
print(max(ans))