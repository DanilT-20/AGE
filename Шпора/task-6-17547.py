from turtle import *
tracer(0)
screensize(10000, 10000)
m=12
for r in range(3):
    fd(7*m)
    rt(90)
    fd(12*m)
    rt(90)
up()
fd(4*m)
rt(90)
fd(6*m)
lt(90)
down()
for r in range(4):
    fd(83*m)
    rt(90)
    fd(77*m)
    rt(90)
up()
for x in range(-100,100):
    for y in range(-100,100):
        goto(x*m, y*m)
        dot(3, 'red')
update()
done()
