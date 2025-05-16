with open('24_9753.txt') as file:
    data = file.readline()

data = data.split('Y')
ans = []
for i in range(len(data)-150):
    dat = data[i:i+151]
    cnt = sum(map(len, dat))
    ans.append(cnt)
print(max(ans)+150)