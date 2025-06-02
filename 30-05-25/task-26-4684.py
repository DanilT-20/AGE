with open('26_4684.txt') as file:
    N = int(file.readline())
    price = [int(i) for i in file]
price = sorted(price)
Shop = sum(price) - sum(price[:N//6])/2
price = sorted(price, reverse=True)
men = sum(price) - sum(price[5::6])/2
print(men, Shop)