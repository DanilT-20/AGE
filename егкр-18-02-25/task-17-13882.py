with open('17_13882.txt') as file:
    data = [int(i) for i in file]
maxx = max(i for i in data if i % 401 == 0)
ans = []
for i in range(len(data)-2):
    num1, num2, num3 = data[i], data[i+1], data[i+2]
    u1 = sum(map(int, str(num1)))
    u2 = sum(map(int, str(num2)))
    u3 = sum(map(int, str(num3)))
    if u1 != u2 and u1 != u3 and u2 != u3 and num1 + num2 + num3 > maxx:
        ans.append(num1 + num2 + num3)
print(len(ans), min(ans))