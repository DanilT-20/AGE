ans = []
with open('17_4597.txt') as file:
    data = [int(i) for i in file]
minim = min(data)
for i in range(len(data) - 1):
    num1, num2 = data[i], data[i+1]
    if num1 % 117 == minim or num2 % 117 == minim:
        ans.append(num1 + num2)
print(len(ans), max(ans))