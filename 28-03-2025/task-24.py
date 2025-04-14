with open('24_4643.txt') as file:
    data = file.readline()
ans = []
data = data.replace('1', '2').replace('B', 'A')
data = data.replace('22A', '*')
data = data.replace('A', '2')
data = data.replace('*2', '*-2').replace('2*', '2-*')
data = data.split('-')
for i in data:
    if '**' in data:
        ans.append(len(i))
print(max(ans))