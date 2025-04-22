from turtle import *
m = 15
tracer(0)
rt(90)
for n in range(15):
    fd(4*m)
    rt(60)
up()
for x in range(-20, 20):
    for y in range(-20,20):
        goto(x*m,y*m)
        dot(3, 'red')
update()
done()