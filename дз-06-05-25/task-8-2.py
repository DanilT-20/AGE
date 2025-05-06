from itertools import product
for pos, val in enumerate(product(sorted('цапля'), repeat=5), start=1):
    val = ''.join(val)
    if val.count('а') <= 1 and val.count('ц')==2 and val.count('л')==0:
        print(pos)
        break