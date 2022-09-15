import turtle

star= turtle.Turtle()


star.shape("circle")
star.speed(100)
turtle.bgcolor("black")
star.color("red", "#FFD700")

star.begin_fill()

star.forward(200)
star.right(144)
star.forward(200)
star.right(144)
star.forward(200)
star.right(144)
star.forward(200)
star.right(144)
star.forward(200)
star.right(144)

star.penup()
star.forward(400)
star.pendown()

star.forward(200)
star.right(144)
star.forward(200)
star.right(144)
star.forward(200)
star.right(144)
star.forward(200)
star.right(144)
star.forward(200)
star.right(144)

star.end_fill()



turtle.mainloop()
