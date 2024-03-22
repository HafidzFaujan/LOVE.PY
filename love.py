import turtle

turtle.bgcolor("#0004ff")
turtle.pensize(3)

a = turtle.Turtle()
a.penup()
a.goto(-200, 60)
a.pendown()
a.color("red")
style = ("courier", 30, "italic")
a.write("I", font=style, align="left")
a.hideturtle()


def curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)


turtle.speed()
turtle.color("red", "pink")

turtle.begin_fill()
turtle.left(140)
turtle.forward(111.0)
curve()

turtle.left(120)
curve()
turtle.forward(111.65)
turtle.end_fill()
turtle.hideturtle()

a = turtle.Turtle()
a.penup()
a.goto(-40, 75)
a.pendown()
a.color("red")
style = ("courier", 10, "italic")
a.write("LOVE", font=style)
a.hideturtle()
style = ("courier", 30, "italic")
a = turtle.Turtle()
a.penup()
a.goto(-2, 75)
a.pendown()
a.color("red")
style = ("courier", 10, "italic")
a.write("SIAPA", font=style, align="left")
a.hideturtle()

a = turtle.Turtle()
a.penup()
a.goto(180, 60)
a.pendown()
a.color("red")
style = ("courier", 20, "italic")
a.write("YOU", font=style, align="left")
a.hideturtle()

a = turtle.Turtle()
a.penup()
a.goto(-150, -130)
a.pendown()
a.color("red")
style = ("courier", 30, "italic")
a.write("ANJAY MABAR", font=style)
a.hideturtle()


turtle.done()
