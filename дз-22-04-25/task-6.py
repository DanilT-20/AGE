from turtle import *
m = 25
tracer(0)
lt(90)
for n in range(15):
    fd(4*m)
    rt(60)
up()
for x in range(20):
    for y in range(20):
        goto(x*m,y*m)
        dot(3, 'red')
goto(0,0)
dot(7, 'red')
update()
done()