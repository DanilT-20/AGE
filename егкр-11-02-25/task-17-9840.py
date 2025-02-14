with open('17_9840.txt') as file:
    data = [int(i) for i in file]
maxx = max(i for i in data if len(str(abs(i))) == 4 and abs(i) % 100 == 39)
ans = []
for i in range(len(data) - 1):
    num1, num2 = data[i], data[i+1]
    u = len(str(abs(num1))) == 4
    u1 = len(str(abs(num2))) == 4
    if u + u1 == 1 and (num1 + num2)**2 <= maxx**2:
        ans.append(num1 + num2)
print(len(ans), max(ans))
