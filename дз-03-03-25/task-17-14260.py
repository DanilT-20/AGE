with open('17_14260.txt') as file:
    data = [int(i) for i in file]
ans = []
mi = min(i for i in data if str(i)[0] != '-' and len(str(i)) == 4 and str(i)[-1] == str(i)[-2])
for i in range(len(data)-2):
    num1, num2, num3 = data[i], data[i+1], data[i+2]
    if len(str(abs(num1))) == len(str(abs(num2))) == len(str(abs(num3))) == 3 and num1+num2+num3>mi:
        ans.append(num1+num2+num3)
print(len(ans), max(ans))