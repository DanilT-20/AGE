with open('24_10105.txt') as file:
    data = file.readline()
data = data.split('T')
ans = []
for i in range(len(data)-100):
    dat = data[i:i+101]
    cnt = sum(map(len, dat))
    ans.append(cnt)
print(max(ans)+100)