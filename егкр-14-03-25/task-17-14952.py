with open('17_14952.txt') as file:
    data = [int(i) for i in file]
ans = []
maxx = max(i for i in data if str(i)[-3:] == '121')
for i in range(len(data)-2):
    num1, num2, num3 = data[i], data[i+1], data[i+2]
    u1 = ((len(str(abs(num1))) == 4) + (abs(num1)%2==0)) == 2
    u2 = ((len(str(abs(num2))) == 4) + (abs(num2) % 2 == 0)) == 2
    u3 = ((len(str(abs(num3))) == 4) + (abs(num3) % 2 == 0)) == 2
    if u1 + u2 + u3 <= 1 and num1+num2+num3 <= maxx:
        ans.append(num1+num2+num3)
print(len(ans), max(ans))