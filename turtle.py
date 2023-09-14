import turtle
import math

colors = ["blue","red"]
r = 20
n = 3
x = 0
y = 0

p = turtle.pen()
p.shape("turtle")

while True:
    for j in range(len(colors)):
        p.pencolor(colors[j])
        for i in range(n):
            if i == 0:
                p.left((360-((n-2)*180/n))/2)
                
            else:
                p.left(360/n)    
            p.forward(2*r*math.sin(math.pi/n))
        r += 10
        n += 1
        x += 10
        p.penup()
        p.goto(x, y)
        p.pendown()
        p.setheading(0)