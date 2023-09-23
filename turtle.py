import turtle


p = turtle.Pen()
p.shape("turtle")
n = 3

while n >= 3:
    i = (n - 2) * 180/n
    p.left(180 - i / 2)
    
    for j in range(n):
        p.left(180 - i)
        p.forward(70 * (1 + n / 10))

    
    p.right(180 - i / 2)
    p.penup()
    p.forward(12 * ( 1 + n / 10))
    p.pendown()
    

    n += 1
    

turtle.done()
