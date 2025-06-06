with open('17_17873.txt') as file:
    data = [int(i) for i in file]
ans = []
minn = min(data)
for i in range(len(data)-1):
    u = data[i:i+2]
    if len([i for i in u if i%16==minn]) >= 1:
        ans.append(sum(u))
print(len(ans), max(ans))