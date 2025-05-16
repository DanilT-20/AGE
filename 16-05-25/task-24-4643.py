with open('24_4643.txt') as file:
    data = file.readline()
data = data.replace('1', '2').replace('A', 'B')
data = data.replace('22B', '*')
data = data.replace('2', 'B')
data = data.split('B')
print(max([i.count('*') for i in data]))