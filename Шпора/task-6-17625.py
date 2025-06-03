from turtle import *
tracer(0)
m=12
screensize(10000, 10000)
for r in range(10):
    fd(22*m)
    rt(90)
    fd(16*m)
    rt(90)
up()
fd(1*m)
rt(90)
fd(1*m)
lt(90)
down()
for r in range(10):
    fd(72*m)
    rt(90)
    fd(79*m)
    rt(90)
up()
for x in range(-100, 100):
    for y in range(-100,100):
        goto(x*m, y*m)
        dot(3, 'white')
update()
done()
