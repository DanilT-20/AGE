from itertools import product
count = 0
for v in product('0123456789AB', repeat=7):
    v = ''.join(v)
    if v[0] != '0' and v.count('B') == 2 and '00' not in v and '02' not in v and '04' not in v and '06' not in v and '08' not in v and '0A' not in v and '22' not in v and '24' not in v and '26' not in v and '28' not in v and '2A' not in v and '44' not in v and '46' not in v and '48' not in v and '4A' not in v and '66' not in v and '68' not in v and '6A' not in v and '88' not in v and '8A' not in v and 'AA' not in v and '11' not in v and '13' not in v and '15' not in v and '17' not in v and '19' not in v and '1B' not in v and '33' not in v and '35' not in v and '37' not in v and '39' not in v and '3B' not in v and '55' not in v and '57' not in v and '59' not in v and '5B' not in v and '77' not in v and '79' not in v and '7B' not in v and '99' not in v and '9B' not in v and 'BB' not in v:
        count += 1
print(count)