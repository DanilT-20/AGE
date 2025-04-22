with open('24.5_19717.txt') as file:
    data = file.readline()
ans = 0
data = data.split('M')
for i in range(len(data)-278):
    data1 = data[i:i+279]
    ans = max(ans, len('M'.join(data1)))
print(ans)
