with open('17.txt') as file:
    data = [int(i) for i in file]
ans = []
summ = sum([n for n in data if n < 0])
for i in range(len(data)-2):
    u = data[i:i+3]
    if max(u)*min(u)>summ:
        ans.append(sum(u))
print(len(ans), abs(max(ans)))