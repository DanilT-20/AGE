from turtle import *
tracer(0)
m = 13
for x in range(10):
    fd(22*m)
    rt(90)
    fd(16*m)
    rt(90)
up()
fd(m)
rt(90)
fd(m)
lt(90)
down()
for x in range(10):
    fd(72*m)
    rt(90)
    fd(79*m)
    rt(90)
up()
for x in range(-40,40):
    for y in range(-40,40):
        goto(x*m, y*m)
        dot(3, 'white')
update()
done()