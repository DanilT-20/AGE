with open('24_4544.txt') as file:
    data = file.readline()
data = data.replace('XIX', ' ').split()
print(len(max(data, key=len))+4)