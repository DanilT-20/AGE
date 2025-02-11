with open('17_9786.txt') as file:
    data = [int(i) for i in file]
ans = []
maxx = max(i for i in data if abs(i) % 100 == 25)
for i in range(len(data)- 2):
    num1, num2, num3 = data[i: i+3]
    u1 = len(str(abs(num1))) == 4
    u2 = len(str(abs(num2))) == 4
    u3 = len(str(abs(num3))) == 4
    summ = num1 + num2 + num3
    if u1 + u2 + u3 <= 2 and summ <= maxx:
        ans.append(summ)
print(len(ans), max(ans))