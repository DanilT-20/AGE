with open('17_17636.txt') as file:
    data = [int(i) for i in file]
ans = []
maxx = max(i for i in data if len(str(abs(i))) == 3 and str(i)[-1] == '3')
for i in range(len(data)-2):
    u = data[i:i+3]
    if len([n for n in u if len(str(abs(n))) == 3 and str(n)[-1] == '3']) >= 1 and sum(u) < maxx:
        ans.append(sum(u))
print(len(ans), max(ans))