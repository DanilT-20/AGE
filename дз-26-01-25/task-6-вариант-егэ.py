from turtle import *
m = 6
tracer(0)
for x in range(9):
    fd(15*m)
    rt(90)
    fd(25*m)
    rt(90)
up()
bk(10*m)
rt(90)
down()
for x in range(8):
    fd(15*m)
    lt(90)
    fd(25*m)
    lt(90)
up()
fd(6*m)
lt(90)
down()
for x in range(7):
    fd(15*m)
    rt(90)
    fd(25*m)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*m, y*m)
        dot(3, 'red')
update()
done()

