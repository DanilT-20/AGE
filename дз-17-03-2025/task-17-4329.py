with open('17_4329.txt') as file:
    data = [int(i) for i in file]
def f(num):
    res = set()
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            res |= {i, num//i}
    return res
ans = []
maxx = max((f(i) for i in data), key=len)
for i in range(len(data)-1):
    num1, num2 = data[i:i+2]
    if len([i for i in f(num1) if i in maxx]) >= 3 and len([i for i in f(num2) if i in maxx]) >= 3:
        ans.append(len([i for i in f(num1) if i in f(num2)]))
print(len(ans), max(ans))