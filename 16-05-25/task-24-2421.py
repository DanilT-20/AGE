with open('24_2421.txt') as file:
    data = file.readline()
ans = []
data = data.split('D')
for i in data:
    ans.append(len(i))
print(max(ans))