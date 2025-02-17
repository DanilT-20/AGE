with open('17_19249.txt') as file:
    data = [int(i) for i in file]
ans = []
maxx = max(i for i in data if str(abs(i))[-2:] == '43' and len(str(abs(i))) == 5)**2
for i in range(len(data) - 2):
    num1, num2, num3 = data[i], data[i+1], data[i+2]
    u1 = len(str(abs(num1))) == 5 and str(num1)[-2:] == '43'
    u2 = len(str(abs(num2))) == 5 and str(num2)[-2:] == '43'
    u3 = len(str(abs(num3))) == 5 and str(num3)[-2:] == '43'
    if u1 + u2 + u3 >= 1 and num1**2 + num2**2 + num3**2 <= maxx:
        ans.append(num1**2 + num2**2 + num3**2)
print(len(ans), min(ans))
