from itertools import combinations
with open('17 (2)_7718.txt') as file:
    data = [int(i) for i in file]

ans = []
for i in combinations(data, 2):
    num1, num2 = i
    if ((num1+num2)%18 == 0) + ((num1*num2)%18==0) == 1:
        ans.append(num1+num2)
print(len(ans), max(ans))

