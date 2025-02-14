with open('17_17873.txt') as file:
    d = [int(i) for i in file]
ans = []
minn = min(d)
for i in range(len(d) - 1):
    u = d[i] % 16 == minn
    u1 = d[i+1] % 16 == minn
    if u + u1 >= 1:
        ans.append(d[i] + d[i+1])
print(len(ans), max(ans))