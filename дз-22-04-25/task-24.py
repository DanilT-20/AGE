with open('24.5_19717.txt') as file:
    data = file.readline()
ans = []
data = data.split('M')
for i in range(len(data)):
    count = 1
    for i1 in range(i+1, len(data)):
        count += 1
        if count == 278:
            data1 = data[i:i1+1]
            ans.append(len(''.join(data1)))
print(max(ans))
