ans = []
with open('17_9748.txt') as file:
    data = [int(i) for i in file]
maxx = max(i for i in data if i % 100 == 15)
for i in range(len(data) - 2):
    num1, num2, num3 = data[i], data[i+1], data[i+2]
    nums = [num1, num2, num3]
    if ([len(str(i)) for i in nums].count(4) == 1) and sum(map(int, str(num1) + str(num2) + str(num3))) >= maxx:
        ans.append(sum(map(int, str(num1) + str(num2) + str(num3))))
print(len(ans), max(ans))
