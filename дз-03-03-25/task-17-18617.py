with open('17_18617.txt') as file:
    data = [int(i) for i in file]
mi = min(i for i in data)
ma = max(i for i in data)
ans = []
for i in range(len(data)-1):
    num1, num2 = data[i], data[i+1]
    u1 = num1%3 == ma%3
    u2 = num2%3 == ma%3
    u3 = num1%7 == mi%7
    u4 = num2%7 == mi%7
    if (u1 + u2 > 0) and (u3 + u4 > 0):
        ans.append(num1+num2)
print(len(ans), max(ans))