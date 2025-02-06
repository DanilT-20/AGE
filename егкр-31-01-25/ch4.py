from string import digits, ascii_uppercase
alph = digits + ascii_uppercase
ans = []
for x in alph[:25]:
    num = int(f'11353{x}12', 25) + int(f'135{x}21', 25)
    if num % 24 == 0:
        ans.append([x, num // 24])
print(max(ans))