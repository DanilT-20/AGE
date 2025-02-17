from turtle import *
m = 10
tracer(0)
up()
for x in range(10):
    rt(120*m)
    fd(10*m)
down()
for x in range(7):
    fd(15*m)
    rt(90)
for x in range(5):
    rt(60)
    fd(20*m)
    rt(30)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*m, y*m)
        dot(4, 'red')
update()
done()
