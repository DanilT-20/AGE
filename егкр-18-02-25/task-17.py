with open('17_19486.txt') as file:
    data = [int(i) for i in file]
ans = []
count = [i for i in data if str(i)[-1] == '7']
for i in range(len(data)-1):
    num1, num2 = data[i], data[i+1]
    u1 = str(num1)[0] == '-'
    u2 = str(num2)[0] == '-'
    if u1 + u2 == 1 and num1 + num2 < len(count):
        ans.append(num1 + num2)
print(len(ans), max(ans))