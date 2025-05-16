with open('24_3792 (1).txt') as file:
    data = file.readline()
data = data.replace('D', '*').replace('E','*')
data = data.split('*')
ans = []
for i in data:
    ans.append(len(i))
print(len(max([i for i in data], key=len)), max(ans))