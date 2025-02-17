with open('17.txt') as file:
    data = [int(i) for i in file]
ans = []
maxx = max(i for i in data if str(i)[-2:] == '50')
for i in range(len(data) - 2):
    num1, num2, num3 = data[i], data[i+1], data[i+2]
    if num1 != num2 and num2 != num3 and num1 != num3:
        u1 = len(str(abs(num1))) == 5
        u2 = len(str(abs(num2))) == 5
        u3 = len(str(abs(num3))) == 5
        if u1 + u2 + u3 == 3 and num1 + num2 + num3 <= maxx:
            ans.append(num1 + num2 + num3)
print(len(ans), max(ans))
