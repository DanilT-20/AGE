with open('17_17636.txt') as file:
    data = [int(i) for i in file]
ans = []
maxx = max(i for i in data if len(str(abs(i))) == 3 and str(i)[-1] == '3')
for i in range(len(data)-2):
    u = data[i:i+3]
    if len([1 for x in u if str(x)[-1] == '3' and len(str(abs(x))) == 3]) >= 1 and sum(u) < maxx:
        ans.append(sum(u))
print(len(ans), max(ans))