from turtle import *
tracer(0)
m = 12
for x in range(2):
    down()
    for x in range(2):
        fd(8*m)
        rt(90)
        fd(8*m)
        rt(90)
    up()
    fd(6*m)
    rt(90)
    fd(6*m)
    lt(90)
rt(180)
fd(4*m)
down()
for x in range(4):
    fd(8*m)
    rt(270)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*m, y*m)
        dot(3, 'white')
update()
done()
ans = 80





















