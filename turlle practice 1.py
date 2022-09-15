import turtle
t=turtle.Pen()

turtle.speed(10)
turtle.bgcolor('black')
colors = ["blue", "red", "yellow", "purple", "green", "orange"]

for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x//100+1)
    t.forward(x)
    t.right(59)
    

