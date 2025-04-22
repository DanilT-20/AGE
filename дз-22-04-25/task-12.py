#print(1600/(12+15), 1600/(12+12), 19*6/8, (15*5+4*4)/8)
st = '1' + 90*'0'
while '1' in st:
    if '10' in st:
        st = st.replace('10','0001', 1)
    else:
        st = st.replace('1', '000', 1)
print(st.count('0'))