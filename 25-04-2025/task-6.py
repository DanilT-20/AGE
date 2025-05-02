from turtle import *
tracer(0)
m = 10
screensize(10000, 10000)
for r in range(2):
    fd(5*m)
    rt(90)
    fd(11*m)
    rt(90)
up()
fd(-4*m)
rt(90)
fd(6*m)
lt(90)
down()
for r in range(2):
    fd(42*m)
    rt(90)
    fd(63*m)
    rt(90)
up()
for x in range(-80,80):
    for y in range(-80,80):
        goto(x*m, y*m)
        dot(3, 'white')
update()
done()