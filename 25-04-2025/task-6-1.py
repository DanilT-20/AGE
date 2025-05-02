from turtle import *
tracer(0)
m = 5
screensize(10000, 10000)
rt(45)
for r in range(10):
    rt(45)
    fd(203*m)
    rt(45)
up()
backward(40*m)
rt(45)
down()
for r in range(5):
    fd(20*m)
    lt(90)
up()
for x in range(-300,40):
    for y in range(-300,40):
        goto(x*m,y*m)
        dot(2, 'red')
update()
done()


