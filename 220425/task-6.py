from turtle import *
m = 15
tracer(0)
for r in range(7):
    fd(9*m)
    rt(90)
    fd(16*m)
    rt(90)
up()
fd(3*m)
rt(90)
fd(4*m)
lt(90)
down()
for r in range(4):
    fd(7*m)
    rt(90)
    fd(13*m)
    rt(90)
up()
for x in range(-20, 20):
    for y in range(-20,20):
        goto(x*m,y*m)
        dot(3, 'white')
update()
done()