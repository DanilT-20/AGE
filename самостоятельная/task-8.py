count = 0
from itertools import product
for x in product('0123456789AB', repeat=5):
    x = ''.join(x)
    if x[0]!= '0' and x.count('7') == 1 and len([i for i in x if i in '9AB']) <= 3:
        count += 1
print(count)

