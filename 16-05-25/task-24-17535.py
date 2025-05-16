with open('24_17535 (1).txt') as file:
    data = file.readline()
data = data.split('CD')
ans = []
for i in range(len(data)-160):
    dat = data[i:i+161]
    cnt = sum(map(len, dat))
    ans.append(cnt)
print(max(ans)+160*2+2)